from prob07 import prob07


def test_prob07():
    assert prob07(["WeWork", "Regus", "Spaces", "WeWork", "Regus", "WeWork"]) == ['WeWork']
    assert prob07(["IndieDesk", "Spaces", "IndieDesk", "WeWork", "Spaces",
                   "IndieDesk", "WeWork"]) == ['IndieDesk']
    assert prob07(["Hub", "Regus", "WeWork", "Hub", "WeWork", "Regus", "Hub",
                   "Regus"]) == ['Hub', 'Regus']
