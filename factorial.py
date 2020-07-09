def factorial():
    number = int(input("input the number to find the factorial"))
    fact=1
    while number> 1:
        fact =fact*number
        number=number-1
    print("factorail :" + str(fact))
factorial()
