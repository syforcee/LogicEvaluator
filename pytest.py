#check function test

import checker

def test_answer():
    assert checker.check('b') == True
    assert checker.check('balon') == True
    assert checker.check('b|') == False
    assert checker.check('( a | b  ') == False
    assert checker.check('( a | b  )') == True
    assert checker.check('( a | b  )&(c>d)') == True
    assert checker.check('(a > > >> bb)') == False
    assert checker.check('(( a > b) > c)') == True
    assert checker.check('( a | b  )&(c>d))') == False


def main():
    print("Test")
    test_answer()

if __name__=="__main__":
    main()