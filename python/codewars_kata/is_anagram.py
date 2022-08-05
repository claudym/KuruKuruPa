def is_anagram(test, original):
    # commented lines achieve same result as next line after
    
    test_d = {}
    original_d = {}
    for ch in original.lower():
        original_d[ch] = original_d.get(ch, 0) + 1
    for ch in test.lower():
        # if test_d.get(ch) is None:
        #     test_d[ch] = 1
        # else:
        #     test_d[ch] += 1
        test_d[ch] = test_d.get(ch, 0) + 1
    # if len(original_d) != len(test_d):
    #     return False
    # for k in original_d:
    #     if original_d[k] != test_d.get(k):
    #         return False
    # return True
    return test_d == original_d