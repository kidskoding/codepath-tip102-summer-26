import pytest
from prob05 import prob05


@pytest.mark.parametrize("episodes, threshold, expected", [
    ([("Episode 1", "Tech", 30), ("Episode 2", "Health", 45), ("Episode 3", "Tech", 35),
      ("Episode 4", "Entertainment", 60)], 30, ["Entertainment", "Health", "Tech"]),
    ([("Episode A", "Science", 40), ("Episode B", "Science", 50), ("Episode C", "Art", 25),
      ("Episode D", "Art", 30)], 30, ["Art", "Science"]),
    ([("Episode X", "Music", 20), ("Episode Y", "Music", 15), ("Episode Z", "Drama", 25)], 20, ["Drama", "Music"]),
    ([("Episode X", "Music", 10)], 20, []),
    ([], 20, []),
])
def test_prob05(episodes, threshold, expected):
    assert prob05(episodes, threshold) == expected
