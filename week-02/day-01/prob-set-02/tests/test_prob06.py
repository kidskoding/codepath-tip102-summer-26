import pytest
from prob06 import prob06


@pytest.mark.parametrize("transmission, expected", [
    ("thequickbrownfoxjumpsoverthelazydog", True),
    ("spacetravel", False),
    ("", False),
    ("abcdefghijklmnopqrstuvwxyz", True),
])
def test_prob06(transmission, expected):
    assert prob06(transmission) == expected
