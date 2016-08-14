import sys

num = int(raw_input().strip())
arr = []

for i in range(0, num):
  arr_i = map(int, raw_input().strip().split(' '))
  arr.append(arr_i)

d1 = 0
d2 = 0
# for i in range(0, num):
#   for j in range(0, num):
#     if(i == j):
#       d1 += arr[i][j]
#     if(j == num - 1 - i):
#       d2 += arr[i][j]

i = 0
for arr_i in arr:
  d1 += arr_i[i]
  d2 += arr_i[num-1-i]
  i += 1

d1 = d1-d2
if(d1 < 0):
  print -d1
else:
  print d1
