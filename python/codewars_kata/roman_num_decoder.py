def solution(roman):
    num = 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for i in range(len(roman) - 1):
        if roman_dict[roman[i]] >= roman_dict[roman[i + 1]]:
            num += roman_dict[roman[i]]
        else:
            num -= roman_dict[roman[i]]    
    num += roman_dict[roman[len(roman) - 1]]
    return num

# print(solution('MDCLXVI'))