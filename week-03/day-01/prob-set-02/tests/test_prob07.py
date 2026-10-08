import pytest
from prob07 import prob07


@pytest.mark.parametrize("watchlist, expected", [
    ("egcfe", "efcfe"),
    ("abcd", "abba"),
    ("seven", "neven"),
    ("a", "a"),
    ("racecar", "racecar"),
])
def test_prob07(watchlist, expected):
    assert prob07(watchlist) == expected
