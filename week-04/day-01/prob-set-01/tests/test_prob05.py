import pytest
from prob05 import search_nft_by_tag


@pytest.mark.parametrize("collections, tag, expected", [
    ([[{"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
       {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}],
      [{"name": "Urban Jungle", "tags": ["urban", "landscape"]},
       {"name": "City Lights", "tags": ["modern", "landscape"]}]],
     "landscape", ['Urban Jungle', 'City Lights']),
    ([[{"name": "Golden Hour", "tags": ["sunset", "landscape"]},
       {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}],
      [{"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}]],
     "sunset", ['Golden Hour', 'Sunset Serenade']),
    ([[{"name": "The Last Piece", "tags": ["finale", "abstract"]}],
      [{"name": "Ocean Waves", "tags": ["seascape", "calm"]},
       {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}]],
     "modern", []),
    ([], "landscape", []),  # edge: no collections at all
])
def test_prob05(collections, tag, expected):
    assert search_nft_by_tag(collections, tag) == expected
