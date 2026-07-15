import pytest
from prob03 import identify_popular_creators


@pytest.mark.parametrize("collection, expected", [
    ([{"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
      {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
      {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}],
     ['ArtByAlex']),
    ([{"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
      {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
      {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}],
     ['SpaceArt']),
    ([{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}], []),
    ([], []),  # edge: empty collection -> no creators
    # edge: a creator with 3 NFTs is still popular, listed once
    ([{"name": "A", "creator": "Zoe", "value": 1.0},
      {"name": "B", "creator": "Zoe", "value": 2.0},
      {"name": "C", "creator": "Zoe", "value": 3.0}],
     ['Zoe']),
])
def test_prob03(collection, expected):
    assert identify_popular_creators(collection) == expected
