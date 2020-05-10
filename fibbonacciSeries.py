def fibonnaciSeries():
    n = int(input("Enter the numbers in fibbonacci series"))
    first = 0
    second = 1
    a = []
    a.append(first)
    a.append(second)

    for i in range(2,n):
        next = first+ second
        a.append(next)
        first = second
        second = next
    print(a)
fibonnaciSeries()
