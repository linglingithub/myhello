__author__ = 'linglin'

from os.path import expanduser
from collections import OrderedDict
import json
import re

class GroupTypeAConverter(object):

    def __init__(self):
        home = expanduser("~")
        self.problem_name = home + "/Documents/skill_problem.json"
        self.problem_out = home + "/Documents/skill_problem_out.json"
        self.problem_data = {}

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
        items_per_group = 2
        for problem in self.problem_data:
            problem["template_type"] = "group_type_a"
            problem["group_answer"] = [0,0,0,0]
            if "problemItems" in problem:
                i = 0
                problemgroup = OrderedDict()
                problemgroup["problemItems"] = []
                problem["problems"] = []
                for pitem in problem["problemItems"]:
                    i += 1
                    problemgroup["problemItems"].append(pitem)
                    if i == items_per_group:
                        problem["problems"].append(problemgroup)
                        i = 0
                        problemgroup = OrderedDict()
                        problemgroup["problemItems"] = []

            problem["problemItems"] = []
            del problem["problemItems"]
            #
            # for i in xrange(len(problem)):
            #     if "problemItems" in problem[i]:
            #         problem.pop(i)
            #         break

    @staticmethod
    def process_convert():
        gtac = GroupTypeAConverter()
        gtac.get_problem_data()
        gtac.convert_problem_group()
        gtac.write_problem_out()

if __name__ == '__main__':
    GroupTypeAConverter.process_convert()