import sys

class Difference(object):
  def __init__(self, a):
    self.__elements = a

  def computeDifference(self):
    self.maximumDifference = 0
    tempMax = 0

    for i in range(0, len(self.__elements)-1):
      for j in range(i+1, len(self.__elements)):
        tempMax = self.__elements[i] - self.__elements[j]
        if(tempMax < 0):
          tempMax = -tempMax
        if(tempMax > self.maximumDifference):
          self.maximumDifference = tempMax

_ = raw_input()
a = map(int, raw_input().strip().split(' '))
d = Difference(a)
d.computeDifference()

print d.maximumDifference