def moveZeroToRightHandSide(arr):

    # Only append non zero number by looping iusing for
    # comparing with lenght of the array and
    # diiferent which is there i will pushong tp the array
    arr_change =[]
    for i in range(len(arr)):
        if arr[i] != 0:
            arr_change.append(arr[i])
    print(arr_change)

    len_ori_arr = len(arr)
    len_new_arr = len(arr_change)
    diff = len_ori_arr- len_new_arr
    for i in range(len(arr),len(arr)+diff):
        arr_change.append(0)
    print(arr_change)

arr =[1, 2, 0, 4, 3, 0, 5, 0]
moveZeroToRightHandSide(arr)


