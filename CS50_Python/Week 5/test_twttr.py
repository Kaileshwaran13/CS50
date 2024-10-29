from twttr import shorten

def main():
    test_input()

def test_input():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("CS50") == "CS50"
    assert shorten("13") == "13"
    assert shorten("hello, world") == "hll, wrld"
    assert shorten("HELLO, WORLD") == "HLL, WRLD"
    assert shorten("hello, WORLD") == "hll, WRLD"
    assert shorten("._,") == "._,"

if __name__ == "__main__":
    main()