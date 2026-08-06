import pytest
from prob05 import prob05


@pytest.mark.parametrize("terminals, expected", [
    ([[1, 2], [2, 3], [4, 2]], 2),          # example
    ([[1, 2], [5, 1], [1, 3], [1, 4]], 1),  # example
    ([[1, 2], [2, 3]], 2),                  # edge: smallest star (n = 3)
    ([[7, 4], [4, 9]], 4),                  # edge: center is not the first label
])
def test_prob05(terminals, expected):
    assert prob05(terminals) == expected
