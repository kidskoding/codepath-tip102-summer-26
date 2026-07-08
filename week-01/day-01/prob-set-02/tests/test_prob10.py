from prob10 import up_and_down

def test_prob10():
    assert up_and_down([1, 2, 3]) == 1
    assert up_and_down([1, 3, 5]) == 3
    assert up_and_down([2, 4, 10, 2]) == -4
