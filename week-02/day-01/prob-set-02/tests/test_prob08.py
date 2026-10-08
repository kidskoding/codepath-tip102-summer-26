import pytest
from prob08 import prob08


# each inner list may come back in any order, so compare sorted
@pytest.mark.parametrize("signals1, signals2, expected", [
    ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
    ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
    ([], [], [[], []]),
])
def test_prob08(signals1, signals2, expected):
    result = prob08(signals1, signals2)
    assert len(result) == 2
    assert sorted(result[0]) == expected[0]
    assert sorted(result[1]) == expected[1]
