import json
def convertFileToJson():

    file = open("5.txt","r")
    dict1 ={}
    for lines in file:
        command,description = lines.strip().split(None,1)
        dict1[command] = description.strip()
    out_file = open("1.json","w")
    json.dump(dict1,out_file)

    file.close()
    out_file.close
convertFileToJson()
