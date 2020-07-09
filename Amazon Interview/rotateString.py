def rotateString(string1,string2):

    if len(string1) == len(string2):
        totalString1 = string1+string1
        if string2 in totalString1:
            return True
        else:
            return False

res= rotateString("amazon","azonam")
print(res)
res= rotateString("geeksforgeeks","geeksgeeksfor")
print(res)