from working import convert
import pytest

def test_c1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12 PM") == "00:00 to 12:00"
    assert convert("4 PM to 7:30 PM") == "16:00 to 19:30"
    assert convert("8:30 AM to 5:30 PM") == "08:30 to 17:30"

def test_c2():
    with pytest.raises(ValueError):
        convert("7 AM - 9 PM")

def test_c3():
    with pytest.raises(ValueError):
        convert("8:60 AM to 8 PM")
