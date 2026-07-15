import pytest
from prob11 import prob11

@pytest.mark.parametrize("word, expected", [
    ("suspicerous", "suspcous"),
    ("Trigger", ""),
    ("Hunny", "Hunny"),
    # edge: empty string -> empty string
    ("", ""),
])
def test_prob11(word, expected):
    assert prob11(word) == expected
