def countDuplicateCharacters():

    string1 = input("Enter the string")
    string2 =""
    string1 = string1.lower()
    string1 = string1.replace(" ","")
    print(string1)
    for i in string1:
        index = string1.count(i)
        if index >1 and i not in string2:
            string2 = string2+i+str(index)
    print(string2)

countDuplicateCharacters()

