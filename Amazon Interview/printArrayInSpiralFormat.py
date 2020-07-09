def printArrayInSpiralArray():
    arr =[[1,2,3,4],
          [7,8,9,5],
          [13,14,15,16]]
    max_r = 3
    max_c =4
    c=0
    r=0
    arr_spiral =[]
    for i in range(r,1):
        for y in range(c,max_c):
         arr_spiral.append(arr[i][y])
    for i in range(r, max_r):
        if arr[i][max_c-1] not in arr_spiral:
            arr_spiral.append(arr[i][max_c-1])
    for i in range(c,max_c):
        if arr[max_r-1][i] not in arr_spiral:
            arr_spiral.append(arr[max_r-1][i])
    for i in range(r,max_r):
        for y in range(c,max_c):
            if arr[i][y] not in arr_spiral:
                print(arr[i][y])
                arr_spiral.append(arr[i][y])
    print(arr_spiral)


printArrayInSpiralArray()