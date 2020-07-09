def missingNumberWhenLengthIsGiven(arr,n):

    for i in range(1,n):
        if i not in arr:
            print(i)
arr=[1,2,3,5]
n=5
missingNumberWhenLengthIsGiven(arr,n)