from prob09 import get_odds

def test_prob09():
    assert get_odds([1, 2, 3, 4]) == [1, 3]
    assert get_odds([2, 4, 6, 8]) == []
