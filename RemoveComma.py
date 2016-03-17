__author__ = 'linglin'


from os.path import expanduser
from collections import OrderedDict
import json
import re

class RemoveComma(object):

    def process(self):
        home = expanduser("~")
        in_file = home + "/Documents/skill_problem.json"
        out_file = home + "/Documents/skill_problem_out.json"
        problem_str = ""
        with open(in_file, 'r') as inf:
            problem_str = inf.read()
        problem_data = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(problem_str)
        for problem in problem_data:
            for problemItem in problem["problemItems"]:
                answer = problemItem["answer"]
                print answer
                print type(answer)
                if isinstance(answer,unicode):
                    re_comma = re.compile("[0-9]+\,[0-9]+")
                    match = re_comma.search(answer)
                    if match:
                        print answer
                        new_ans = answer.replace(",", "")
                        print new_ans
                        print type(new_ans)
                        problemItem["answer"] = int(new_ans)
        problem_out_str = json.dumps(problem_data, indent=2, separators=(',', ': '))
        #print problem_out_str
        with open(out_file, 'w+') as of:
            of.write(problem_out_str)


if __name__ == '__main__':
    removeComma = RemoveComma()
    removeComma.process()