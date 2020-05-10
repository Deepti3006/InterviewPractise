class Node:
    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def printlist(self):
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

    def reverseList(self):

        self.temp = None
        self.temp = self.headval
        self.last = self.headval.nextval.nextval
        self.headval = self.headval.nextval.nextval
        self.last = self.temp

    def revprintlist(self):
       print(self.last)
       print(self.last.nextval.dataval)
       print(self.temp)

    def reverse(self):
        prev = None
        current = self.headval
        while current is not None:
            next = current.nextval
            current.next = prev
            prev = current
            current = next
        self.headval = prev



list1 = SLinkedList()
list1.headval = Node(30)
e2 = Node(40)
e3 = Node(50)
list1.headval.nextval = e2
e2.nextval = e3

list1.printlist()

list1.reverse()
list1.printlist()

