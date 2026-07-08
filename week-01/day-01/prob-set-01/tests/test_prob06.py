from prob06 import doubled

def test_prob06():
    assert doubled([1, 2, 3]) == [1, 2, 3, 1, 2, 3]
    assert doubled([]) == []
