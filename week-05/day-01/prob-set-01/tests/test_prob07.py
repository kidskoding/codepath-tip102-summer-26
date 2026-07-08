from references import Villager
from prob07 import of_personality_type


def test_prob07():
    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
    stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")
    assert of_personality_type([isabelle, bob, stitches], "Lazy") == ["Bob", "Stitches"]
    assert of_personality_type([isabelle, bob, stitches], "Cranky") == []
