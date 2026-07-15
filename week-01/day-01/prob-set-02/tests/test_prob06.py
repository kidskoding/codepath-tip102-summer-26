import pytest
from prob06 import squared

@pytest.mark.parametrize("arg, expected", [
    ([1, 2, 3], [1, 4, 9]),
    ([], []),
    ([5], [25]),
    ([-3], [9]),
])
def test_prob06(arg, expected):
    assert squared(arg) == expected
