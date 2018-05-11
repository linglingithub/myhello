__author__ = 'linglin'

"""
Input: excel file in .xlsx format, with tabs starting with "lc_***", where *** will be parsed into int id of learning centers.
Output:
"""
import xlrd
import os
from collections import defaultdict
import json


grade_outline_xls = "Downloads/Afficient English Language Arts Chapter Outline.xlsx"

HOME = os.path.expanduser("~")
SHEET_PREFIX = "lc_"
COL_NAME = 0
COL_COMMENT = 4


class StudentLCGenerator:
    def __init__(self, in_excel="aa_student_lc.xlsx"):
        self._infile = os.path.join(HOME, "Documents", in_excel)
        self._outdict = {}   # name: lc_id
        self._manual_check = defaultdict(list) # name: lc_id

    def generate_student_lc_dict(self):
        workbook = xlrd.open_workbook(self._infile)
        sheet_names = workbook.sheet_names()

        # worksheets = workbook.get_sheets()
        #for sheet in worksheets:
        for sheet_name in sheet_names:
            if not sheet_name.startswith(SHEET_PREFIX):
                continue
            sheet = workbook.sheet_by_name(sheet_name)
            lc_id = self._get_lc_id(sheet.name)
            self._parse_sheet(sheet, lc_id)

    def _get_lc_id(self, sheetname):
        idstr = sheetname[3:]
        return int(idstr)

    def _parse_sheet(self, worksheet, lc_id):
        row_cnt = worksheet.nrows
        for i in range(1, row_cnt):
            row = worksheet.row(i)
            student_name = str(row[COL_NAME].value).strip()
            if student_name == "":
                continue
            if student_name in self._outdict:
                self._manual_check[student_name].append(lc_id)
            self._outdict[student_name] = lc_id
            student_comment = str(row[COL_COMMENT].value).strip()
            if student_comment != "":
                self._manual_check[student_name].append(str(lc_id) + " - " + student_comment)



    def update_db_users_lc(self):
        pass


    def run(self):
        self.generate_student_lc_dict()
        self.update_db_users_lc()
        for k, v in self._outdict.items():
            print(k, " === ", v)
        print("\r\n==================This is a separate line ==================\r\n")
        for k, v in self._manual_check.items():
            print(k, " >>> ", v)


if __name__ == '__main__':
    loader = StudentLCGenerator()
    loader.run()