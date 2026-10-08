import pytest
from prob05 import prob05


@pytest.mark.parametrize("species_populations, expected", [
    ([4, 1, 4, 0, 3, 5], 2),
    ([1, 100], 1),
    ([2, 2], 1),
])
def test_prob05(species_populations, expected):
    assert prob05(species_populations) == expected
