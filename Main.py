import PostfixCalc
import Function


def simplyfy(input, debug):

    fun = Function.Function(input)
    onp = PostfixCalc.PostfixCalc(fun)
    onp.reductor()
    if debug:
        print("Input: " + input)
        print("Postfix:")
        print(onp.postfix)
        print("Variables:")
        print(onp.variables)
        print("Expression is true for:")
        print(onp.correctValues)
        print("Is tautology: " + onp.tautology().__str__())

    print("Evaluated expression:")
    print(onp)


if __name__ == "__main__":

   # simplyfy()
    fun = 'a | b > c'
    simplyfy(fun,True)
    #fun = 'a | a v (a > b) = (c > d)'
    #fun = '((a |      b) & ad )> c'
    #fun = '( ! abba  ) | ( b > c > d     )'
    #print("Input: " + fun)

    #f = Function.Function(fun)
    #print(f.function)
    #print(f.variables)

    #p = PostfixCalc.PostfixCalc(f)
    #print("Postfix:")
    #print(p.postfix)
    #print("Variables:")
    #print(p.variables)

    #print("Possibilities:")
    #print(p.values())
    #p.reductor()
    #f.reducted = p.reductor()

    #print("Evaluation: ")
    #print(p)
