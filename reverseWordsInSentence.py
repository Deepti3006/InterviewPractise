def reverseWordsInSentence():

    sentence = input("Enter the string to be reversed")
    rev_sentence = ''.join(reversed(sentence))
    print(rev_sentence)

def reverseofWrod ():
    sentence = input("Enter the string to be reversed")

    for word in sentence.split() :
        print(word)
        word = word[::-1]
    print(sentence)


reverseofWrod()