import pytest
from prob11 import prob11

@pytest.mark.parametrize("arg, expected", [
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    ([5], [5]),
    ([], []),
])
def test_prob11(arg, expected):
    assert prob11(arg) == expected
