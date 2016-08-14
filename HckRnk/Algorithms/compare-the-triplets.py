import sys

arrA = map(int, raw_input().strip().split(' '))
arrB = map(int, raw_input().strip().split(' '))
a = 0
b = 0

for i in range(0, 3):
  if(arrA[i] > arrB[i]):
    a += 1
  elif(arrA[i] < arrB[i]):
    b += 1

print "%d %d" % (a, b)
