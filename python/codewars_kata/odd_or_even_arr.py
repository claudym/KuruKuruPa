def odd_or_even(arr):
    odd = 0
    for el in arr:
        odd ^= el & 1
    if odd:
        return 'odd'
    return 'even'


if __name__ == '__main__':
    print(odd_or_even([1023, 1, 2]))
