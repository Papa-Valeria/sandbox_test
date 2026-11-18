from calculator import multiply


def test_multiply():
    assert multiply(3, 4) == 12


def test_impossible_requirement():
    assert multiply(3, 4) == 13