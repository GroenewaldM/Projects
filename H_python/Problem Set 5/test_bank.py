import bank

def test_hello():
    assert bank.value("hello") == "$0"

def test_h():
    assert bank.value("hi") == "$20"

def test_none():
    assert bank.value("sup") == "$100"
