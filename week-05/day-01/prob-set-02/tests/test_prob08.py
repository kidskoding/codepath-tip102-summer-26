import pytest

from references import Player
from prob08 import get_rank


def make_players():
    peach = Player("Peach", "Daytripper")
    mario = Player("Mario", "Standard Kart M", peach)
    luigi = Player("Luigi", "Super Blooper", mario)
    # lone player with no one ahead
    solo = Player("Toad", "Standard Kart T")
    # extend the chain by one
    toad = Player("Toad", "Standard Kart T", luigi)
    return {"peach": peach, "mario": mario, "luigi": luigi, "solo": solo, "toad": toad}


@pytest.mark.parametrize("key, expected", [
    ("luigi", 3),
    ("peach", 1),
    ("mario", 2),
    ("solo", 1),   # lone player with no one ahead is 1st
    ("toad", 4),   # extend the chain by one -> 4th place
])
def test_prob08(key, expected):
    assert get_rank(make_players()[key]) == expected
