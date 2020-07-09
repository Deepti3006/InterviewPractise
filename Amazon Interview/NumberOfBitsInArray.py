def numberOfBitsInNumber():

    number = int(input("Enter the number: "))
    bin_number = bin(number)[2:]
    index = str(bin_number).count("1")
    arr =[]
    for i in range(len(str(bin_number))):
       if bin_number[i] == "1":
            arr.append(i)
    for i in range(len(arr)):
        if i >0:
            result = arr[i]-arr[i-1]
            print(result)



numberOfBitsInNumber()