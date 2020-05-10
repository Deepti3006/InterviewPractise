def removeDuplicateString():

    a = input("Enter the string")

    for char in a:
        if a.count(char) > 1:
            print("I am in")
            b= a.replace(char,'')
    print(b)
removeDuplicateString()