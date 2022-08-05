def sequence_sum(begin_number, end_number, step):
    n = (end_number - begin_number) // step
    if n < 0:
        return 0
    ending = step*n+begin_number
    return (begin_number + ending) * (n+1) // 2

# print(sequence_sum(-960, -5894842, 3))
# print(sequence_sum(-2, 4, 658))