import pytest
from prob01 import prob01


@pytest.mark.parametrize("tasks, target, expected", [
    ([30, 45, 60, 90, 120], 105, True),
    ([15, 25, 35, 45, 55], 100, True),
    ([20, 30, 50, 70], 60, False),
    ([], 100, False),          # empty: no pair possible
    ([50], 100, False),        # single element can't form a pair
    ([50, 50], 100, True),     # two distinct equal-value tasks sum to target
])
def test_prob01(tasks, target, expected):
    assert prob01(tasks, target) == expected
