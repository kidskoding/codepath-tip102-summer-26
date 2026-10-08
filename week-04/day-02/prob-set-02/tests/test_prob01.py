import pytest
from prob01 import prob01


@pytest.mark.parametrize("episode_lengths, expected", [
    ([15, 45, 32, 67, 22, 59, 70], (2, 3, 2)),
    ([10, 25, 30, 45, 55, 65, 80], (2, 3, 2)),
    ([30, 30, 30, 30, 30], (0, 5, 0)),
    ([], (0, 0, 0)),
])
def test_prob01(episode_lengths, expected):
    assert prob01(episode_lengths) == expected
