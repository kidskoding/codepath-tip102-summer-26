from prob07 import count_less_than

def test_prob07():
    assert count_less_than([1, 2, 3, 4, 5, 6], 4) == 3
    assert count_less_than([], 4) == 0
