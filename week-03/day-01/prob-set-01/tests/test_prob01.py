import pytest
from prob01 import is_valid_post_format

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
    assert is_valid_post_format(s) == expected
