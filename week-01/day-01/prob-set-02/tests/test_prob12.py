from prob12 import shuffle

def test_prob12():
    assert shuffle(['Joker', 'Queen', 2, 3, 'Ace', 7]) == ['Joker', 3, 'Queen', 'Ace', 2, 7]
    assert shuffle([9, 2, 3, 'Joker', 'Joker', 3, 2, 9]) == [9, 'Joker', 2, 3, 3, 2, 'Joker', 9]
    assert shuffle([10, 10, 2, 2]) == [10, 2, 10, 2]
