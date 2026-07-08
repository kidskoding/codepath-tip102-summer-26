from prob04 import get_items

def test_prob04():
    items = ["piglet", "pooh", "roo", "rabbit"]

    assert get_items(items, 0) == "piglet"
    assert get_items(items, 2) == "roo"
    assert get_items(items, 3) == "rabbit"

    assert get_items(["piglet", "pooh", "roo", "rabbit"], 10) is None
    assert get_items([], 0) is None
