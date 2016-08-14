import sys

def rotateKTimes(arrN, k):
  i = len(arrN) - k
  temp = arrN[0:i]
  arrN = arrN[i:]
  arrN[k:] = temp
  return arrN

numbers = map(int, raw_input().strip().split(' '))
n = numbers[0]
k = numbers[1]
q = numbers[2]
arr = map(int, raw_input().split(' '))
arrM = []

for i in range(0, q):
  arrM.append(int(raw_input().strip()))

if(k < n):
  arr = rotateKTimes(arr, k)
elif(k > n):
  k %= n
  arr = rotateKTimes(arr, k)

# print arr
for arr_i in arrM:
  print arr[arr_i]