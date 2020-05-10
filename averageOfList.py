class listAverage():

    def average(self):
        n = int(input("Enter number of elements in Array"))
        a= []
        for i in range(0,n):
            element = int(input("Enter the number in the Array"))
            a.append(element)
            avg = sum(a)/n
            print("Average of Numbers is : " + str(avg) + "Number of elements are : " + str(n) )


la = listAverage()
la.average()
