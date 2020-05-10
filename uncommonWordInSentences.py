def uncommonWordsInSentence():
    test1 = ["elppa", "banana"]
    test2 = ["grape", "ananab"]
    test3 =[]
    test4 =[]
    final_count = []
    count =0
    for i in test1:
        s=sorted(i)
        test3.append(s)
    for i in test2:
        s=sorted(i)
        test4.append(s)
    print(test4)
    print(test3)
    for i in test3:
        if i in test4:

            count = count+1
            final_count.append(count)
    print(str(final_count))
uncommonWordsInSentence()