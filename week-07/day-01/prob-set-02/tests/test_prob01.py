import pytest
from prob01 import get_village_class_iterative, get_village_class_recursive

CASES = [
    (432, 3),   # example
    (9, 1),     # example
    (0, 1),     # edge: zero is one digit
    (1000, 4),  # edge: trailing zeros
]


@pytest.mark.parametrize("population, expected", CASES)
def test_prob01_iterative(population, expected):
    assert get_village_class_iterative(population) == expected


@pytest.mark.parametrize("population, expected", CASES)
def test_prob01_recursive(population, expected):
    assert get_village_class_recursive(population) == expected
