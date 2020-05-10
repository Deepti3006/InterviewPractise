class large():

    def largestInArray(self):
        n = int(input("The number of elements in array"))
        a=[]
        for i in range(0,n):
            element = int(input("Enter the element in array"))
            a.append(element)
        print(a)
        a.sort()
        print(a)
        print("The largest number in array is :" + str(a[n-1]))
l =large()
l.largestInArray()
