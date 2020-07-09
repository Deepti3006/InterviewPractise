import itertools

def permutationOfString(string1):
    permutation_list=[]
    character_sequence = itertools.permutations(string1)
    for char in character_sequence:
        string_permutation="".join(char)
        permutation_list.append(string_permutation)
    print(permutation_list)
    print(len(permutation_list))

permutationOfString("venkat")