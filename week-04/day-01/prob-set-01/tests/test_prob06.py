import pytest
from prob06 import process_nft_queue


@pytest.mark.parametrize("queue, expected", [
    ([{"name": "Abstract Horizon", "processing_time": 2},
      {"name": "Pixel Dreams", "processing_time": 3},
      {"name": "Urban Jungle", "processing_time": 1}],
     ['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']),
    ([{"name": "Golden Hour", "processing_time": 4},
      {"name": "Sunset Serenade", "processing_time": 2},
      {"name": "Ocean Waves", "processing_time": 3}],
     ['Golden Hour', 'Sunset Serenade', 'Ocean Waves']),
    ([{"name": "Crypto Kitty", "processing_time": 5},
      {"name": "Galactic Voyage", "processing_time": 6}],
     ['Crypto Kitty', 'Galactic Voyage']),
    ([], []),  # edge: empty queue
    # edge: single NFT
    ([{"name": "Solo", "processing_time": 1}], ['Solo']),
])
def test_prob06(queue, expected):
    assert process_nft_queue(queue) == expected
