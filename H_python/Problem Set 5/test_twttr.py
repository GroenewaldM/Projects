import twttr

def main():
    test_shorten()

def test_shorten():
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("testaeiou") == "tst"
    assert twttr.shorten("TTTT") == "TTTT"
    assert twttr.shorten("CS50") == "CS50"

if __name__ == "__main__":
    main()
