from prob01 import Player


def make_players():
    mario = Player("Mario", "Standard", [1, 2, 1, 1, 3])
    luigi = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
    peach = Player("Peach", "Standard", [3, 3, 2, 3, 1])
    return mario, luigi, peach


def test_prob01_first():
    mario, luigi, peach = make_players()
    assert mario.get_tournament_place([luigi, peach]) == 1


def test_prob01_second():
    mario, luigi, peach = make_players()
    assert luigi.get_tournament_place([mario, peach]) == 2


def test_prob01_last():
    mario, luigi, peach = make_players()
    assert peach.get_tournament_place([mario, luigi]) == 3


def test_prob01_no_opponents():
    mario, _, _ = make_players()
    assert mario.get_tournament_place([]) == 1
