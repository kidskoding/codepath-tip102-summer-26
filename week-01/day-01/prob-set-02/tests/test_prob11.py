from prob11 import running_sum

def test_prob11():
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert running_sum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
