import PostfixConverter

class PostfixCalc:
    def __init__(self,function):
        self.postfix = PostfixConverter.convert_postfix(function.function)
        self.variables = function.variables
        self.operators = ['!','|', '&', '>','=','v']
        self.correctValues=[]
        self.reducedExpression=[]

    #Generates bit mask
    def values(self):
        result = []
        variableCount = len(self.variables)

        for i in range(0, 2 ** variableCount):
            elem = list(bin(i)[2:])
            if len(elem) < variableCount:
                elem = ["0" for i in range(0, variableCount - len(elem))] + elem
            for j, y in enumerate(self.variables):
                if y in ['0', '1']:
                    elem[j] = y
            result.append(elem)

        result = sorted(result)
        return result

    #Checks if given statement is a tautology
    def tautology(self):
        binaryValues = self.values()
        correctValues=0

        for set in binaryValues:
            function = self.postfix[:]

            for bit, var in zip(set, self.variables):
                self.putValue(function,var,bit)
           # print(function)
            result = self.evaluate(function)
            if result[0]=='1':
                correctValues+=1
                self.correctValues= self.correctValues+ [set]
        if correctValues == len(binaryValues):
            return True
        else:
            return False

    #puts binary value to variable in postfix expression
    def putValue(self,expression, varaible, value):
        for i, part in enumerate(expression):
            if part == varaible:
                expression[i] = value

    #calculates logical value with given postfix function with values
    def evaluate(self, expression):
        stack=[]
        for part in expression:
            if part == '!':
                operand = stack.pop()
                if operand == '1':
                    operand = '0'
                else:
                    operand = '1'
                stack=stack+[operand]
            elif part in self.operators:
                arg1 = stack.pop()
                arg2 = stack.pop()
                res = self.logicalValue(arg2,arg1,part)
                stack=stack+[res]
            else:
                stack = stack+[part]
        return stack

    #returns logical value for operator and its arguments
    def logicalValue(self, arg1, arg2, operator):
        if operator == "&":
            if arg1=='1' and arg2=='1':
                return '1'
            else:
                return '0'

        elif operator == "|":
            if arg1=='0' and arg2=='0':
                return '0'
            else:
                return '1'

        elif operator == '>':
            if arg1 == '1' and arg2 == '0':
                return '0'
            else:
                return '1'

        elif operator =='=':
            if arg1 == arg2:
                return '1'
            else:
                return '0'

        elif operator == 'v':
            if (arg1 == '1' and arg2 =='0') or (arg1=='0' and arg2=='1'):
                return '1'
            else:
                return '0'

    #performs reduction
    def reductor(self):
        is_tautology = self.tautology()

        returned_true =[]#= self.correctValues

        for item in self.correctValues:
            returned_true= returned_true+[''.join(item)]

        was_change = True
        while was_change:
            was_change=False
            result = []
            for item in returned_true:

                pom=[]
                pom=self.differentByOne(item, returned_true)
                if pom:
                    was_change=True
                    result = result + pom
                else:
                    result = result+[item]

            pom = list(set(result))
            returned_true = pom[:]

        self.reducedExpression = returned_true



    def differentByOne(self,val, list ):

        leng =len(val)
        result=[]
        for  piece in list:

            wasDifferent=False
            differentPlace=-1

            for i in range(leng):
                if (piece[i] != val[i]) and not wasDifferent and differentPlace==-1:
                    wasDifferent = True
                    differentPlace=i
                elif piece[i] != val[i]:
                    wasDifferent=False

            if wasDifferent:
                valCpy=piece[:]
                str2=''
                for i in range(leng):
                    if i!= differentPlace:
                        str2+=valCpy[i]
                    else:
                        str2+='x'

                result=result+ [str2]

        return result


    def __str__(self):
        expression=""
        for exp in self.reducedExpression:
            andMark = False
            for i in range(len(exp)):
                if exp[i]=='1':
                    if andMark:
                        expression += ' & '
                    expression += self.variables[i]
                    andMark=True

                elif exp[i]=='0':
                    if andMark:
                        expression += ' & '
                    expression += ('!' + self.variables[i])
                    andMark=True

            expression+=" | "
        expression=expression[:-2]
        return expression
