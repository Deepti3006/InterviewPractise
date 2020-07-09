def mergeTwoSortedArray(arr1,arr2):

    arr1 = arr1+arr2
    print(arr1)
    for i in range(len(arr1)):
        for j in range(len(arr1)-1):
            if arr1[j]>arr1[j+1]:
                arr1[j],arr1[j+1] = arr1[j+1],arr1[j]
    print(arr1)
arr1 = [1,3,5,7]
arr2 = [0,2,4,6,8,9]
mergeTwoSortedArray(arr1,arr2)
