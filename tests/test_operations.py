import pytest
from app.operations import Add, Subtract, Multiply, Divide, Power, Root


@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 8),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert Add.execute(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (-1, 1, -2),
    (0, 0, 0),
])
def test_subtract(a, b, expected):
    assert Subtract.execute(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 15),
    (-1, 1, -1),
    (0, 0, 0),
])
def test_multiply(a, b, expected):
    assert Multiply.execute(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2),
    (10, 5, 2),
    (5, 2, 2.5),
])
def test_divide(a, b, expected):
    assert Divide.execute(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError):
        Divide.execute(5, 0)


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 8),
    (4, 0.5, 2),
    (5, 1, 5),
])
def test_power(a, b, expected):
    assert Power.execute(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (27, 3, 3),
    (16, 4, 2),
])
def test_root(a, b, expected):
    assert round(Root.execute(a, b), 5) == round(expected, 5)


def test_root_zero_degree():
    with pytest.raises(ValueError):
        Root.execute(27, 0)
