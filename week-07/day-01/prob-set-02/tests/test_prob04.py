import pytest
from prob04 import prob04


@pytest.mark.parametrize("name, expected", [
    ("eve", True),    # example
    ("ling", False),  # example
    ("", True),       # example: empty reads the same both ways
    ("a", True),      # edge: single character
    ("ab", False),    # edge: shortest non-palindrome
    ("abba", True),   # edge: even-length palindrome
])
def test_prob04(name, expected):
    assert prob04(name) == expected
