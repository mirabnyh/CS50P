from fuel import gauge, convert
import pytest

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(40) == "40%"

def test_convert():
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("7/6")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
