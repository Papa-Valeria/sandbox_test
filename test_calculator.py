from calculator import add, multiply


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_mixed_numbers():
    assert add(-2, 5) == 3


def test_add_zero():
    assert add(0, 7) == 7

def test_multiply():
    assert multiply(3, 4) == 12


def test_impossible_requirement():
    assert multiply(3, 4) == 13