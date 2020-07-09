def maximumSubarrayAgain(arr):

    current_max = arr[0]
    max_subaary = arr[0]
    for i in range(1,len(arr)):
        current_max = max(arr[i],current_max+arr[i])
        max_subaary =max(max_subaary,current_max)
    print(max_subaary)
arr = [3,4,-2,3,-10,32,4,-11,7,-3,2]
maximumSubarrayAgain(arr)