import sys

n = int(raw_input())
strs = raw_input().split()
sum = 0

for num in range(0, n):
  sum += int(strs[num])

print sum
