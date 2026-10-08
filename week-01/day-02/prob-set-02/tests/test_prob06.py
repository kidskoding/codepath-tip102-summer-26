import pytest
from prob06 import prob06


@pytest.mark.parametrize("s, expected", [
    ("robin", "ribon"),
    ("BATgirl", "BiTgArl"),
    ("batman", "batman"),
    ("", ""),
    ("xyz", "xyz"),
])
def test_prob06(s, expected):
    assert prob06(s) == expected
