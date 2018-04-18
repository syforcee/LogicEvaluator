import PostfixCalc
import Function
import sys


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

    if len(sys.argv)>1:
       fun = sys.argv[1]
    else:
        fun = 'a | b > c'

    simplyfy(fun,True)
