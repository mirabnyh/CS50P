from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("PI = 3.14") == "P = 3.14"
