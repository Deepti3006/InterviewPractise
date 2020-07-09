class Node():
    def __init__(self,data):
        self.data = data
        self.next =None

class SLinkedList():
    def __init__(self):
        self.head = None


    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        rev =[]
        current = self.head
        while current:
            rev.append(current.data)
            current =current.next
        rev = rev[::-1]
        print(rev)

    def insertAtBegininng(self,node):

        temp = self.head
        self.head = Node(node)
        self.head.next = temp

    def insertAtEnd(self,node):
        lastnode = Node(node)
        current = self.head
        while current.next:
            current = current.next
        current.next = lastnode






sl = SLinkedList()
sl.head = Node(30)
e2 = Node(40)
e3 = Node(50)
sl.head.next =e2
e2.next =e3
sl.printLinkedList()
sl.reverse()
sl.insertAtBegininng(10)
sl.printLinkedList()
sl.insertAtEnd(60)
sl.printLinkedList()


