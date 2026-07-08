from prob03 import is_symmetrical_title

def test_prob03():
    assert is_symmetrical_title("A Santa at NASA") == True
    assert is_symmetrical_title("Social Media") == False
