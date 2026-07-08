from prob10 import split_haycorns

def test_prob10():
    assert split_haycorns(6) == [1, 2, 3, 6]
    assert split_haycorns(1) == [1]
