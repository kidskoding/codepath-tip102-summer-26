import pytest
from prob10 import up_and_down

@pytest.mark.parametrize("arg, expected", [
    ([1, 2, 3], 1),
    ([1, 3, 5], 3),
    ([2, 4, 10, 2], -4),
    ([], 0),
    ([7], 1),
    ([8], -1),
])
def test_prob10(arg, expected):
    assert up_and_down(arg) == expected
