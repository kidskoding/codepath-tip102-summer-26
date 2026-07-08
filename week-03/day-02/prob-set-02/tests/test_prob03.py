from prob03 import collect_festival_points


def test_prob03():
    assert collect_festival_points([5, 8, 3, 10]) == 26
    assert collect_festival_points([2, 7, 4, 6]) == 19
    assert collect_festival_points([1, 5, 9, 2, 8]) == 25
