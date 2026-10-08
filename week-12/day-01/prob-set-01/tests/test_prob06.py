import pytest
from prob06 import prob06


@pytest.mark.parametrize("katara_moves, toph_moves, expected", [
    ("waterbend", "earthbend", 6),
    ("bend", "bend", 4),
    ("fire", "air", 2),
    ("abc", "xyz", 0),
    ("", "air", 0),
])
def test_prob06(katara_moves, toph_moves, expected):
    assert prob06(katara_moves, toph_moves) == expected
