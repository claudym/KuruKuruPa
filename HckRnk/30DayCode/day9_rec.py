import sys

def factorial(n):
  if(n <= 1): #base case
    return 1
  else:       #recursive case
    return n * factorial(n-1)

num = int(raw_input().strip())
print "%d" % factorial(num)