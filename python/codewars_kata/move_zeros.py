def move_zeros(lst):
    moved_zero_arr = []
    count = 0
    for el in lst:
        if el == 0:
            count += 1
        else:
            moved_zero_arr.append(el)
    for i in range(count):
        moved_zero_arr.append(0)
    return moved_zero_arr

# print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
