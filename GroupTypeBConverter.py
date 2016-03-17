__author__ = 'linglin'

from os.path import expanduser
from collections import OrderedDict
import json
import re

class GroupTypeBConverter(object):

    def __init__(self, itemPG):
        home = expanduser("~")
        self.problem_name = home + "/Documents/skill_problem.json"
        self.problem_out = home + "/Documents/skill_problem_out.json"
        self.problem_data = {}
        self.itemsPerGroup = itemPG

    def get_problem_data(self):
        problem_str = ""
        with open(self.problem_name, 'r') as pf:
            problem_str = pf.read()
        problem_data = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(problem_str)
        #print problem_data
        self.problem_data=problem_data
        return problem_data

    def write_problem_out(self):
        problem_out_str = json.dumps(self.problem_data, indent=2, separators=(',', ': '))
        print problem_out_str
        with open(self.problem_out, 'w+') as of:
            of.write(problem_out_str)


    def convert_problem_group(self):
        items_per_group = self.itemsPerGroup
        for problem in self.problem_data:
            problem["template_type"] = "group_b_multiple_input"
            problem["group_answer"] = [0,0,0,0]
            if "problemItems" in problem:
                i = 0
                problemgroup = OrderedDict()
                problemgroup["mathJaxText"] = ""
                problemgroup["problemItems"] = []
                problem["problems"] = []
                for pitem in problem["problemItems"]:
                    if "mathJaxText" in pitem and "answer" not in pitem:
                        problemgroup["mathJaxText"] = pitem["mathJaxText"]
                        if "text" in pitem:
                            problemgroup["text"] = pitem["text"]
                    else:
                        i += 1
                        problemgroup["problemItems"].append(pitem)
                        if i == items_per_group:
                            if problemgroup["mathJaxText"] == "":
                                del problemgroup["mathJaxText"]
                            problem["problems"].append(problemgroup)
                            i = 0
                            problemgroup = OrderedDict()
                            problemgroup["mathJaxText"] = ""
                            problemgroup["problemItems"] = []

            problem["problemItems"] = []
            del problem["problemItems"]


    @staticmethod
    def process_convert():
        gtbc = GroupTypeBConverter(2)
        gtbc.get_problem_data()
        gtbc.convert_problem_group()
        gtbc.write_problem_out()

if __name__ == '__main__':
    GroupTypeBConverter.process_convert()