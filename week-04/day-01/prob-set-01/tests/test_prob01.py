import pytest
from prob01 import extract_nft_names


@pytest.mark.parametrize("collection, expected", [
    ([{"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
      {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
      {"name": "Future City", "creator": "UrbanArt", "value": 3.8}],
     ['Abstract Horizon', 'Pixel Dreams', 'Future City']),
    ([{"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
      {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}],
     ['Crypto Kitty', 'Galactic Voyage']),
    ([{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}],
     ['Golden Hour']),
    ([], []),  # edge: empty collection
])
def test_prob01(collection, expected):
    assert extract_nft_names(collection) == expected
