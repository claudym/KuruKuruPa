def reverse_number(n):
    if n < 0:
        return -int(''.join(reversed(str(n)[1:])))
    return int(''.join(reversed(str(n))))
