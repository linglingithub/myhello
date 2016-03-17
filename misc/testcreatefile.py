__author__ = 'linglin'


import os
import csv
from os.path import expanduser
from collections import OrderedDict
import json
import re


home = expanduser("~")


csv_name = home + '/Documents/gttttt.log'
if not os.path.exists(csv_name):
    open(csv_name, 'w').close()
else:
    print csv_name, " already exist!"