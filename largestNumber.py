def largestNumber():
    a=[34,56,1,23]
    a.sort()
    even=[]
    odd=[]
    for i in range(len(a)):
        if a[i]%2 == 0:
            print("even")
            even.append(a[i])
        else:
            print("odd")
            odd.append(a[i])
    print(a)
    print(even)
    print(odd)
largestNumber()