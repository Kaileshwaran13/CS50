from bank import value

def main():
    test1()
    test2()
    test3()


def test1():
    assert value("hello") == 0
    assert value("Hello") == 0

def test2():
    assert value("hi") == 20
    assert value("hlak") == 20

def test3():
    assert value("what's") == 100
    assert value("cs50") == 100
    assert value("50") == 100

if __name__ == "__main__":
    main()