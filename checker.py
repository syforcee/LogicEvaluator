#alt, kon, impl

#OPEN
#operator->zmienna, (,
#(->zmienna,(

#VAR
#zmienna->),operator

#CLOSE
#)->),operator


#split aby oddzielic spacje
#oddzielic wszystkiezmienne
#wykryc tautologie, jezlei dla wszystkich kombinacji 1 0 wychodzi rrezultat 1 to jest tautolaogai

#zamaiana liczby na binarke przez dzielenie

#zadanie DOM na czwarte zajecia

#signaling error placemen

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
    letter = [chr(x) for x in range(97,123)]
    operators = ['|','&','>']
    variables =[]
    leng = len(function)
    lastChar=''
    waSpace=0
    i=0
    openBrackets=0

    if leng<2:
        if function[0] in letter:
            return True

    while i<leng:
        char = function[i]
        if char == ' ':
            i+=1
            continue
        if char =='(':
            if lastChar not in operators and lastChar!='(' and lastChar!='':
                print()
                printError(function, i)
                return False
            openBrackets += 1
            lastChar = '('
        if char in operators:
            if lastChar not in letter and lastChar!=')':
                printError(function, i)
                return False
            lastChar='|'
        elif char == ')':
            if lastChar not in letter and lastChar !=')':
                printError(function, i)
                return False
            openBrackets-=1
            lastChar=')'
        elif char in letter:
            if lastChar in letter:
                printError(function, i)
                return False
            lastChar = char
            # blok czytania zmiennej
            if i+1 < leng and function[i+1] in letter:
                j=i+1
                rest=function[j]
                while(rest in letter and j<leng):
                    char = char+rest
                    j+=1
                    if j<leng:
                        rest=function[j]

                i=j-1
            if char not in variables and lastChar!='':
                variables.append(char)
            elif lastChar not in operators and lastChar!='(':
                printError(function, i)
                return False

        i+=1
    if openBrackets!=0:
        print('Brackets dont match')
        printError(function, i)
        return False
    if lastChar in operators:
        printError(function,i)
        return False

    print(variables)
    return True

#def tautology(varCount):

def spaceOut(function):
    return function.replace(" ", "")

def main():
    fun = 'a   |b  >c '
    print("Check:")
    if check(fun):
        print(spaceOut(fun))

if __name__=="__main__":
    main()