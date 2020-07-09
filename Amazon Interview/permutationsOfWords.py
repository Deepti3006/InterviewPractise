import itertools

def permutationOfWords(word):

    char_p =[]
    char_sequences = itertools.permutations(word)
    for char in char_sequences:
        print(char)
        #string_permutation = "".join(char)
        char_p.append(char)
    print(len(char_p))


permutationOfWords("ABSG")