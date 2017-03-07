__author__ = 'linglin'

import csv
from os.path import expanduser
from collections import OrderedDict
import json

HOME = expanduser("~")

grade_id = 9
# csv_name = HOME + '/Downloads/g' + str(grade_id) + '.csv'
#csv_name = HOME + '/Downloads/Copy of Afficient Academy K-8 Outline - Grade ' + str(grade_id) + ' Official.csv'
# csv_name = HOME + '/Downloads/Copy of Afficient Academy 9-12 Outline - Geometry Official.csv'
csv_name = HOME + '/Downloads/Dupe for contest Afficient Academy 9-12 Outline - Algebra 1 Official (4).csv'
csv_weight_name = HOME + '/Downloads/g' + str(grade_id) + '_weights.csv'
json_name = HOME + '/Documents/math_grade.json'
out_file = HOME + '/Documents/g' + str(grade_id) + '.json'

print csv_name, json_name

# for grades higher than 9, comment this out
# skill_weight = {}
# with open(csv_weight_name,'r') as weightf:
#     weight_csv = csv.reader(weightf)
#     headers = next(weight_csv)
#     print headers
#
#     reDigitStart = re.compile("[0-9]+.[0-9]+ [a-zA-Z ]+")
#     for row in weight_csv:
#         print row[3], row[10]
#         mpre = reDigitStart.search(row[3])
#         if mpre:
#             #print mpre.group()
#             skill_arr = row[3].split()
#             #print skill_arr
#             skill_section = skill_arr[0]
#             if row[10].strip() == 'y' or row[10].strip() == 'n':
#                 skill_weight[skill_section] = row[10].strip()
#     print skill_weight


json_str = ""
with open(json_name, 'r') as jf:
    json_str = jf.read()
    # print json_str

# print json_str
# jdata = demjson.decode(json_str)
jdata = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(json_str)

jdata["level"] = "Grade " + str(grade_id)
jdata["grade_id"] = str(grade_id)
# print jdata

skill_id = 0

with open(csv_name, 'r') as cf:
    f_csv = csv.reader(cf)
    headers = next(f_csv)
    print headers

    for row in f_csv:
        print row[0], row[1], row[2], row[3], row[4], row[6], row[7], row[8], row[9]
        if row[1].startswith("Chapter "):
            chapter_id = row[1][len("Chapter ") - 1:row[1].index(":")].strip()
            chapter_name = row[1][row[1].index(":") + 1:].strip()
            print chapter_id, chapter_name
            chapter_new = OrderedDict()
            chapter_new["chapter_id"] = int(chapter_id)
            chapter_new["chapter_name"] = chapter_name
            chapter_new["skills"] = []
            jdata["chapters"].append(chapter_new)
        elif row[0].strip() != "":
            skill_new = OrderedDict()

            skill_id += 1
            section = row[0].strip()
            skill_name = row[1].strip()
            icon_url = "content/g" + str(grade_id) + "_c" + str(chapter_id) + "_s" + str(
                section.replace(".", "_")) + ".png"
            specified_time = row[4].strip()
            weight = row[3].strip()
            if weight is None or weight == "":
                weight = "0"

            total_time_for_learning = row[6].strip()
            score_of_learning = row[7].strip()
            time_for_advance_one_level_in_proficiency = row[8].strip()
            score_of_advance_one_level_in_proficiency = row[9].strip()

            # common_core_map = row[2].strip() #-- for g2 only

            skill_new["skill_id"] = skill_id
            skill_new["section"] = section
            skill_new["skill_name"] = skill_name
            skill_new["icon_url"] = icon_url
            skill_new["image_name"] = icon_url
            skill_new["status"] = "To Be Learned"
            skill_new["specified_time"] = specified_time
            skill_new["weight"] = weight
            skill_new["democount"] = 0
            skill_new["assistedexercisecount"] = 0
            if grade_id > 2 and grade_id <= 6 and section in skill_weight:
                if skill_weight[section] == 'y':
                    skill_new["testskill"] = True
                else:
                    skill_new["testskill"] = False
            else:
                if grade_id == 2 or grade_id >= 7:
                    if weight == "0":
                        skill_new["testskill"] = False
                    else:
                        skill_new["testskill"] = True
                else:
                    skill_new["testskill"] = False

            skill_new["total_time_for_learning"] = total_time_for_learning
            skill_new["score_of_learning"] = score_of_learning
            skill_new["time_for_advance_one_level_in_proficiency"] = time_for_advance_one_level_in_proficiency
            skill_new["score_of_advance_one_level_in_proficiency"] = score_of_advance_one_level_in_proficiency

            '''
            skill_new["common_core_map"] = common_core_map
            '''

            jdata["chapters"][-1]["skills"].append(skill_new)



            # for chp in jdata["chapters"]:
            #     for ski in chp["skills"]:
            #         if ski["section"] == row[0]:
            #             ski["weight"] = row[3]
            #             ski["specified_time"] = row[4]
            #             # print ski

print jdata
# jstr = demjson.encode( jdata )

jstr = json.dumps(jdata, indent=2, separators=(',', ': '))

print jstr

with open(out_file, 'w+') as of:
    of.write(jstr)
    # jrowdatason.dumps(jstr, of)
    # json.dump(jstr, of, indent=4)
