import pytest
from prob05 import prob05


@pytest.mark.parametrize("tokens, amount, expected", [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1, 3, 4], 6, 2),  # 3 + 3 beats greedy 4 + 1 + 1
])
def test_prob05(tokens, amount, expected):
    assert prob05(tokens, amount) == expected
