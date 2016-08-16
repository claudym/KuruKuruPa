import sys

maxOnes = 0
tempOnes = 0
num = int(raw_input().strip())

while(num > 0):
  if(num%2):
    tempOnes += 1
    if(tempOnes > maxOnes):
      maxOnes = tempOnes
  else:
    tempOnes = 0

  num /= 2;
print maxOnes