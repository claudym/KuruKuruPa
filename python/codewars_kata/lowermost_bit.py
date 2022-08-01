# lowermost set bit

# clear
def clear_lowest_set_bit(num):
    return num & (num-1)

def set_lowest_unset_bit(num):
    return num | (num + 1)

def index_lowest_set_bit(num):
    index = 0
    while(not num&1):
        index += 1
        num >>= 1
    return index

def index_lowest_unset_bit(num):
    index = 0
    while(num&1):
        index += 1
        num >>= 1
    return index

number = 0b11011000
print(f'the number is {bin(number)}')
print(bin(clear_lowest_set_bit(number)))
print(bin(set_lowest_unset_bit(number)))
print(index_lowest_set_bit(number))
print(index_lowest_unset_bit(number))