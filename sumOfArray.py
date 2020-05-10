def sumOfArray():

    n = int(input("Enter the number"))
    a=[]
    for i in range(n):
        ele = int(input("Enter the element"))
        a.append(ele)
    sum=0
    for i in range(len(a)):
        sum=sum+a[i]
    print(sum)
sumOfArray()
