class specialStack():
    def __init__(self,n):
        self.specialstack =[]
        self.n =n

    def push(self,data):
        self.specialstack.append(data)
        if self.isFull():
            print("Done")

    def pop(self,data):
        self.specialstack.remove(data)

    def isEmpty(self):
        if len(self.specialstack) == 0:
            return True
        else:

            return False

    def isFull(self):
        if len(self.specialstack) == self.n:
            return True
        else:
            return False

    def minStack(self,specialstack):
        specialstack = sorted(specialstack)
        print(specialstack[0])

    def printlist(self):
        print(self.specialstack)

s =specialStack(5)
s.push(80)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.printlist()
s.pop(50)
s.printlist()
checkEmpty =s.isEmpty()
print(checkEmpty)
checkFull = s.isFull()
print(checkFull)
s.minStack(s.specialstack)







