import pytest
from prob04 import prob04


@pytest.mark.parametrize("group_sizes, room_capacity, expected", [
    ([1, 20, 10, 14, 3, 5, 4, 2], 12, 11),
    ([10, 20, 30], 15, -1),
    ([5, 5], 11, 10),  # two groups of the same size still count as distinct groups
    ([5, 5], 10, -1),  # sum must be strictly less than capacity
    ([5], 100, -1),
])
def test_prob04(group_sizes, room_capacity, expected):
    assert prob04(group_sizes, room_capacity) == expected
