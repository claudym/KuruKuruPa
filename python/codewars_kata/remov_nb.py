# The function takes the parameter: n (n is always strictly greater than 0) and 
# returns an array or a string (depending on the language) of the form:

# [(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]

# with all (a, b) which are the possible removed numbers in the sequence 1 to n.
def remov_nb(n):
    arr_truth = []
    cache = {}
    s = ((1 + n) * n) // 2
    for a in range(1, n + 1):
        if a in cache:
            arr_truth.append((a, cache[a]))
        else:
            if (s - a) % (a + 1) == 0:
                b = (s - a) // (a + 1)
                if b <= n:
                    arr_truth.append((a, b))
                    cache[b] = a
    return arr_truth

# print(remov_nb(26))