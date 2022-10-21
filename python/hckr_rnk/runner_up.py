def runner_up(arr):
    sorted_arr = sorted(arr, reverse=True)
    best = sorted_arr[0]
    # for i in range(len(arr)):
    for val in sorted_arr:
        if val < best:
            return val
    return best

if __name__ == '__main__':
    arr = [2, 3, 6, 6, 5]
    print(runner_up(arr))
