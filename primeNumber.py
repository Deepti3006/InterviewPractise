def primeNumber():
    number = int(input("Enter the number which needs to be checked"))
    for i in range(2, number):
        if number % i == 0:
            print("I am not prime and divisble by :" + str(i))
            break
        else:
            print("I am prime")
primeNumber()