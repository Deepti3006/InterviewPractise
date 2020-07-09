def trappingRainWater(arr):

    sum1 =0
    for y in range(len(arr)):
        if arr[0] > arr[y]:
            print(arr[y])
            sum1 =sum1+(arr[0] - arr[y])
            print(sum1)
    print(sum1)

arr =[6,9,9]
trappingRainWater(arr)