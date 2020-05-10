def anagramStringTest():

    string1 = input("Enter String one ")
    string2 = input("Enter String 2")
    if sorted(string1) == sorted(string2):
        print("Strings are anagram..")
    else:
        print("I am noot anangram")
anagramStringTest()