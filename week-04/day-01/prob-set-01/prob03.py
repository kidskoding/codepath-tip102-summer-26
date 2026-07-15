# Time: O(n)
# Space: O(n)

def prob03(nft_collection):
    if not nft_collection or len(nft_collection) == 1:
        return []

    frequencies = {}
    for collection in nft_collection:
        frequencies[collection['creator']] = frequencies.get(collection['creator'], 0) + 1

    popular_nft_creators = []
    for key, value in frequencies.items():
        if value > 1:
            popular_nft_creators.append(key)

    return popular_nft_creators
