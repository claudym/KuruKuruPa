import sys

num = int(raw_input().strip())

for i in range(1, 11):
  print "%d x %d = %d" % (num, i, num*i)