def smart_multiply(func):

   def inner(a,b):
      print("I am going to multiply")
      return func(a,b)
   return inner

@smart_multiply
def multiply(a,b):
    return a*b

colour =('orange' ,'banana' ,'apple' ,'jackfruit')
print(enumerate(colour))
for element in enumerate(colour):
    print(element)
import json
def jsonToPython():
    x = '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["age"])


def pythontoJson():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    j =json.dumps(x)
    print(j)
    j.upper()
    print(j)
    print (j[1])



res=multiply(2,2)
print(res)
jsonToPython()
pythontoJson()