from prob01 import prob01


def test_prob01():
    assert prob01([30, 45, 60, 90, 120], 105) == True
    assert prob01([15, 25, 35, 45, 55], 100) == True
    assert prob01([20, 30, 50, 70], 60) == False
