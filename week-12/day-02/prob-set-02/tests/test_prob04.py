import pytest
from prob04 import prob04


@pytest.mark.parametrize("s, t, expected", [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("", "ahbgdc", True),
    ("abc", "", False),
    ("aec", "abcde", False),  # right letters, wrong order
])
def test_prob04(s, t, expected):
    assert prob04(s, t) == expected
