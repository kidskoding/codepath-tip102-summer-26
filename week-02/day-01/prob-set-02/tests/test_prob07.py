import pytest
from prob07 import prob07


@pytest.mark.parametrize("signals, expected", [
    (["cd", "ac", "dc", "ca", "zz"], 2),
    (["ab", "ba", "cc"], 1),
    (["aa", "ab"], 0),
    ([], 0),
])
def test_prob07(signals, expected):
    assert prob07(signals) == expected
