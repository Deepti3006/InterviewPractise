def reverseSentenceWithoutReversingWord(string1):
    length =0
    string2 =""
    arr =[]
    for i in string1.split("."):
        length = length+1
        arr.append(i)
    print(length)
    print(arr)
    length = length-1
    while length >= 0:
            if length == 0:
                string2 = string2+arr[length]
            else:
                string2 = string2 + arr[length] +"."
            length = length -1
    print(string2)




string1 = "pqr.mno"
reverseSentenceWithoutReversingWord(string1)