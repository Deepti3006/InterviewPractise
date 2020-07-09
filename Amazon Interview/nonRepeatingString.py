def nonRepeatingCharacter():

    string1 = input("Enter the string :")
    string1 = string1.lower()
    count =0
    for i in string1:
        index = string1.count(i)
        while count < 1 and index==1:
            print(i)
            count = count+1
nonRepeatingCharacter()