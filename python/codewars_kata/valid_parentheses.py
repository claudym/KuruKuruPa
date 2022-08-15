def valid_parentheses(string):
    if len(string) == 0:
        return True
    if string[0] == ')':
        return False
    count = 0
    for char in string:
        if char == '(':
            count += 1
            print(count)
        elif char == ')' and count > 0:
            count -= 1
            print(count)
        elif char == ')' and count == 0:
            return False
    return True if count == 0 else False 

print(valid_parentheses('(rfhqpyzagixynoavz(grrpwtigroz))x)b(nl)hp'))