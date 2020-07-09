def reverseFileWithFileOnlySentence():

    with open("1.txt","r") as file:
        data = file.readlines()

        data2 = data[::-1]
        file.close()

    with open("2.txt","w") as  file1:
        file1.writelines(data2)
        file1.close()

reverseFileWithFileOnlySentence()