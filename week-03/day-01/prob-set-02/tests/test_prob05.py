import pytest
from prob05 import prob05


@pytest.mark.parametrize("watchlist, expected", [
    ("ABFCACDB", 2),
    ("ACBBD", 5),
    ("ACDB", 0),  # removing "CD" creates a new "AB"
    ("", 0),
])
def test_prob05(watchlist, expected):
    assert prob05(watchlist) == expected
