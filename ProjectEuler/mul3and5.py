_author_ = 'kura'

sum = 0
max = 1000
for i in range(max):
  if not (i%3 and i%5):
    sum = sum+i
print("The sum is",sum)