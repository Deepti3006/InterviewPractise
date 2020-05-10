class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

class Slinkedlist:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def size(self):
        current = self.headval
        count = 0
        while current:
            count += 1
            current = current.nextval
        return count


list1 = Slinkedlist()
list1.headval = Node(30)
e2 = Node(40)
e3 = Node(50)
e4 = Node(60)
e5 = Node(70)
e6 = Node(80)
list1.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
e5.nextval = e6
list1.listprint()
print(list1.size())
print(round(list1.size()/2))
print(list1.headval.nextval.nextval.dataval)



