import pytest
from prob04 import fibonacci_growth


@pytest.mark.parametrize("n, expected", [
    (5, 5),    # example
    (8, 21),   # example
    (0, 0),    # base case
    (1, 1),    # base case
])
def test_prob04(n, expected):
    assert fibonacci_growth(n) == expected
