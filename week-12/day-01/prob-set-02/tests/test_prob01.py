import pytest
from prob01 import prob01


@pytest.mark.parametrize("n, expected", [
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2]),
    (10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]),
    (0, [0]),
])
def test_prob01(n, expected):
    assert prob01(n) == expected
