from prob09 import can_pair

def test_prob09():
    assert can_pair([2, 4, 6, 8]) == True
    assert can_pair([1, 2, 3, 4]) == False
    assert can_pair([]) == True
