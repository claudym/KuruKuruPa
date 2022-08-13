def comp(arr1, arr2):
    if arr1 is None or arr2 is None or len(arr1) != len(arr2):
        return False
    arr1_dict = {}
    arr2_dict = {}
    for i in range(len(arr1)):
        arr1_dict[arr1[i]**2] = arr1_dict.get(arr1[i]**2, 0) + 1
        arr2_dict[arr2[i]] = arr2_dict.get(arr2[i], 0) + 1
    return arr1_dict == arr2_dict


# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# print(comp(a1, a2))