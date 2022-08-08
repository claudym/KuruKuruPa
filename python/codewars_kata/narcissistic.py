def narcissistic(num):
    numArr = []
    digits = 0
    temp_num = num
    while(temp_num > 0):
        numArr.append(temp_num % 10)
        temp_num = temp_num // 10
        digits += 1
    return sum(x ** digits for x in numArr) == num