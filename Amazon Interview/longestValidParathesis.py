def longestValidParenthesis(string1):
    stack =[]
    for i in string1:
        if stack:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    print(len(stack))
string1=")()())"
longestValidParenthesis(string1)