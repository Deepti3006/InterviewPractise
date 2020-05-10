class sumOfDigits():

    def digitSum(self):

        number = int(input("Enter the number :"))
        total = 0
        while number > 0:
            dig = number%10
            print(str(dig))
            total = total + dig
            number = number//10
            print("I am in //" + str(number))
            print("Total of Digits is :" + str(total))

sof = sumOfDigits()
sof.digitSum()