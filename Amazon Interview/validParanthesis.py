def validParanthesis(string1):

    stack=[]
    mapping ={"(":")" ,"{":"}","[":"]"}
    for i in string1:
        if i in mapping:
            stack.append(i)

        elif stack:
            print(i)
            if mapping[stack.pop()] != i:
                return False
            print(stack)
        else:
            return False
    return len(stack) ==0
string1 ="()[]{}]"
validParanthesis(string1)