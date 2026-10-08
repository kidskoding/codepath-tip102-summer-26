import pytest
from prob02 import prob02


@pytest.mark.parametrize("lst, expected", [
    (["na", "nana", "nanana", "batman", "!"], 4),
    (["the", "joker", "robin"], 0),
    (["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough",
      "to", "see", "yourself", "become", "the", "villain"], 9),
    ([], 0),
])
def test_prob02(lst, expected):
    assert prob02(lst) == expected
