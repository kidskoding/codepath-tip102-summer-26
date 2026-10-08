import pytest
from prob02 import prob02


@pytest.mark.parametrize("endangered_species, observed_species, expected", [
    ("aA", "aAAbbbb", 3),
    ("z", "ZZ", 0),
    ("abc", "", 0),
])
def test_prob02(endangered_species, observed_species, expected):
    assert prob02(endangered_species, observed_species) == expected
