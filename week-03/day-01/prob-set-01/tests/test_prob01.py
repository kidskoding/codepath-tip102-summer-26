import pytest
from prob01 import prob01

@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("", True),        # empty is trivially balanced
    ("(", False),      # unclosed opener
    (")", False),      # closer with empty stack
    ("([)]", False),   # wrong closing order
])
def test_prob01(s, expected):
    assert prob01(s) == expected
