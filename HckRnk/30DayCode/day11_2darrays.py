import sys
from sys import maxint

maxSum = -maxint
sum = 0
arr = []
for i in range(0, 6):
  arr.append(map(int, raw_input().strip().split(' ')))

for i in range(0, 4):
  for j in range(0, 4):
    sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
    if(sum > maxSum):
      maxSum = sum
print maxSum