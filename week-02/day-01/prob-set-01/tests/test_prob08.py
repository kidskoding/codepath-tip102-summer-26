import pytest
from prob08 import prob08


@pytest.mark.parametrize("popularity_scores, expected", [
    ([1, 2, 3, 1, 1, 3], 4),
    ([1, 1, 1, 1], 6),
    ([1, 2, 3], 0),
    ([], 0),
])
def test_prob08(popularity_scores, expected):
    assert prob08(popularity_scores) == expected
