import pytest
from prob09 import prob09


@pytest.mark.parametrize("signals1, signals2, expected", [
    ([2, 3, 2], [1, 2], [2, 1]),
    ([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6], [3, 4]),
    ([3, 4, 2, 3], [1, 5], [0, 0]),
    ([], [1], [0, 0]),
])
def test_prob09(signals1, signals2, expected):
    assert prob09(signals1, signals2) == expected
