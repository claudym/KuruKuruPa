import time

def binary_array_to_number(arr):
    s = 0
    for digit in arr:
        s = (s << 1) + digit
        # s = (s << 1) | digit

    return s

def binary_array_to_number2(arr):
    if len(arr) == 1:
        return arr[0]
    
    number=0
    for i in range(len(arr)-1):
        number = (number | arr[i]) << 1
    number |= arr[i+1]
    return number

if __name__ == '__main__':
    elapsed = time.process_time()
    for i in range(1000000):
        binary_array_to_number([0,0,0,1])
    elapsed = time.process_time()-elapsed
    print(bin(binary_array_to_number([0,0,0,1])))
    print('elapsed time:', elapsed)
    print(binary_array_to_number([0,0,1,0]))
    print(binary_array_to_number([1,1,1,1]))
    print(binary_array_to_number([0,1,1,0]))
    print(binary_array_to_number([0]))
    print(binary_array_to_number([1]))
