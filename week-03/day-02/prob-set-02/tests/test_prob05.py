import pytest
from prob05 import prob05


@pytest.mark.parametrize("explorers, supplies, expected", [
    ([1, 1, 0, 0], [0, 1, 0, 1], 0),
    ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3),
    ([0], [1], 1),
])
def test_prob05(explorers, supplies, expected):
    assert prob05(explorers, supplies) == expected
