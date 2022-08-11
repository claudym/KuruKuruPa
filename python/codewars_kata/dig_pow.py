def dig_pow(n, p):
    s = 0
    digits = []
    count = 0
    temp_n = n
    while temp_n > 0:
        digits.append(temp_n % 10)
        count += 1
        temp_n //= 10
    s = sum(digits[-i-1] ** (i + p) for i in range(count))
    return s // n if s % n == 0 else -1

# print(dig_pow(89, 1))
# print(dig_pow(92, 1))
# print(dig_pow(46288, 3))