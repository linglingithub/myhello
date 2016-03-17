__author__ = 'linglin'
"""
Generate the hint image references for hints.json,
according to skill_problem.json as where is
the start & end of hint-img-index of one problem.
"""

from os.path import expanduser
from collections import OrderedDict
import json


home = expanduser("~")
hints_name = home + '/Documents/hints.json'
problem_name = home + "/Documents/skill_problem.json"
out_file = home + '/Documents/hints_out.json'

hints_str = ""
with open(hints_name, 'r') as hf:
    hints_str = hf.read()
hints_data = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(hints_str)
print hints_data

problem_str = ""
with open(problem_name, 'r') as pf:
    problem_str = pf.read()
problem_data = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(problem_str)
print problem_data

hintimgs = []
hintimgs.append("../../../theme/sea/hint-img-fish-left.png")
hintimgs.append("../../../theme/sea/hint-img-dolphin-left.png")
hintimgs.append("../../../theme/sea/hint-img-whate-left.png")
hintimgs.append("../../../theme/sea/hint-img-crab-left.png")
hintimgs.append("../../../theme/sea/hint-img-seahorse-left.png")
hintimgs.append("../../../theme/sea/hint-img-octopus-left.png")

#hintNumPattern=[]
# for all problems that have 4 hints
#hintNumPattern = [4]
# for all problems that have 4, 5, 4, 5 ,... hints
#hintNumPattern = [4,5]
# special hint number
#hintNumPattern = [5,5,4,5,5,4,5,4,4,4]

for problem in problem_data:
    # print problem
    hintIds = problem["hintIds"]
    print hintIds
    hintImgIndex = 0
    for hintId in hintIds:
        hintIndex = int(hintId) - 1
        print hints_data[hintIndex]
        hints_data[hintIndex]["hinticon"] = hintimgs[hintImgIndex % len(hintimgs)]
        print hints_data[hintIndex]
        hintImgIndex += 1

hints_out_str = json.dumps(hints_data, indent=2, separators=(',', ': '))

print hints_out_str

with open(out_file, 'w+') as of:
    of.write(hints_out_str)



