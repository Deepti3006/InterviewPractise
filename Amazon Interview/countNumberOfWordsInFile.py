def countNumberOfWordsInFile():
    count=0
    with open("1.txt","r") as f:
        for line in f:
            words = line.split()
            for word in words:
                count=count+1

    print(count)
countNumberOfWordsInFile()