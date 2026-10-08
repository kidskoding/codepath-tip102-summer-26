import pytest
from prob05 import prob05


@pytest.mark.parametrize("lst, expected", [
    ([1, 0, 2, 0, 3, 0], [1, 2, 3, 0, 0, 0]),
    ([], []),
    ([0, 0], [0, 0]),
    ([0, 1], [1, 0]),
])
def test_prob05(lst, expected):
    assert prob05(lst) == expected
