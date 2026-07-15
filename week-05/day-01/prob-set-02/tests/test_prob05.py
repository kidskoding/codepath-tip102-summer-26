from prob05 import Player


def test_prob05():
    player_one = Player("Yoshi", "Dolphin Dasher")
    assert player_one.items == []
    player_one.add_item("red shell")
    assert player_one.items == ["red shell"]
    player_one.add_item("super star")
    assert player_one.items == ["red shell", "super star"]
    player_one.add_item("super smash")
    assert player_one.items == ["red shell", "super star"]
    # duplicate valid item is added again
    player_one.add_item("red shell")
    assert player_one.items == ["red shell", "super star", "red shell"]
    # invalid item leaves list unchanged
    player_one.add_item("")
    assert player_one.items == ["red shell", "super star", "red shell"]
