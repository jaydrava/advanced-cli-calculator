# tests/test_calculation.py

import pytest
from app.calculation import CalculationFactory


@pytest.mark.parametrize("expression, expected", [
    ("2 + 3", 5),
    ("10 - 4", 6),
    ("6 * 7", 42),
    ("8 / 2", 4),
    ("2 ^ 3", 8),
    ("16 root 2", 4)
])
def test_valid_expressions(expression, expected):
    result = CalculationFactory.process(expression)
    assert result == expected


@pytest.mark.parametrize("bad_expr", [
    "5 @ 3",
    "7 plus 3",
    "5 ** 2",
    "2+",
    "+ 2 2",
    "2 + 2 + 2"
])
def test_invalid_expressions(bad_expr):
    with pytest.raises(ValueError):
        CalculationFactory.process(bad_expr)
