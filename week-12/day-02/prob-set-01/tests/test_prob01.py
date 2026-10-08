import pytest
from prob01 import prob01


@pytest.mark.parametrize("s, t, expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("", "", True),
    ("ab", "a", False),  # different lengths
    ("aab", "abb", False),  # same letters, different counts
])
def test_prob01(s, t, expected):
    assert prob01(s, t) == expected
