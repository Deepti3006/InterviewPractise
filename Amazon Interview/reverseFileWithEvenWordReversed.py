def reverseFileWithEvenWordReversed():

    with open("1.txt","r") as file:
        data = file.read()
        data2= data[::-1]
        file.close()

    with open("3.txt","w") as file1:
        file1.write(data2)
        file1.close()

reverseFileWithEvenWordReversed()