def sort_012(arr):

    low =0
    mid = 1
    for i in range(len(arr)):
        if arr[i+1] == "0":
            arr[i+1],arr[i] = arr[i],arr[i+1]
    print(arr)

arr =[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort_012(arr)