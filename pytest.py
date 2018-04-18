#check function test

import Parser

def test_answer():
    assert Parser.check('b') == True
    assert Parser.check('balon') == True
    assert Parser.check('b|') == False
    assert Parser.check('( a | b  ') == False
    assert Parser.check('( a | b  )') == True
    assert Parser.check('( a | b  )&(c>d)') == True
    assert Parser.check('(a > > >> bb)') == False
    assert Parser.check('(( a > b) > c)') == True
    assert Parser.check('( a | b  )&(c>d))') == False
    assert Parser.check('a|b > bda') == True
    assert Parser.check('((a |      b) & ad )> c') == True
    assert Parser.check('( ! abba  ) | ( b > c > d     )') == True


def main():
    print("Test")
    test_answer()

if __name__=="__main__":
    main()