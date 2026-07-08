from prob05 import sum_honey

def test_prob05():
    assert sum_honey([2, 3, 4, 5]) == 14
    assert sum_honey([10]) == 10
    assert sum_honey([]) == 0
