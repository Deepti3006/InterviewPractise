def threeesum(arr , total):

    for i in range(0, len(arr)):
        for j in range(i+1 , len(arr)):
            for k in range(j+1 , len(arr)):
                    if arr[i] + arr[j] + arr[k] == total :
                        print(arr[i],arr[j],arr[k])


A = [1, 4, 45, 6, 10, 8]
sum = 22
threeesum(A, 22)