import itertools
def longestDistinctCharacterInString(string1):
    for i in range(1, 4):
        seq = itertools.combinations(string1, i)
        lst = list(seq)
    print(lst)

    for i in lst:
        i = "".join(i)
        for char in i:
            if i.count(char) ==1:
                print(i)
            else:
                print(i)



longestDistinctCharacterInString("abca")
