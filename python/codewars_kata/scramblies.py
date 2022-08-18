def scramble(s1, s2):
    s2_dict = {}
    for ch in s2:
        s2_dict[ch] = s2_dict.get(ch, 0) + 1
    for ch in s1:
        s2_dict[ch] = s2_dict.get(ch, 0) - 1
    for k in s2_dict:
        if s2_dict[k] > 0:
            return False
    return True

# print(scramble('rkqodlw', 'world'))
# print(scramble('katas', 'steak'))