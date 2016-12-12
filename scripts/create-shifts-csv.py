import pyexcel as pe
from datetime import datetime
from pytz import timezone
import time

spacer = 0

open('testing1.csv','wb')

sheet = pe.get_sheet(file_name="testing1.csv")

#Diffrent types of formats
fmt_1 = "%a %d %b %Y %H:%M"
fmt = "%a %b %d %Y %I:%M %p"
fmt2_1 = "%H:%M"
fmt2 = "%I:%M %p"
fmttime = "%d-%m-%Y %H:%M"

time = "12-12-2016 05:30"

# convert time to colstamp
stamp = float(datetime.strptime(time, fmttime).strftime("%s"))

# list of timezones
timezonelist = ['US/Pacific','EST','UTC','Europe/Berlin','Asia/Kolkata']

sheet.column += ['Shift']

for zone in timezonelist:
    sheet.column += [zone]
sheet.row += [""]

for i in range(300):
    cols = []
    cols.append(i+1)
    for zone in timezonelist:
        zonetime = datetime.fromtimestamp(stamp,timezone(zone))
        if zone in ['UTC','Europe/Berlin']:
            if spacer%6 == 0:
                cols.append(zonetime.strftime(fmt_1))
            else:
                cols.append(zonetime.strftime(fmt2_1))
        elif zone == 'Asia/Kolkata':
            if spacer%6 in [0,5]:
                cols.append(zonetime.strftime(fmt_1))
            else:
                cols.append(zonetime.strftime(fmt2_1))
        elif zone in ['US/Pacific','EST']:
            if spacer%6 in [0,2]:
                cols.append(zonetime.strftime(fmt))
            else:
                cols.append(zonetime.strftime(fmt2))
    sheet.row += cols
    stamp = stamp + 14400
    spacer = spacer + 1
    if spacer%6 == 0:
        sheet.row += [""]

sheet.save_as("Result.csv")
