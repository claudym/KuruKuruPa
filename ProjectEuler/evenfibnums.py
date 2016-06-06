__author__ = "Kura"

max = 4000000
prev = 1
fib = 1
eSum = 0

while fib < max:
  temp = fib
  fib = fib + prev
  prev = temp

  if not fib%2:
    eSum = eSum + fib

print("sum:", eSum)