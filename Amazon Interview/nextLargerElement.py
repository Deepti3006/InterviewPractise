def nextLargerElement(arr,n):

    #1. Aim : To replace the element in array with next greastest element
    # If not found then put as -1
    # sample  1 3 2 4 344-1 is the output
    print(max(arr))
    arr_new =[]
    for i in range(0,len(arr)-1):
        print(arr[i])
        if arr[i] == max(arr):
            arr.remove(arr[i])
            arr.insert(i, -1)
        elif i == len(arr)-1:
            arr.remove(arr[i])
            arr.insert(i, -1)
        elif arr[i+1] > arr[i]:

            arr.remove(arr[i+1])
            arr_new.insert(i,arr[i+1])
        elif arr[i] > arr[i+1]:

            arr.remove(arr[i])
            arr_new.insert(i, arr[i])



    print(arr)
arr =[1,3,2,4]
n=4
nextLargerElement(arr,n)



