import pytest
from prob01 import prob01


@pytest.mark.parametrize("costs, expected", [
    ([8, 4, 6, 2, 3], [4, 2, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([10, 1, 1, 6], [9, 0, 1, 6]),
    ([], []),
    ([7], [7]),
])
def test_prob01(costs, expected):
    assert prob01(costs) == expected
