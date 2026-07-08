from prob01 import is_valid_post_format

def test_prob01():
    assert is_valid_post_format("()") == True
    assert is_valid_post_format("()[]{}") == True
    assert is_valid_post_format("(]") == False
