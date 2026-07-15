import pytest
from prob02 import find_cabin_index


@pytest.mark.parametrize("cabins, preferred_deck, expected", [
    ([1, 3, 5, 6], 5, 2),   # example (found)
    ([1, 3, 5, 6], 2, 1),   # example (insert in middle)
    ([1, 3, 5, 6], 7, 4),   # example (insert at end)
    ([1, 3, 5, 6], 0, 0),   # insert at front
    ([], 4, 0),             # empty -> insert at 0
])
def test_prob02(cabins, preferred_deck, expected):
    assert find_cabin_index(cabins, preferred_deck) == expected
