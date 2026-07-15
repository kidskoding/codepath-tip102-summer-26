import pytest
from prob03 import count_suits_iterative, count_suits_recursive


@pytest.mark.parametrize("suits, expected", [
    (["Mark I", "Mark I", "Mark III"], 2),   # example (one duplicate)
    ([], 0),                                  # empty
    (["Mark I"], 1),                          # single
    (["Mark I", "Mark I", "Mark I"], 1),      # all duplicates
])
def test_prob03(suits, expected):
    assert count_suits_iterative(suits) == expected
    assert count_suits_recursive(suits) == expected
