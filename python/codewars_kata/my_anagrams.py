def anagrams(word, words):
    arr = []
    word_dict = {}
    for char in word:
        word_dict[char] = word_dict.get(char, 0) + 1
    for w in words:
        words_dict = {}
        for char in w:
            words_dict[char] = words_dict.get(char, 0) + 1
        if word_dict == words_dict:
            arr.append(w)
    return arr
