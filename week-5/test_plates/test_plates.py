from plates import is_valid

def test_one():
    assert is_valid("CS 50") == False
    assert is_valid("HELLO!") == False

def test_two():
    assert is_valid("H1LLO") == False
    assert is_valid("88TT") == False
    assert is_valid("44") == False
    assert is_valid("7HI") == False

def test_three():
    assert is_valid("HELLO") == True
    assert is_valid("H") == False
    assert is_valid("GOODBYE") == False

def test_four():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
