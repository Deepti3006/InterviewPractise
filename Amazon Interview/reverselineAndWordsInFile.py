def reverselineAndWordsInFile():

    with open("1.txt","r") as f:
        data = f.read()
        data2 = data[::-1]
    f.close()

    with open("20.txt","w") as f1:
        f1.write(data2)
        f1.close()

    with open("20.txt","r") as f2:

        print(f2.read())
reverselineAndWordsInFile()