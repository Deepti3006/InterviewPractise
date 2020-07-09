def maxContagiousSubarray(arr):
    current_sum= arr[0]
    max_sum=arr[0]
    for i in range(1,len(arr)):
        current_sum = max(arr[i], current_sum+arr[i])
        max_sum = max(max_sum,current_sum)
    print(max_sum)

arr =[-1,-2,-3,-4]
maxContagiousSubarray(arr)
