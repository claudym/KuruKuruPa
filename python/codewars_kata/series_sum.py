def series_sum(n):
    if not n:
        return '0.00'
    s=1
    for i in range(1, n):
        den = i*3 + 1
        s += 1/den
    return f'{s:.2f}'


if __name__ == '__main__':
    print(series_sum(3))
