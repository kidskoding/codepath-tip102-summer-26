from prob05 import prob05


def test_prob05():
    assert prob05("<div><p></p></div>") == True
    assert prob05("<div><p></div></p>") == False
    assert prob05("<div><p><a></a></p></div>") == True
    assert prob05("<div><p></a></p></div>") == False
