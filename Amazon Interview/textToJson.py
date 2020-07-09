import json

def textToJson():

   # Text file to changed to dict
   # dump to json

   dict1={}

   with open("2.txt","r") as f:
      for line in f:
        cammand,description = line.strip().split(None,1)
        dict1[cammand] = description.strip()

   jsonfile= open("70.json","w")
   json.dump(dict1,jsonfile)
textToJson()