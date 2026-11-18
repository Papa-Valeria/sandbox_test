import pytest

from clamp import clamp


def test_inside_range():
    assert clamp(5, 0, 10) == 5


def test_below_range():
    assert clamp(-3, 0, 10) == 0


def test_above_range():
    assert clamp(20, 0, 10) == 10


def test_inclusive_minimum():
    assert clamp(0, 0, 10) == 0


def test_inclusive_maximum():
    assert clamp(10, 0, 10) == 10


def test_invalid_range():
    with pytest.raises(ValueError):
        clamp(5, 10, 0)