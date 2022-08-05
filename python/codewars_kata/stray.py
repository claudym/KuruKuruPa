def stray2(arr):
    # another version faster for when the stray number is closer to the beggining:
    # O(kn), where k is the number of keys, but can be considered O(2n) = O(n)
    dct = {}
    for el in arr:
        dct[el] = dct.get(el, 0) + 1
        if len(dct) > 1:
            for k in dct:
                print(dct[k], dct[el])
                if dct[k] > dct[el]:
                    return el
                elif dct[k] < dct[el]:
                    return k

def stray(arr):
    # O(n + k), where k is the number of keys, since k=2, is then O(n+2)= O(n) 
    dct = {}
    for el in arr:
        if dct.get(el) is None:
            dct[el] = 1
        else:
            dct[el] += 1
    for k in dct:
        if dct[k] == 1:
            return k

if __name__ == '__main__':
    print(stray2([1, 1, 1, 1, 1, 2]))