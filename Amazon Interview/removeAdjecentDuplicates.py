def removeAdjecentDuplicates(word):
    stack =[]
    for i in word:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)


    seq = "".join(stack)
    print(seq)


removeAdjecentDuplicates("acaaabbbacdddd")