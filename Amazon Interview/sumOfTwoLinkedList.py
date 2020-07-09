class Node:
    def __init__(self, data):
        self.data =data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head =None

    def printList(self):
       printval = self.head
       while printval is not None:
         print(printval.data)
         printval = printval.next

    def reverse(self):
        df =[]
        current = self.head
        while current:
            df.append(self.head.data)
            current = current.next
        print(df)
        return sum(df)
l =SLinkedList()
l.head =Node(30)
e2 = Node(60)
l.head.next = e2
l.printList()
l2 =SLinkedList()
l2.head =Node(40)
e3 = Node(100)
l2.head.next = e3
l2.printList()
sum1 = l.reverse()
sum2 =l2.reverse()
sum = sum1+sum2
print(sum)