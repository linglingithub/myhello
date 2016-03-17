import csv
from json import dumps, load
from os.path import expanduser
from pprint import pprint
from collections import OrderedDict
import demjson
import json

home = expanduser("~")
print home
csv_name = home + '/Documents/g3.csv'
json_name = home + '/Documents/math_grade.json'
out_file =  home + '/Documents/out.json'
print csv_name, json_name


json_str = ""
with open (json_name,'r') as jf:
    json_str = jf.read()
    #print json_str

#print json_str
#jdata = demjson.decode(json_str)
jdata = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(json_str)
print jdata
#print jdata["program_type"]
#jdata["program_type"] = "test"
#print jdata



with open (csv_name,'r') as cf:
    f_csv = csv.reader(cf)
    headers = next(f_csv)
    for row in f_csv:
        #print row[0], row[3], row[4]
        for chp in jdata["chapters"]:
            for ski in chp["skills"]:
                if ski["section"] == row[0]:
                    ski["weight"] = row[3]
                    ski["specified_time"] = row[4]
                    #print ski


print jdata
#jstr = demjson.encode( jdata )

jstr = json.dumps(jdata, indent=2, separators=(',', ': '))

print jstr


with open (out_file, 'w+') as of:
    of.write(jstr)
    #json.dumps(jstr, of)
    #json.dump(jstr, of, indent=4)


