def countOccuranceOfeachletter():
    string1 = input("Enter the string")
    string2 =""
    for letter in string1:
        index = string1.count(letter)
        if letter not in string2:
            string2=string2+letter+str(index)
    print(string2)

countOccuranceOfeachletter()