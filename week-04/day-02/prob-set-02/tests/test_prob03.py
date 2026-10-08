import pytest
from prob03 import prob03


@pytest.mark.parametrize("episode_lengths, expected", [
    ([30, 45, 30, 60, 45, 30], 30),
    ([20, 20, 30, 30, 40, 40, 40], 40),
    ([50, 60, 70, 80, 90, 100], 50),  # all tie: smallest wins
    ([45], 45),
])
def test_prob03(episode_lengths, expected):
    assert prob03(episode_lengths) == expected
