__author__ = 'linglin'

from collections import defaultdict
from os.path import expanduser, isfile, join
from os import listdir
from os.path import isfile, join


class LogObj:
    def __init__(self):
        self.ops = []
        self.total_time = 0  # in ms


def read_log(filepath, keyword):
    with open(filepath, 'r') as logf:
        for line in logf:
            if keyword in line:
                try:
                    words = line.split(maxsplit=4)
                    op_time = int(words[4].split()[-1][:-2])
                    log_dict[words[2]].ops.append((op_time, words[4]))
                    log_dict[words[2]].total_time += op_time
                except Exception as e:
                    print("Exception ==== ", e)
    return log_dict


def print_stats(log_dict):
    for k, v in log_dict.items():
        print("========================================================================")
        print(k, len(v.ops), v.total_time, " ==> every op ms: ", v.total_time / len(v.ops))
        print("========================================================================")
        v.ops.sort()
        print(v.ops[0])
        print(v.ops[-1])


db_keyword = "student_progress_report"
db_keyword2 = "notification_tracker"
db_keyword3 = "user_assignment"
home = expanduser("~")
log_folder = join(home, "Documents/prd_mongo_log/")
print(log_folder)
log_dict = defaultdict(LogObj)
log_files = [join(log_folder, f) for f in listdir(log_folder) if isfile(join(log_folder, f))]
for logfile in log_files:
    #logfile = "mongod.log.2018-07-03T06-58-01"
    print(logfile)
    log_dict = read_log(logfile, db_keyword)
print_stats(log_dict)
