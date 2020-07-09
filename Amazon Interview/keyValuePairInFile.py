def keyValuePairInFile():
    d=dict()
    with open("5.txt","r")as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in d:
                    d[word] = d[word]+1
                else:
                    d[word]=1
    file.close()
    print(d)
    for key,values in d.items():
        print(key,values)

keyValuePairInFile()
