import plates

def test_short():
    assert plates.is_valid("P") == "Invalid"

def test_long():
    assert plates.is_valid("PLATE12") == "Invalid"

def test_zero():
    assert plates.is_valid("PLATE0") == "Invalid"

def test_number():
    assert plates.is_valid("PL12TE") == "Invalid"

def test_valid():
    assert plates.is_valid("PLATE1") == "Valid"