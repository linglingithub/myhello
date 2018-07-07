__author__ = 'linglin'

from collections import defaultdict
from os.path import expanduser

class LogObj:
    def __init__(self):
        self.ops = []
        self.total_time = 0 # in ms

def read_log(filepath, keyword):
    log_dict = defaultdict(LogObj)
    with open(filepath, 'r') as logf:
        for line in logf:
            if keyword in line:
                words = line.split(maxsplit=4)
                op_time = int(words[4].split()[-1][:-2])
                log_dict[words[2]].ops.append((op_time, words[4]))
                log_dict[words[2]].total_time += op_time

    return log_dict

def print_stats(log_dict):
    for k, v in log_dict.items():
        print("========================")
        print(k, len(v.ops), v.total_time, " ==> every op ms: ", v.total_time / len(v.ops))
        print("========================")
        v.ops.sort()
        print(v.ops[0])
        print(v.ops[-1])

home = expanduser("~")
logfolder = "/Documents/prd_mongo_log/"
logfile = "mongod.log.2018-07-03T06-58-01"
db_keyword = "student_progress_report"
log_dict = read_log(home+logfolder+logfile, db_keyword)
print_stats(log_dict)
