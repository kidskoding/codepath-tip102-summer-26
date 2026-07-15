import pytest
from prob04 import prob04


@pytest.mark.parametrize("collection, expected", [
    ([{"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
      {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
      {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}],
     5.7),
    ([{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
      {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}],
     9.15),
    ([], 0),
    # edge: single NFT -> its own value
    ([{"name": "Solo", "creator": "X", "value": 4.0}], 4.0),
])
def test_prob04(collection, expected):
    assert prob04(collection) == expected
