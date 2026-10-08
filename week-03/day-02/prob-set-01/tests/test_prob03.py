import pytest
from prob03 import prob03


@pytest.mark.parametrize("points, expected", [
    ([5, 8, 3, 10], 26),
    ([2, 7, 4, 6], 19),
    ([1, 5, 9, 2, 8], 25),
    ([], 0),
    ([7], 7),
])
def test_prob03(points, expected):
    assert prob03(points) == expected
