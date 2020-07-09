def shortestPallindrome(string1):
    arr =[]
    for i in range(len(string1)):
        for y in range(len(string1),0,-1):
            w = string1[i:y]
            if w ==w[::-1] and len(w)>1:
                arr.append(w)

    arr.sort(key=len)
    print(arr[0])

shortestPallindrome("aaaabbaa")

