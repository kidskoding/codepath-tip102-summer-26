from prob12 import locate_thistles

def test_prob12():
    assert locate_thistles(
        ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
    ) == [0, 3]
    assert locate_thistles(["book", "bouncy ball", "leaf", "red balloon"]) == []
