def numberOfPairs(arr1,arr2):
    count=0
    for i in arr1:
        for y in arr2 :
            if i**y > y**i:
                print(i,y)
                count = count+1
    print(count)
arr1 =[2,1,6]
arr2 =[1,5]
numberOfPairs(arr1,arr2)