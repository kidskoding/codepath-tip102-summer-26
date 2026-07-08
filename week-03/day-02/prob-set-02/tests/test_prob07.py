from prob07 import sort_performances_by_type


def test_prob07():
    assert sort_performances_by_type([3, 1, 2, 4]) == [4, 2, 1, 3]
    assert sort_performances_by_type([0]) == [0]
