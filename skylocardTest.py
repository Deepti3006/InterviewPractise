import pandas as pd

def skylocardtest():

    n = int(input("Enter total number of cards"))
    arr_color=[]
    for i in range(n):
        elem = input("Enter the card")
        arr_color.append(elem)
    print(arr_color)
    arr_color_r =[]
    arr_color_g =[]
    #print(sorted(arr_color , reverse=True))
    for i in range(len(arr_color)):
        if arr_color[i].startswith("R"):
            arr_color_r.append(arr_color[i])
        else:
            arr_color_g.append(arr_color[i])
    print(sorted(arr_color_r) + sorted(arr_color_g))

def skylocardTestWithSingleLineInput():

    string1 = input("Enter the string needed")
    words = string1.split()
    words.sort()
    for word in words:
        print(word)

def readExcel():
    read_excel = pd.read_excel("1.csv")

    read_excel.sort(columns ="Serial Number")





#skylocardtest()
#skylocardTestWithSingleLineInput()
readExcel()