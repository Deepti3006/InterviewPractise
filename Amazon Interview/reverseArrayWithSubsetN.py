def reverseArrayWithSubsetN(arr):
    subset =[]
    l= len(arr)
    print(arr)
    for i in range(l-3,l):
        subset.append(arr[i])
    for i in subset:
        arr.remove(i)
    print(arr+ subset[::-1])


arr = [1,3,5,7,9,11,15,17,19]

reverseArrayWithSubsetN(arr)
