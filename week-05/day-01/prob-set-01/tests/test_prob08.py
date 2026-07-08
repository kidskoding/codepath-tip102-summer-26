from references import Villager
from prob08 import message_received


def test_prob08():
    kk_slider = Villager("K.K. Slider", "Dog", "Normal", "ba ba")
    tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes yes", kk_slider)
    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?", tom_nook)
    assert message_received(isabelle, kk_slider) == True
    assert message_received(kk_slider, isabelle) == False
