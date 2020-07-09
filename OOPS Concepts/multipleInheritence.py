class Name():

    def __init__(self, name,grade):
        self.name =name
        self.grade = grade

class Age():

    def __init__(self, age,grade):
        self.age =age
        self.grade =grade

class Student(Name,Age):
    n = Name("Ananya","12")
    a =Age("6","34")
    def __init__(self,grade):
        self.grade = grade
        self.name =n.name
        self.age = a.age

    def getDetails(self):
        print("The details are {},{},{}".format(self.name,self.age,self.grade))

n=Name("Ananya",12)
a=Age("6",33)
s=Student("4")
s.getDetails()
