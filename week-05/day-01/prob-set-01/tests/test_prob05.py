from prob05 import Villager


def test_prob05():
    alice = Villager("Alice", "Koala", "guvnor")
    assert alice.furniture == []
    alice.add_item("acoustic guitar")
    assert alice.furniture == ["acoustic guitar"]
    alice.add_item("cacao tree")
    assert alice.furniture == ["acoustic guitar", "cacao tree"]
    alice.add_item("nintendo switch")
    assert alice.furniture == ["acoustic guitar", "cacao tree"]

    # duplicates of a valid item are both added (no dedup in spec)
    bob = Villager("Bob", "Cat", "pthhhpth")
    assert bob.furniture == []
    bob.add_item("kotatsu")
    bob.add_item("kotatsu")
    assert bob.furniture == ["kotatsu", "kotatsu"]
