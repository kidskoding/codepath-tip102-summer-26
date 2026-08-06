import pytest
from prob02 import prob02


@pytest.mark.parametrize("s, t, expected", [
    ("abcd", "abcde", "e"),   # example 1
    ("", "y", "y"),           # example 2 (empty s)
    ("aa", "aaa", "a"),       # added letter duplicates existing ones
    ("ab", "aba", "a"),       # duplicate of one existing letter
])
def test_prob02(s, t, expected):
    assert prob02(s, t) == expected
