def camelCase():

    string1 ="Hi Hello HelloWorld HiTech HiGeek HiTechWorld HiTechCity HiTechLab"
    all_caps =[]
    all_words=[]

    pattern = "HA"
    string2 =""

    for i in string1.split():
        l= len(i)
        print(l)
        all_words.append(i)
        for letter in i:
            print(letter)
            while letter.isupper():
                string2=string2+letter
                all_caps.append(string2)
            else:
                print("out")








    print(all_words)
    print(all_caps)

camelCase()