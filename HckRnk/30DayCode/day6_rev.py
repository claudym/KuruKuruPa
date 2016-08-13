import sys

num = int(raw_input().strip())
indStrs = []

for i in range(0, num):
  indStrs.append(raw_input())

for st in indStrs:
  tempStr1 = ""
  tempStr2 = ""
  for i in range(0, len(st)):
    if(i%2 == 0):
      tempStr1 += st[i]
    else:
      tempStr2 += st[i]
  print "%s %s" % (tempStr1, tempStr2)