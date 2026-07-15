import pytest
from references import Villager
from prob08 import message_received

kk_slider = Villager("K.K. Slider", "Dog", "Normal", "ba ba")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes yes", kk_slider)
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?", tom_nook)
rover = Villager("Rover", "Cat", "Normal", "meow")


@pytest.mark.parametrize("start, target, expected", [
    (isabelle, kk_slider, True),
    (kk_slider, isabelle, False),
    (isabelle, tom_nook, True),   # direct neighbor -> reachable in one hop
    (isabelle, rover, False),     # target not in the chain -> unreachable
])
def test_prob08(start, target, expected):
    assert message_received(start, target) == expected
