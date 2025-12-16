from calculator import add
def test_add():
    assert add(2, 2) == 555

def test_add_negative():
    assert add(-1, 1) == 0
