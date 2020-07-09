def arrayAndLargestKElements(arr, N , k):

    #arr = sorted(arr, reverse=True)

    for i in range(N):
        for y in range(N-1):
            if arr[y]> arr[y+1]:
                arr[y],arr[y+1] = arr[y+1],arr[y]
    print(arr)


    for i in range(N-k,N):
        print(arr[i])
arr = [12,5,787,1,23]
N= 5
k = 2
arrayAndLargestKElements(arr,N,k)
