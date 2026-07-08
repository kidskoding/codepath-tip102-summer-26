from prob05 import search_nft_by_tag


def test_prob05():
    assert search_nft_by_tag([[{"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
                               {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}],
                              [{"name": "Urban Jungle", "tags": ["urban", "landscape"]},
                               {"name": "City Lights", "tags": ["modern", "landscape"]}]], "landscape") == ['Urban Jungle', 'City Lights']
    assert search_nft_by_tag([[{"name": "Golden Hour", "tags": ["sunset", "landscape"]},
                               {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}],
                              [{"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}]], "sunset") == ['Golden Hour', 'Sunset Serenade']
    assert search_nft_by_tag([[{"name": "The Last Piece", "tags": ["finale", "abstract"]}],
                              [{"name": "Ocean Waves", "tags": ["seascape", "calm"]},
                               {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}]], "modern") == []
