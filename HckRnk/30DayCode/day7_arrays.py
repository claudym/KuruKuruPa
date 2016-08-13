import sys

arrSize = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

for i in range(0, arrSize):
  print "%d" % arr[arrSize - 1 - i],