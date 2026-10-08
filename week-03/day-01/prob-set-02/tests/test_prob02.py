import pytest
from prob02 import prob02


@pytest.mark.parametrize("watchlist, expected", [
    (["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"],
     ["The Witcher", "The Crown", "Stranger Things", "Breaking Bad"]),
    (["The Crown"], ["The Crown"]),
    ([], []),
])
def test_prob02(watchlist, expected):
    result = prob02(watchlist)
    assert result == expected
    assert watchlist == expected  # must reverse in place
