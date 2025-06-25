from bank import value

def test_one():
    assert value("HeLLO, word") == 0
    assert value("hello ALL") == 0

def test_two():
    assert value("How are you") == 20
    assert value("Hey!") == 20

def test_three():
    assert value("Whats' up") == 100
    assert value("Greetings") == 100
