from prob04 import Villager


def test_prob04():
    alice = Villager("Alice", "Koala", "guvnor")
    alice.set_catchphrase("sweet dreams")
    assert alice.catchphrase == "sweet dreams"
    alice.set_catchphrase("#?!")
    assert alice.catchphrase == "sweet dreams"
    # 19 chars, only letters + whitespace -> valid (length < 20)
    alice.set_catchphrase("a" * 19)
    assert alice.catchphrase == "a" * 19
    # exactly 20 chars -> invalid (not less than 20), unchanged
    alice.set_catchphrase("b" * 20)
    assert alice.catchphrase == "a" * 19
    # contains a digit -> invalid, unchanged
    alice.set_catchphrase("hello2you")
    assert alice.catchphrase == "a" * 19
