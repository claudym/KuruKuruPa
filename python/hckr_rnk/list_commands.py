def list_commands(lst, command):
    tokens = command.split()
    if tokens[0] == 'insert':
        lst.insert(tokens[1], tokens[2])
    elif tokens[0] == 'print':
        print(lst)
    elif tokens[0] == 'remove':
        lst.remove(tokens[1])
    elif tokens[0] == 'append':
        lst.append(tokens[1])
    elif tokens[0] == 'sort':
        lst.sort()
    elif tokens[0] == 'pop':
        lst.pop()
    else:
        lst.reverse()


