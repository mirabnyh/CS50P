from numb3rs import validate

def test_one():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True

def test_two():
    assert validate("1000") == False
    assert validate("1.0.1.2.3") == False
    assert validate("255.255.255.256") == False
    assert validate("290.1.1.1") == False
