from prob07 import validate_nft_actions


def test_prob07():
    assert validate_nft_actions(["add", "add", "remove", "remove"]) == True
    assert validate_nft_actions(["add", "remove", "add", "remove"]) == True
    assert validate_nft_actions(["add", "remove", "remove", "add"]) == False
