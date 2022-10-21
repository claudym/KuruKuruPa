def list_comp(x, y, z, n):
    l_comp = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    return l_comp


if __name__ == '__main__':
    print(list_comp(1, 1, 1, 2))