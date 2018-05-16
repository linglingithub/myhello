

# from datetime import *
# from dateutil.tz import *
from datetime import datetime, timezone
ts = datetime.now()
import dateutil.parser

print(ts)
print(ts.isoformat())


timestr = "2018-04-24T16:39:16+07:00"
timestr1 = "2018-04-24T16:39:16-07:00"

yourdate = dateutil.parser.parse(timestr)
print(yourdate, yourdate.year, yourdate.date(), yourdate.hour, yourdate.minute, yourdate.second)
print(yourdate.tzinfo)
print(yourdate.tzname())

#print(timezone.utcoffset())

print(datetime.utcnow().isoformat())
print(datetime.now().isoformat())

print(dir(timezone))