from seasons import return_date
from datetime import date

def test_func():
    assert return_date("1999-01-01") == date(1999, 1, 1)
