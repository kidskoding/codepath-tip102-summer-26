import pytest
from prob10 import prob10


@pytest.mark.parametrize("trust, n, expected", [
    ([[1, 2]], 2, 2),
    ([[1, 3], [2, 3]], 3, 3),
    ([[1, 3], [2, 3], [3, 1]], 3, -1),
    ([], 1, 1),
])
def test_prob10(trust, n, expected):
    assert prob10(trust, n) == expected
