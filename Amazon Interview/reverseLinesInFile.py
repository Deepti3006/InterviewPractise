def reverseLinesInFile():

    with open("1.txt", "r") as f:
        data = f.readlines()
        data2 = data[::-1]
        f.close()

    with open("10.txt","w") as f1:
        f1.writelines(data2)
        f1.close()

    with open("10.txt", "r") as f4:
        print(f4.readlines())
        f4.close()
reverseLinesInFile()