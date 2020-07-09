def numberOfFibbonacciNumbersInArray(arr,n):

    arr_fibbo =[]

    first =0
    second=1
    next =0
    arr_fibbo.append(first)
    arr_fibbo.append(second)
    for i in range(2,n):
        next= first+second
        arr_fibbo.append(next)
        first= second
        second= next

    intersection_1 = set(arr_fibbo).intersection(arr)

    for i in intersection_1:
        print(i)


arr =[0,2,8,5,2,1,4,13,23]


numberOfFibbonacciNumbersInArray(arr,10)
