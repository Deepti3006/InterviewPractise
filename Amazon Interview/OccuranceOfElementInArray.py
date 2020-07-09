def numberOfOccurancesOfNumberinArray():

    n = int(input("Enter number of Elements"))
    arr =[]
    for i in range(n):
        elem = input("enter the array number")
        arr.append(elem)

    print(arr)
    find_element = input("Enter the element to be found")
    Occurances = arr.count(find_element)
    print(Occurances)

numberOfOccurancesOfNumberinArray()
