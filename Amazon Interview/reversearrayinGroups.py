def reverseArrayInGroups(arr,n):

    number_of_sets = len(arr)//n
    print(number_of_sets)
    arr_new=arr[0:2]
    arr_new = arr_new[::-1]
    while len(arr)> len(arr_new):
        arr_new_1= arr[3:len(arr)]
        arr_new_1 = arr_new_1[::-1]
        arr_new = arr_new+arr_new_1

    print(arr_new)

arr =[1,2,3,4,5]
n=3
reverseArrayInGroups(arr,3)