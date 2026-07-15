import pytest
from prob01 import count_suits_iterative, count_suits_recursive


@pytest.mark.parametrize("suits, expected", [
    (["Mark I", "Mark II", "Mark III"], 3),  # example
    ([], 0),                                 # empty
    (["Mark I"], 1),                         # single
])
def test_prob01(suits, expected):
    assert count_suits_iterative(suits) == expected
    assert count_suits_recursive(suits) == expected
