from prob06 import next_greater_event


def test_prob06():
    assert next_greater_event([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert next_greater_event([2, 4], [1, 2, 3, 4]) == [3, -1]
