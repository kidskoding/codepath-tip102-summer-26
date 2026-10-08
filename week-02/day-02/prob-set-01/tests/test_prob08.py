import pytest
from prob08 import prob08


@pytest.mark.parametrize("species_pairs, expected", [
    ([[1, 2], [2, 1], [3, 4], [5, 6]], 1),
    ([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]], 3),
    ([], 0),
])
def test_prob08(species_pairs, expected):
    assert prob08(species_pairs) == expected
