__author__ = 'linglin'


import csv
from os.path import expanduser
from collections import OrderedDict
import json
import re


home = expanduser("~")

grade_id = 9
problem_count_csv = home + '/Downloads/g'+ str(grade_id) +'_problem_count.csv'
problem_count_out = home + '/Documents/g'+ str(grade_id) +'_problem_count_out.json'
out_file = home + '/Documents/g' + str(grade_id) + '_problem_count_output.json.json'

schema_test_session  = ['problem_id','skill','exercise']
schema_problem_count = ['skill','democount','assistedexercisecount','numberofProblemstobeafficient']


def generateProblemCountJson():
    json_str=""
    print "problem_count_csv: ", problem_count_csv
    with open(problem_count_csv, "r") as f_obj:
        json_data=csv_reader(f_obj)


    #target=open(problem_count_out,'w')
    #target.write(json_str)
    json_str = json.dumps(json_data, indent=2, separators=(',', ': '))
    #json_str = json_data
    #print json_str

    with open(out_file, 'w+') as outfile:
        json.dump(json_str, outfile)


def csv_reader(file_obj):
    """
    Read a csv file
    """
    # with open(problem_count_out, "r") as rfile:
    #     jolddata = rfile.read()
    # jdata = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(jolddata)
    # problems = jdata
    problems = []

    reader = csv.reader(file_obj)

    section_regx = re.compile("\d{1,2}\.\d{1,2}")
    for row in reader:
        if(len(row)>0):
            #data=row[0].split('\t')
            #data=row.split(',')
            rowdata = row
            if len(rowdata)>0:
                print rowdata[1],"  ",rowdata[2]," ",rowdata[3]," ",rowdata[4]
                # obj={"problem_id": data[0],"skill":data[1],"exercise":data[2]}
                if section_regx.match(rowdata[1]):
                    skill = OrderedDict()

                    for idx, item in enumerate(schema_problem_count):
                        if idx == 0:
                            dvalue = rowdata[idx+1]
                        else:
                            dvalue = int(rowdata[idx+1])
                        skill[item] = dvalue
                    problems.append(skill)

    for p in problems:
        print p
    print problems
    print type(problems)
    return problems

if __name__ == '__main__':
    generateProblemCountJson()