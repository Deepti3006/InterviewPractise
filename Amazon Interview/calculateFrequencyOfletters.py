from collections import Counter

def calculateFrequencyOfLetters():

    string1 = input("Enter the string")
    all_freq = {}

    for i in string1:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    print(str(all_freq))

def calculateWithFor(string1):

   for i in string1:
        for y in range(i+1,len(string1)):
          index = string1.count(string1[y])
          if  string1[i] is string1[y]:
            string1.replace(string1[i]," ")

   print("{}-{}".format(str(index),string1[i]))



#calculateFrequencyOfLetters()
calculateWithFor("Hello World")
