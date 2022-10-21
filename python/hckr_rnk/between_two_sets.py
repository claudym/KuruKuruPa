def getTotalX(a, b):
    between_count = 0
    for num in range(a[-1], b[0]+1, a[-1]):
        incomplete = False
        for el_a in a:
            if num % el_a != 0:
                incomplete = True
                break
        if not incomplete:
            incomplete = False
            for el_b in b:
                if el_b % num != 0:
                    incomplete = True
                    break
        if not incomplete:
            between_count += 1
    return between_count


a = [2, 4]
b = [16, 32, 96]
print(getTotalX(a, b))
