from prob11 import tiggerfy

def test_prob11():
    assert tiggerfy("suspicerous") == "suspcous"
    assert tiggerfy("Trigger") == ""
    assert tiggerfy("Hunny") == "Hunny"
