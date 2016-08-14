import sys

num = int(raw_input().strip())
for i in range(0, num):
  print "%s%s" %(" "*(num-1-i), "#"*(i+1))