import pytest
from prob03 import prob03

@pytest.mark.parametrize("title, expected", [
    ("A Santa at NASA", True),
    ("Social Media", False),
    ("", True),   # empty reads same both ways
    ("x", True),  # single character
    ("No lemon, no melon", True),  # ignores case/punct
])
def test_prob03(title, expected):
    assert prob03(title) == expected
