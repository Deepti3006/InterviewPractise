def findingNumbers(arr):
    # remove the duplicates
    # sort the list
    all_freq ={}
    for i in arr:
        if i in all_freq:
            all_freq[i] =all_freq[i] +1
        else:
            all_freq[i] =1
    for key,values in all_freq.items():
        if values == 2:
            print(key)






arr =[2,1,3,2]
findingNumbers(arr)