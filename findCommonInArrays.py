from collections import Counter
def commonElements(arr1,arr2,arr3):
    a1=Counter(arr1)
    a2=Counter(arr2)
    a3=Counter(arr3)
    resultDict = dict(a1.items() & a2.items() & a3.items())
    common =[]
    for key,values in resultDict.items():
        for i in range(0,values):
            common.append(key)
    print(common)

def commonElementsArray(arr1,arr2,arr3):

    resultArray = arr1+arr2+arr3
    common =[]
    count = 0
    for i in range(len(resultArray)):
        for j in range(i+1,len(resultArray)):
            if resultArray[i]==resultArray[j]:
                count=count+1
                common.append(resultArray[i])

    coomon_uniq=[]
    for i in range(len(common)):
        for y in range(i + 1, len(common)):
            if common[i] == common[y]:
                common.remove(common[y])
    print(common)

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
commonElementsArray(ar1,ar2,ar3)