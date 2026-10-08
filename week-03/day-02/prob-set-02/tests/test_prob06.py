import pytest
from prob06 import prob06


@pytest.mark.parametrize("terrain, expected", [
    ("00110011", 6),
    ("10101", 4),
    ("0", 0),
    ("01", 1),
])
def test_prob06(terrain, expected):
    assert prob06(terrain) == expected
