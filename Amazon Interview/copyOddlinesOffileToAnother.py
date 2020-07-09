def copyOddlinesOffileToAnother():

    file1 = open("1.txt" ,"r")

    file2 = open("4.txt" ,"w")

    data = file1.readlines()
    type(data)
    for i in range(len(data)):
        if i%2 != 0:
            file2.writelines(data[i])

    file1.close()

    file2.close()

    file2 = open("4.txt","r")
    data = file2.read()
    print(data)
    file2.close()
copyOddlinesOffileToAnother()