def pythogoreonTriplet(arr):

    number_of_triplets = len(arr)//3
    sum1 = 1
    sum_arr = []
    for i in range(len(arr)):
        for y in range(i+1,len(arr)):
            for k in range(y+1,len(arr)):
                sq_arr_i = arr[i]**2
                sq_arr_y = arr[y]**2
                sq_arr_k = arr[k]**2
                if sq_arr_i+sq_arr_y == sq_arr_k:
                    print(arr[i],arr[y],arr[k])



arr =[3,2,4,6,5]
pythogoreonTriplet(arr)

