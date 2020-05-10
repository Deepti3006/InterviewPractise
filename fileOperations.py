import pandas as pd
def fileOpen():
    #file_1 = open("1.txt","w+")
    #file_1.write("I need to crack the interv")
    file_1 = open("1.txt","r+")
    print(file_1.readlines())
    print(file_1.readline(1))

def readCSV():
    df = pd.read_csv("1.csv",delimiter='\t')
    print(df.keys())
    print(df.values)
#readCSV()

def convertFileToCSV():

    read_file = pd.read_csv("1.txt")
    read_file.to_csv("2.CSV")
    df = pd.read_csv("2.CSV")
    print(df.values)

def readExcel():

    read_excel = pd.read_excel("1.xlsx")
    print(read_excel.keys())
    print(read_excel.values())

def convertFileToExcel():
    read_excel = pd.read_excel("1.txt")
    read_excel.to_excel("2.xlxs")
    ex1 = pd.read_excel("2.xlxs")
    print(ex1.keys())
    print(ex1.values)







readExcel()
