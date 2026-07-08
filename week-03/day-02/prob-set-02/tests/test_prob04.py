from prob04 import booth_navigation


def test_prob04():
    assert booth_navigation([1, 2, "back", 3, 4]) == [1, 3, 4]
    assert booth_navigation([5, 3, 2, "back", "back", 7]) == [5, 7]
    assert booth_navigation([1, "back", 2, "back", "back", 3]) == [3]
