import re
def getNumericFromthefile():
    count =0
    with open("1.txt" , "r") as f:
        for line in f:
            words = line.split()
            for i in words:
                for letter in i:
                    if letter.isdigit():
                        print("letters" + letter)
                        count =count+1
    print(count)

def getallspecialCharatersfromFile():
    count = 0
    with open("1.txt", "r") as f:
        for line in f:
            words = line.split()
            for i in words:
                for letter in i:
                   sp_ch = re.compile('[@_!#$]')

                   if sp_ch.search(letter):
                    count=count+1
                    print(letter)

    print(count)

def countAllNumbersInFile():
    count = 0
    with open("1.txt","r") as f:
        for line in f:
            words = line.split()
            count += len(words)
    print(count)

countAllNumbersInFile()