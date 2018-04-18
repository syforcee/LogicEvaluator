
operators = ['!','|', '&', '>','=','v']
variables = []
allowedChars=['!','|', '&', '>','(',')',' ','=','v']

def printError(function, char):
    print(function)
    i=0
    str=''
    while i<char:
        str += ' '
        i+=1
    str+='^'
    print(str)
    return

def check(function):

    nextLeftBracket=True
    nextRightBracket=False
    nextOperator=False
    nextVariable=True
    nextNot=True

    lastChar=''
    leng=len(function)
    i=0
    openBrackets=0

    while i<leng:
        char = function[i]
        if char == ' ':
            i+=1
            continue

        elif char =="!":
            if not nextNot:
                printError(function, i)
                return False
            nextLeftBracket = True
            nextRightBracket = False
            nextOperator = False
            nextVariable = True
            nextNot = False
            lastChar = '!'
            i += 1

        elif char =='(':
            if not nextLeftBracket:
                printError(function, i)
                return False
            nextLeftBracket = True
            nextRightBracket = True
            nextOperator = False
            nextVariable = True
            nextNot = True
            openBrackets += 1
            lastChar = '('
            i += 1

        elif char in operators:
            if not nextOperator:
                printError(function, i)
                return False
            nextLeftBracket = True
            nextRightBracket = False
            nextOperator = False
            nextVariable = True
            nextNot = True
            lastChar = '|'
            i += 1

        elif char == ')':
            if not nextRightBracket:
                printError(function, i)
                return False
            openBrackets-=1
            nextLeftBracket = False
            nextRightBracket = True
            nextOperator = True
            nextVariable = False
            nextNot = False
            lastChar = ')'
            i += 1

        else:
            if not nextVariable:
                printError(function, i)
                return False
            nextLeftBracket = False
            nextRightBracket = True
            nextOperator = True
            nextVariable = False
            nextNot = False
            #browse through variable
            while i< leng and function[i] not in allowedChars:
                i+=1
            lastChar = 'a'

    if openBrackets!=0:
        print('Brackets dont match')
        printError(function, i)
        return False
    if lastChar in operators or lastChar =="(":
        return False
    return True

def spaceOut(function):
    return function.replace(" ", "")

#def insert_space(string, index)
def putSpace(ind, function):
    newFun = function[:ind] + ' ' + function[ind:]
    return newFun

def spaceIn(function):
    special = operators+['(']+[')']
    operatorSpot = []

    for i,char in enumerate(function):
        if char in special:
            operatorSpot+=[i]

    #offset created by inserting spaces to function
    k=0

    for i in operatorSpot:
        if i == 0:
            k+=1
            function = putSpace(i+k, function)
        else:
            if function[i+k-1] != ' ':
                function = putSpace(i+k,function)
                k+=1
            function = putSpace(i + k+1, function)
            k+=1
    if function[-1] == ' ':
        function = function[:-1]
    expr = function.split(' ')
    return expr
