import copy

import pytest
from prob05 import prob05


@pytest.mark.parametrize("city, expected", [
    ([[4, 3], [1, 2]], 4),
    ([[1, 2, 18, 3], [26, 6, 7, 15], [9, 10, 17, 18], [14, 15, 16, 22]], 9),
    ([[7]], 1),
    ([[1, 1]], 1),  # equal neighbors are not strictly decreasing
])
def test_prob05(city, expected):
    assert prob05(copy.deepcopy(city)) == expected
