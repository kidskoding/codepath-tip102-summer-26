from prob08 import find_closest_nft_values


def test_prob08():
    assert find_closest_nft_values([3.5, 5.4, 7.2, 9.0, 10.5], 8.0) == (7.2, 9.0)
    assert find_closest_nft_values([2.0, 4.5, 6.3, 7.8, 12.1], 6.5) == (6.3, 7.8)
    assert find_closest_nft_values([1.0, 2.5, 4.0, 6.0, 9.0], 3.0) == (2.5, 4.0)
