import sys

phoneDir = {}
phoneDirSize  = int(raw_input().strip())

for i in range(0, phoneDirSize):
  tempStr = raw_input().strip().split(' ')
  phoneDir[tempStr[0]] = int(tempStr[1])

keys = []

while(True):
  key = sys.stdin.readline()
  if key == '':
    break
  keys.append(key.strip())


for key in keys:
  if key in phoneDir:
    print "%s=%d" % (key, phoneDir[key])
  else:
    print "Not found"