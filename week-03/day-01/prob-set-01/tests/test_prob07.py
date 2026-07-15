import pytest
from prob07 import post_compare

@pytest.mark.parametrize("s, t, expected", [
    ("ab#c", "ad#c", True),
    ("ab##", "c#d#", True),
    ("a#c", "b", False),
    ("", "", True),       # both empty
    ("a#", "", True),      # left backspaces to empty
    ("###", "", True),     # backspacing empty stays empty
    ("a", "", False),      # non-empty vs empty
])
def test_prob07(s, t, expected):
    assert post_compare(s, t) == expected
