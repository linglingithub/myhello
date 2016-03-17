import csv
from json import dumps, load
from os.path import expanduser
from pprint import pprint
from collections import OrderedDict
import json

home = expanduser("~")
print home
rtf_name = home + '/Documents/106ptxt.txt'
json_name = home + '/Documents/106_p.json'
out_file =  home + '/Documents/106_p.json'
print rtf_name, json_name


json_str = ""
with open (rtf_name,'r') as rf:
    for line in rf:
        if "\xe2" in line:
            print repr(line)
        line.replace('/[\x00-\x1F\x80-\xFF]/','')
        print line
        json_str += line



print "json_str: " + json_str




#print json_str
#jdata = demjson.decode(json_str)
#jdata = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(json_str)
#print jdata
#print jdata["program_type"]
#jdata["program_type"] = "test"
#print jdata

'''

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


'''