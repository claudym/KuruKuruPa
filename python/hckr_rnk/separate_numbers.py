def separateNumbers(s):
    for delta in range(1, len(s) // 2 + 1):
        first_num = int(s[:delta])
        num = first_num
        next_num = num + 1
        i = delta
        while(i < len(s)):
            len_next_num = len(str(next_num))
            next_num_str = int(s[i:i+len_next_num])
            if num + 1 != next_num_str:
                break
            i += len_next_num
            num = next_num
            next_num = num + 1
        if i >= len(s):
            print("YES", first_num)
            return
    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
    # separateNumbers("1234")
    # separateNumbers("91011")
    # separateNumbers("99100")
    # separateNumbers("101103")
    # separateNumbers("010203")
    # separateNumbers("13")
    # separateNumbers("1")