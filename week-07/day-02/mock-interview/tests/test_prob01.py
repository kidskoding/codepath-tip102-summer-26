import pytest
from prob01 import prob01


@pytest.mark.parametrize("ransomNote, magazine, expected", [
    ("a", "b", False),        # example 1
    ("aa", "ab", False),      # example 2
    ("aa", "aab", True),      # example 3
    ("a", "a", True),         # exact match, single char
    ("abc", "cba", True),     # same letters, different order
    ("aab", "ab", False),     # note longer than magazine
])
def test_prob01(ransomNote, magazine, expected):
    assert prob01(ransomNote, magazine) == expected
