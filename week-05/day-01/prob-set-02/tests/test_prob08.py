from references import Player
from prob08 import get_rank


def test_prob08():
    peach = Player("Peach", "Daytripper")
    mario = Player("Mario", "Standard Kart M", peach)
    luigi = Player("Luigi", "Super Blooper", mario)
    assert get_rank(luigi) == 3
    assert get_rank(peach) == 1
    assert get_rank(mario) == 2
