def sortArray012(arr):

    mid = 1
    low =0
    high = 2

    arr_new = []
    stack =[]
    for i in arr:
        if i =="red":
            stack.append("red")
            arr_new.append(0)
    for i in arr:
        if i == "green":
            stack.append("green")
            arr_new.append(1)
    for i in arr:
        if i == "blue":
            stack.append("blue")
            arr_new.append(2)
    print(stack)
    print(arr_new)
arr=["red","blue","green","blue","red"]
sortArray012(arr)
