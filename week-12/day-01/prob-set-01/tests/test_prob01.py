import pytest
from prob01 import prob01


@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 1),
    (5, 5),
    (7, 13),
    (3, 2),
    (10, 55),
])
def test_prob01(n, expected):
    assert prob01(n) == expected
