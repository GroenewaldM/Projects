import fuel 

def test_full():
    assert fuel.gauge(fuel.convert("1/1")) == "F"

def test_empty():
    assert fuel.gauge(fuel.convert("0/1")) == "E"

def test_percent():
    assert fuel.gauge(fuel.convert("34/100")) == "34 %"

