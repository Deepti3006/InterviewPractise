def rotateCompleteArray():

    arr_1 = [1,2,3,4,5,6]
    arr_2=[]
    arr_2.append(arr_1[0])
    arr_2.append(arr_1[1])
    del arr_1[0]
    del arr_1[1]

    arr_1.extend(arr_2)
    print(arr_1)
rotateCompleteArray()