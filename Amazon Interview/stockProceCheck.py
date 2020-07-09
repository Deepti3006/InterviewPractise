def stockPriceCheck(arr,n):

    # If stock price is less than previous dayyyyy then value is always 1
    # if stock price is grater than previous day then value is in mulriples of 2
    # first element is fixed to one
    # We will take the array which is given
    # Comparing each other with adjecent value using bubble sort
    # then based on the coparison will append value to array
    # finally print the array.
    #100 80 60 70 60 75 85  1 1 1 2 1 4 6
    arr_number =[]
    high_value=1
    low_value =2
    for y in range(len(arr) -1):
            if arr[y] > arr[y+1]:
                arr_number.append(1)
            elif low_value not in arr_number:
                arr_number.append(low_value)
                print(low_value)
                low_value =low_value+2
                print(low_value)
    print(arr_number)

arr =[10,4,5,90,120,80]
n = 6

stockPriceCheck(arr,n)



