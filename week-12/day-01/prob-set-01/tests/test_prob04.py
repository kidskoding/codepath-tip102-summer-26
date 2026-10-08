import pytest
from prob04 import prob04


@pytest.mark.parametrize("sequence, move, expected", [
    ("airairwater", "air", 2),
    ("fireearthfire", "fire", 1),
    ("waterfire", "air", 0),
    ("ababab", "ab", 3),
    ("aaa", "a", 3),
])
def test_prob04(sequence, move, expected):
    assert prob04(sequence, move) == expected
