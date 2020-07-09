def elementOccuroingOddNumber(arr):
    all_freq ={}
    for i in arr:
        if i in all_freq:
            all_freq[i] = all_freq[i] +1
        else:
            all_freq[i] =1
    print(all_freq)
    for key,values in all_freq.items():
        if values%2 != 0:
            print(key)

arr =[1,2,3,1,2,3,4,1,2,3,1,2,4,3,4]
elementOccuroingOddNumber(arr)
