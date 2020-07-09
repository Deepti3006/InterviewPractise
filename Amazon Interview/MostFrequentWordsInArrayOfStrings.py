def mostFrequentlyWords():
    string1 = input("Enter the string")
    all_freq ={}
    for i in string1:
        if i in all_freq:
            all_freq[i] = all_freq[i] +1
        else:
            all_freq[i] = 1
    for key,values in all_freq.items():
        if key != " ":
            print("{}-{}".format(key,values))





mostFrequentlyWords()