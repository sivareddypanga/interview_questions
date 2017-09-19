def parenthesis_matching(str):
    stack = []
    pushChars, popChars = "<({[", ">)}]"
    for c in str :
        if c in pushChars:
            stack.append(c)
        elif c in popChars:
            if not len(stack):
                return False
            else:
                stackTop = stack.pop()
                balancingBracket = pushChars[popChars.index(c)]
            if stackTop != balancingBracket :
                return False

    return not len(stack)

print  parenthesis_matching("[{[()]}{}]")
