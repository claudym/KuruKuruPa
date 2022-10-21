from itertools import islice


def second_lowest(arr):
    sorted_arr = sorted(arr, key= lambda x : (x[1], x[0]))
    lowest = sorted_arr[0]
    second_lowest = lowest
    second_lowest_arr = []
    # for i in range(1, len(arr)):
    for el in islice(sorted_arr, 1, None):
        print(el)
        if lowest[1] == second_lowest[1]:
            if el[1] > lowest[1]:
                second_lowest = el
                second_lowest_arr.append(el)
        elif el[1] == second_lowest[1]:
            second_lowest_arr.append(el)
        else:
            break
    return second_lowest_arr

def print_second_lowest(arr):
    for el in arr:
        print(el[0])


if __name__ == "__main__":
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    print_second_lowest(second_lowest(students))