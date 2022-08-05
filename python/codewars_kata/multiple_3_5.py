def solution(num):
    if num < 0:
        return 0
    
    a = 3
    b = 5
    mults = [a, b, a*b]
    sums = []
    for mult in mults:
        n = (num - 1) // mult
        end = n * mult
        sums.append((mult + end) * n // 2)
    return sums[0] + sums[1] - sums[2]
