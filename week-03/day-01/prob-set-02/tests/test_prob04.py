import pytest
from prob04 import prob04


@pytest.mark.parametrize("view_counts, expected", [
    ([7, 8, 3, 4, 15, 13, 4, 1], 5.5),
    ([1, 9, 8, 3, 10, 5], 5.5),
    ([1, 2, 3, 7, 8, 9], 5.0),
    ([2, 4], 3.0),
])
def test_prob04(view_counts, expected):
    assert prob04(view_counts) == expected
