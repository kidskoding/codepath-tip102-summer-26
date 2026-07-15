import pytest
from prob03 import reverse_scroll


@pytest.mark.parametrize("scroll, expected", [
    ("cigam", "magic"),  # example
    ("lleps", "spell"),  # example
    ("", ""),            # edge: empty
    ("a", "a"),          # edge: single character
])
def test_prob03(scroll, expected):
    assert reverse_scroll(scroll) == expected
