import pytest
from prob03 import prob03


@pytest.mark.parametrize("scroll, expected", [
    ("cigam", "magic"),  # example
    ("lleps", "spell"),  # example
    ("", ""),            # edge: empty
    ("a", "a"),          # edge: single character
])
def test_prob03(scroll, expected):
    assert prob03(scroll) == expected
