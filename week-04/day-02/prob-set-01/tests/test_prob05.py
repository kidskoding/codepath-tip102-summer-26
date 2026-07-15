import pytest
from prob05 import prob05


@pytest.mark.parametrize("html, expected", [
    ("<div><p></p></div>", True),
    ("<div><p></div></p>", False),
    ("<div><p><a></a></p></div>", True),
    ("<div><p></a></p></div>", False),
    ("", True),          # empty is trivially balanced
    ("<div>", False),    # unclosed opening tag
    ("</div>", False),   # closing tag with nothing open
])
def test_prob05(html, expected):
    assert prob05(html) == expected
