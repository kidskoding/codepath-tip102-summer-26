import pytest
from prob05 import prob05


@pytest.mark.parametrize("track1, track2, expected", [
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    ([10, 20], [15, 30], [10, 15, 20, 30]),
    ([], [1, 2], [1, 2]),
    ([], [], []),
])
def test_prob05(track1, track2, expected):
    assert prob05(track1, track2) == expected
