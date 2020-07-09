def fibbonacciInReverse(n):

    if n == 0:
        return 0
    if n ==1:
        return 1
    if n>1:
        return (fibbonacciInReverse(n-1) + fibbonacciInReverse(n-2))

n= 9
while n >= 0:
    print(fibbonacciInReverse(n))
    n=n-1
