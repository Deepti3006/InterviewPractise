def missingNumberInArray(arr):

    last_element = arr[-1]
    print(last_element)

    original_array = []
    for i in range(1,last_element+1):
        original_array.append(i)

    diff  = set(original_array).symmetric_difference(set(arr))
    for i in diff:
        print(i)

arr = [1,2,3,4,5,6,7,8,10]
missingNumberInArray(arr)