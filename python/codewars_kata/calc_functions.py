def zero(op=''):
    return eval(f'0{op}')
def one(op=''):
    return eval(f'1{op}')
def two(op=''):
    return eval(f'2{op}')
def three(op=''):
    return eval(f'3{op}')
def four(op=''):
    return eval(f'4{op}')
def five(op=''):
    return eval(f'5{op}')
def six(op=''):
    return eval(f'6{op}')
def seven(op=''):
    return eval(f'7{op}')
def eight(op=''):
    return eval(f'8{op}')
def nine(op=''):
    return eval(f'9{op}')


def plus(num):
    return f'+{num}'
def minus(num):
    return f'-{num}'
def times(num):
    return f'*{num}'
def divided_by(num):
    return f'//{num}'

print(seven(times(five()))) # must return 35
print(four(plus(nine()))) # must return 13
print(eight(minus(three()))) # must return 5
print(six(divided_by(two()))) # must return 3