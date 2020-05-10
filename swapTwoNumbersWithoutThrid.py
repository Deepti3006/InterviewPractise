def swapTwoNumbersWithoutThird():
    number1 = int(input("Enter the first number"))
    number2 = int(input("Enter the second number"))
    number1 = number1+number2
    number2 = number1-number2
    number1 = number2-number1

    print("number1 : " + str(abs(number1)))
    print("number2 : " + str(abs(number2)))
    print("number1 : " + str(number1))
    print("number2 : " + str(number2))
swapTwoNumbersWithoutThird()