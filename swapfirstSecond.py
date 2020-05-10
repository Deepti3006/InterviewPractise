class swapFirstAndLast():

    def swapFirst(self):
        a = []
        total = int(input("Enter the number of elements"))
        for i in range(0,total):
            elem = int(input("Enter the element to be added in list"))

            a.append(elem)
            print(a)
            if i == total-1:
                print("I vcame in")
                temp =a[0]
                a[0]=a[total -1]
                a[total -1]= temp

                print(a)

sf = swapFirstAndLast()
sf.swapFirst()


