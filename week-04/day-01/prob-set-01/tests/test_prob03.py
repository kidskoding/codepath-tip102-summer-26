from prob03 import identify_popular_creators


def test_prob03():
    assert identify_popular_creators([{"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
                                      {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
                                      {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}]) == ['ArtByAlex']
    assert identify_popular_creators([{"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
                                      {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
                                      {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}]) == ['SpaceArt']
    assert identify_popular_creators([{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}]) == []
