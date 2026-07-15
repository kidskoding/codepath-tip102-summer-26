import pytest
from prob05 import prob05


@pytest.mark.parametrize("depths, expected", [
    ([5, 7, 2, 8, 3], 2),      # example
    ([12, 15, 10, 21], 10),    # example
    ([7], 7),                  # single element
    ([3, 1, 1], 1),            # duplicated minimum
])
def test_prob05(depths, expected):
    assert prob05(depths) == expected
