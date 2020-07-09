def countOccuranceOfWordsInFile():

    all_freq={}
    with open("1.txt" ,"r+") as f:
        for line in f:
            words = line.split()
            for word in words:
                if word in all_freq:
                    all_freq[word] =all_freq[word]+1
                else:
                    all_freq[word] =1
    print(all_freq)

    for key,values in all_freq.items():
        if key == "Write":
            print(values)

countOccuranceOfWordsInFile()