# put into a function
def to_while_and_print(maxN):
  i = 0
  numbers = []

  while i < maxN:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
  
  return numbers
    
print "The numbers: "
results = to_while_and_print(10)
for num in results:
      print num