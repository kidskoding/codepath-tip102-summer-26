from prob04 import average_nft_value


def test_prob04():
    assert average_nft_value([{"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
                              {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
                              {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}]) == 5.7
    assert average_nft_value([{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
                              {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}]) == 9.15
    assert average_nft_value([]) == 0
