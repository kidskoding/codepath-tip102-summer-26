import pytest
from references import Villager
from prob07 import prob07

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")


@pytest.mark.parametrize("townies, personality, expected", [
    ([isabelle, bob, stitches], "Lazy", ["Bob", "Stitches"]),
    ([isabelle, bob, stitches], "Cranky", []),
    ([], "Lazy", []),                    # empty townies list -> no names
    ([isabelle], "Normal", ["Isabelle"]),  # single villager that matches
])
def test_prob07(townies, personality, expected):
    assert prob07(townies, personality) == expected
