import pytest
from prob06 import prob06


@pytest.mark.parametrize("tasks, capacity, expected", [
    ([5, 10, 7, 8], 20, 3),
    ([2, 4, 6, 3, 1], 10, 4),
    ([8, 5, 3, 2, 7], 15, 3),
    ([], 10, 0),      # no tasks
    ([5], 10, 1),     # single task that fits
    ([20], 10, 0),    # single task that doesn't fit
])
def test_prob06(tasks, capacity, expected):
    assert prob06(tasks, capacity) == expected
