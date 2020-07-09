import json

def jsonToTextFile():

   with open("6.json","r") as f:
      python_object = json.load(f)

   with open("70.txt","w") as f2:
      f2.write(json.dumps(python_object))

   f.close()
   f2.close()
   with open("70.txt","r") as f3:
      print(f3.readlines())
jsonToTextFile()