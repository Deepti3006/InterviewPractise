def numberOfTriplets(arr):

    count =0
    for i in range(len(arr)):
        for y in range(i+1,len(arr)):
            if arr[i]+arr[y] in arr:
                count=count+1
                print(arr[i],arr[y])
    if count==0:
        return -1
    else:
        return count
arr =[1,5,3,2]
count =numberOfTriplets(arr)
print(count)