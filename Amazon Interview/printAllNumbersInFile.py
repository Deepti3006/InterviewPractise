def printAllNumbersInFile():

    with open("1.txt","r") as f:
        for line in f:
            words = line.split()
            for word in words:
                for letter in word:
                    if letter.isdigit():
                        print(letter)
printAllNumbersInFile()