import pytest
from prob06 import prob06


@pytest.mark.parametrize("episodes, n, expected", [
    (["episode1", "episode2", "episode3", "episode4"], 3, ["episode4", "episode3", "episode2"]),
    (["ep1", "ep2", "ep3"], 2, ["ep3", "ep2"]),
    (["a", "b", "c", "d"], 5, ["d", "c", "b", "a"]),
    (["a", "b"], 0, []),
    ([], 3, []),
])
def test_prob06(episodes, n, expected):
    assert prob06(episodes, n) == expected
