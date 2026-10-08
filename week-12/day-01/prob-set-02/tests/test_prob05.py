import pytest
from prob05 import prob05


@pytest.mark.parametrize("pokeballs, expected", [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([5], 5),
    ([2, 1, 1, 2], 4),  # best picks are not every other center
    ([], 0),
])
def test_prob05(pokeballs, expected):
    assert prob05(pokeballs) == expected
