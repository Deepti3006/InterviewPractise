def addAndMergeArray(arr1,arr2):

    # Arr 2 should be added to arr 1 elements of a[0] ,a[i] and a[2]
    # sort the arr1  with built in
    print(arr1)
    print(arr2)
    for i in range(len(arr2)):
        if arr1[i] == None:
            arr1.remove(arr1[i])
            arr1.insert(i,arr2[i])
    print(arr1)
    print(sorted(arr1))
arr1 = [None,None,None,9,8,7,4]
arr2 = [1,2,6]
addAndMergeArray(arr1,arr2)