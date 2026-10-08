from prob01 import Villager


def make_town():
    names = ["Bob", "Marshal", "Ankha", "Fauna", "Raymond", "Stitches"]
    return {n: Villager(n, "Cat", "hi") for n in names}


def test_prob01_mutuals():
    t = make_town()
    t["Bob"].friends = [t["Stitches"], t["Raymond"], t["Fauna"]]
    t["Marshal"].friends = [t["Raymond"], t["Ankha"], t["Fauna"]]
    assert sorted(t["Bob"].get_mutuals(t["Marshal"])) == ["Fauna", "Raymond"]


def test_prob01_no_mutuals():
    t = make_town()
    t["Bob"].friends = [t["Stitches"], t["Raymond"], t["Fauna"]]
    t["Ankha"].friends = [t["Marshal"]]
    assert t["Bob"].get_mutuals(t["Ankha"]) == []


def test_prob01_no_friends():
    t = make_town()
    assert t["Bob"].get_mutuals(t["Marshal"]) == []
