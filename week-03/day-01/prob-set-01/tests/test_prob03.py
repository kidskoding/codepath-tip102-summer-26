import pytest
from prob03 import is_symmetrical_title

@pytest.mark.parametrize("title, expected", [
    ("A Santa at NASA", True),
    ("Social Media", False),
    ("", True),   # empty reads same both ways
    ("x", True),  # single character
    ("No lemon, no melon", True),  # ignores case/punct
])
def test_prob03(title, expected):
    assert is_symmetrical_title(title) == expected
