import sys

num = int(raw_input().strip())
arr = map(int, raw_input().strip().split())
positive = 0
negative = 0
zeroes = 0

for arr_i in arr:
  if(arr_i < 0):
    negative += 1
  elif(arr_i > 0):
    positive += 1
  else:
    zeroes += 1

print "%f" %(float(positive)/num)
print "%f" %(float(negative)/num)
print "%f" %(float(zeroes)/num)