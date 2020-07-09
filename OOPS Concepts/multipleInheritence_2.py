class apple():
    def __init__(self,colour,type_apple):
        self.colour = colour
        self.type_apple =type_apple

    def printColour(self):
        print("print in apple class :" + str(self.colour))


    def typeofApple(self):
        print("print in apple class :" + str(self.type_apple))

class banana(apple):
    def __init__(self,colour,count_1):
        self.colour =colour
        self.count_1 =count_1

    def printColour(self):
        print("print in banana class" + self.colour)

    def count_1(self):
        print("count is as you need" + self.count_1)

class fruit(banana,apple):

    def __init__(self, colour,type_apple):
        self.colour = colour
        self.type_apple =type_apple



a=apple("RED" ,"FUJI")
a.printColour()
a.typeofApple()

b=banana("YELLOW", 30)
b.printColour()



f=fruit("PINK", "WASHINGTOM")
f.printColour()
f.typeofApple()

