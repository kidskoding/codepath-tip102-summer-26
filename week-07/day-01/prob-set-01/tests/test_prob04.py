import pytest
from prob04 import prob04


@pytest.mark.parametrize("n, expected", [
    (5, 5),    # example
    (8, 21),   # example
    (0, 0),    # base case
    (1, 1),    # base case
])
def test_prob04(n, expected):
    assert prob04(n) == expected
