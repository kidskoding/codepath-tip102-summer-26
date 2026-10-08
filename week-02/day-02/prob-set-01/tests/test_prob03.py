import pytest
from prob03 import prob03


@pytest.mark.parametrize("station_layout, observations, expected", [
    ("pqrstuvwxyzabcdefghijklmno", "wildlife", 45),
    ("abcdefghijklmnopqrstuvwxyz", "cba", 4),
    ("abcdefghijklmnopqrstuvwxyz", "", 0),
    ("abcdefghijklmnopqrstuvwxyz", "a", 0),
])
def test_prob03(station_layout, observations, expected):
    assert prob03(station_layout, observations) == expected
