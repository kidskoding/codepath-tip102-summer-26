import pytest
from prob04 import is_profitable


@pytest.mark.parametrize("excursion_counts, expected", [
    ([3, 5], 2),    # example: 2 values >= 2
    ([0, 0], -1),   # example: no valid x
    ([5], 1),       # one value >= 1  -> x = 1
])
def test_prob04(excursion_counts, expected):
    assert is_profitable(excursion_counts) == expected
