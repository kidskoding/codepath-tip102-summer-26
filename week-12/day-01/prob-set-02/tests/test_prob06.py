import pytest
from prob06 import prob06


@pytest.mark.parametrize("dna1, dna2, dna3, expected", [
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "", True),
    ("abc", "", "abc", True),
    ("a", "b", "abc", False),  # lengths don't add up
])
def test_prob06(dna1, dna2, dna3, expected):
    assert prob06(dna1, dna2, dna3) == expected
