from collections import deque

def process_nft_queue(nft_queue: list[dict[str, object]]) -> list[str]:
    if not nft_queue:
        return []

    res = []
    queue = deque()
    for nft in nft_queue:
        name = nft['name']
        queue.append(name)

    while queue:
        res.append(queue.popleft())

    return res
