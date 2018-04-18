import Parser

class Function:
    def __init__(self, expression):
        self.input = expression
        self.function = self._parse()
        self.variables = self._getVariables()
        self.reducted=[]

    def _parse(self):
        if Parser.check(self.input):
            fun = Parser.spaceOut(self.input)
            expr =Parser.spaceIn(fun)
        else:
            raise ValueError('Wrong input')
        return expr

    def _getVariables(self):
        return sorted(set([var for var in self.function if var not in ['!','|', '&', '>', '(',')','v','=']]))
