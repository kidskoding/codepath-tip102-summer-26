import pytest
from prob05 import prob05


@pytest.mark.parametrize("is_connected, expected", [
    ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
    ([[1]], 1),
    ([[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1),  # 0 and 2 linked through 1
])
def test_prob05(is_connected, expected):
    assert prob05(is_connected) == expected
