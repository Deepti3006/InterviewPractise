import re

def checkSpecialCharacters():

    regex= re.compile('[@_!#$]')
    string = input("Enter the string")
    if regex.search(string) == None:
        print("I am not regex")
    else :
        print("I am regex")
checkSpecialCharacters()


