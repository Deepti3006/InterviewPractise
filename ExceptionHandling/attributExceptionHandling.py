class attributeExceptionHandling():
    def __init__(self):
        self.name = "Ananya"
        self.age ="6"

ae = attributeExceptionHandling()

try:
    print(ae.age)
    print(ae.deepti)
except AttributeError:
    print("Error as we are referring to the object which is not there ")