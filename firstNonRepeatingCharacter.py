def firstNonRepeatingCharater():
    notrepeat = []
    name = input("Enter the String")
    for char in name:
        if name.count(char) == 1:
            if char not in notrepeat:
                notrepeat.append(char)


    print (notrepeat)

firstNonRepeatingCharater()