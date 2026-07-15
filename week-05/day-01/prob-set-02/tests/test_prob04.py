from prob04 import Player


def test_prob04():
    player_three = Player("Donkey Kong", "Standard Kart")
    player_three.set_character("Peach")
    assert player_three.character == "Peach"
    player_three.set_character("Baby Peach")
    assert player_three.character == "Peach"
    # another valid name updates
    player_three.set_character("Bowser")
    assert player_three.character == "Bowser"
    # empty string is invalid, character unchanged
    player_three.set_character("")
    assert player_three.character == "Bowser"
