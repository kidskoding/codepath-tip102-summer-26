import pytest
from prob06 import prob06


@pytest.mark.parametrize("raised_species, target_species, expected", [
    ("abcba", "abc", 1),
    ("aaaaabbbbcc", "abc", 2),
    ("xyz", "abc", 0),
])
def test_prob06(raised_species, target_species, expected):
    assert prob06(raised_species, target_species) == expected
