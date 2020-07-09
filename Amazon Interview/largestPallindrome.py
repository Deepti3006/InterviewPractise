def largestPallindrome(word):
    arr = []
    for i in range(len(word)):
        for j in range(len(word), 0, -1):
            w = word[i:j]
            if w == w[::-1]:
                arr.append(w)
    arr.sort(key=len)
    return (arr[-1])
p=largestPallindrome("aaaabbaa")
print(p)