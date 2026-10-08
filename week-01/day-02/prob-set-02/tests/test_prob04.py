import pytest
from prob04 import prob04


@pytest.mark.parametrize("n, expected", [
    (964, 3),
    (0, 1),
    (7, 1),
    (10, 2),
])
def test_prob04(n, expected):
    assert prob04(n) == expected
