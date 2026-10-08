import pytest
from prob04 import prob04


@pytest.mark.parametrize("is_connected, expected", [
    ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
    ([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]], 2),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),  # no flights at all
    ([[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1),  # 0 and 2 linked through 1
    ([[1]], 1),
])
def test_prob04(is_connected, expected):
    assert prob04(is_connected) == expected
