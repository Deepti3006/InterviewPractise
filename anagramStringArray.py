def anagramStringArray():
    n = int(input("Enter the number of strings"))
    str_arr=[]
    for i in range(1,n+1):
        element=input("Enter the string")
        str_arr.append(element)
    print(str_arr)
    count_arr=[]
    count=0
    for i in range(0,len(str_arr)):

        for y in range(i+1, len(str_arr)):

            if sorted(str_arr[i]) == sorted(str_arr[y]):


                count_arr.append(str_arr[i])
                print(len(count_arr))

anagramStringArray()
