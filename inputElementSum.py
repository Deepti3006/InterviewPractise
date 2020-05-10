class inputElementSum():
    def inputsum(self):
        total = int(input("Enter the number whose total to be checked"))
        a = [1,2,3,4,5]
        for i in range(len(a)):
            for y in range (i+1, len(a)):
                if a[i] + a[y] == total:
                    print("Sum of digits :" + str(a[i]) + "and" + str(a[y]) + "is equal to" + str(total))
ie = inputElementSum()
ie.inputsum()