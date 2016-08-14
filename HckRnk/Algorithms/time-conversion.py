import sys

hStr = raw_input().strip()
hour = int(hStr[0:2])

if(hStr[8:] == "PM"):
  if(hour != 12):
    hour += 12
else:
  if(hour == 12):
    hour = 0

pStr = ""
if(hour < 10):
  pStr += '0'
pStr += str(hour) + hStr[2:8]
print pStr