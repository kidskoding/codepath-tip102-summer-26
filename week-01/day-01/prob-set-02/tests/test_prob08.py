from prob08 import find_villain

def test_prob08():
    crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
    assert find_villain(crowd, 'The Joker') == [1, 4, 6]
