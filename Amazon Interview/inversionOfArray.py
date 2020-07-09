def inversionOfArray(arr):
    count =0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j] and i<j:
                count =count+1
    print(arr)
    print(count)

arr =[2,4,1,3,5]
inversionOfArray(arr)