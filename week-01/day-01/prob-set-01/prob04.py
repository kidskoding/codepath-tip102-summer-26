def prob04(items: list[str], x: int) -> str | None:
    # 1. Loop through your items list
    # 2. If the index is found (equal to x), simply return that element/item
    # 3. If the index is not found, return None

    # Time: O(n)
    # Space: O(1)

    for i, item in enumerate(items):
        if i == x:
            return item

    return None
