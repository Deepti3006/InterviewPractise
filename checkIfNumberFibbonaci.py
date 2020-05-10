import math

def squareofNumber(x):
    s = int(math.sqrt(x))

    return s * s == x

def isFibbonacci(n):


    return squareofNumber(5*n*n+4)

if isFibbonacci(1)== True:
    print("Its Fibbonacci")
else:
    print("How can i be fibbonacci")

isFibbonacci(1)
