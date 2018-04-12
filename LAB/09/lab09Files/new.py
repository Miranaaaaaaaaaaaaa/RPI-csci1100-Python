from Date import *
import sys

month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

earliest = Date(3000,1,1)
latest = Date(100,1,1)
count = [0,0,0,0,0,0,0,0,0,0,0,0,0]
for item in date:
    count[item.m] += 1
    if item<earliest:
        earliest = item
    if latest< item:
        latest = item
    
month2 = month_names[count.index(max(count))]
print("earliest " + str(earliest))
print("lastest: " + str(latest))
print(month2)