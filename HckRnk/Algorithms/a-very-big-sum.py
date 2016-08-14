#no need for bignum in python
import sys

num = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
sum = 0

for n in arr:
  sum += n
print sum