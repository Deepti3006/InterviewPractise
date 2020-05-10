class removeDuplicate():
    def findDuplicates(self):
        total = int(input("Enter total number of elements :"))
        a=[]
        for i in range(total):
            element = int(input("Enter the element to be added"))
            a.append(element)
        print(str(a))
        for i in range(len(a)):
            for y in range(i+1, len(a)):
                if a[y] == a[i]:
                    print("I am duplicate " + str(a[i]) + "and at position" + str(i) + str(y))
        a.remove(a[y])
        print(str(a))

rD = removeDuplicate()
rD.findDuplicates()

