from prob06 import process_nft_queue


def test_prob06():
    assert process_nft_queue([{"name": "Abstract Horizon", "processing_time": 2},
                              {"name": "Pixel Dreams", "processing_time": 3},
                              {"name": "Urban Jungle", "processing_time": 1}]) == ['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']
    assert process_nft_queue([{"name": "Golden Hour", "processing_time": 4},
                              {"name": "Sunset Serenade", "processing_time": 2},
                              {"name": "Ocean Waves", "processing_time": 3}]) == ['Golden Hour', 'Sunset Serenade', 'Ocean Waves']
    assert process_nft_queue([{"name": "Crypto Kitty", "processing_time": 5},
                              {"name": "Galactic Voyage", "processing_time": 6}]) == ['Crypto Kitty', 'Galactic Voyage']
