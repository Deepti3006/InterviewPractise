def findVowelsConsonants():

    string1 = input("Enter the String ")
    vowels =[]
    consonants =[]
    for char in string1:
        if ((char == 'a') or (char == 'e') or (char == 'i') or (char == 'o')):
            print("I am vowel")
            vowels.append(char)
        else:
            print("I am consonant")
            consonants.append(char)

    print("total are : " + str(len(vowels)))
    print("total are : " + str(len(consonants)))
findVowelsConsonants()

