import pytest
from prob03 import prob03


@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),
    ("([)]", False),
    ("(", False),  # never closed
    ("]", False),  # close with no open
])
def test_prob03(s, expected):
    assert prob03(s) == expected
