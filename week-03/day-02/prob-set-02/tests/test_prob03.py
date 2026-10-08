import pytest
from prob03 import prob03


# any valid sequence is accepted: a permutation of 0..n that follows every I/D
@pytest.mark.parametrize("terrain", ["IDID", "III", "DDI", "D", ""])
def test_prob03(terrain):
    result = prob03(terrain)
    assert sorted(result) == list(range(len(terrain) + 1))
    for i, step in enumerate(terrain):
        if step == "I":
            assert result[i] < result[i + 1]
        else:
            assert result[i] > result[i + 1]
