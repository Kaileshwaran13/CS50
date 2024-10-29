from plates import is_valid


def main():
    testSize()
    testStart()
    testNum()
    testZeros()
    testChar()

def testSize():
    assert is_valid("HI") == True
    assert is_valid("ABCDEFG") == False

def testStart():
    assert is_valid("AA") == True
    assert is_valid("A2") == False

def testNum():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22S") == False

def testZeros():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def testChar():
    assert is_valid("PI3.14") == False

if __name__ == "__main__":
    main()