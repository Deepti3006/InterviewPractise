def leaderOfArray(arr):

    for i in range(len(arr)):
        for y in range(i+1,len(arr)):
            if arr[i] <= arr[y]:
                break
        if y == len(arr) - 1:  # If loop didn't break
            print(arr[i],)

arr = [16,17,4,3,5,2]
leaderOfArray(arr)