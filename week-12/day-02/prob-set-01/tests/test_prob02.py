import pytest
from prob02 import prob02


@pytest.mark.parametrize("s, expected", [
    ("00110011", 6),
    ("10101", 4),
    ("0", 0),
    ("01", 1),
    ("000111", 3),  # "01", "0011", "000111"
])
def test_prob02(s, expected):
    assert prob02(s) == expected
