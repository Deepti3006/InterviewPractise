def reverseWordInString(string1):

    print(string1)
    string2 =""
    #for i in reversed(string1.split(".")):
     #   string2= string2+"."+i
    #print(string2)
    arr_str = []
    for i in string1.split("."):
        arr_str.append(i)
    print(arr_str)
    print(arr_str[::-1])
    print((".").join(arr_str[::-1]))


reverseWordInString("i.like.this.program.very.much")