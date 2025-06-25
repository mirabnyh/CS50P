from um import count

def test_c1():
    assert count("UM") == 1
    assert count("um") == 1

def test_c2():
    assert count("um...") == 1
    assert count("hello, um, friend, um") == 2

def test_c3():
    assert count("Um, thanks for the album.") == 1
    assert count("mum um yum UM") == 2
