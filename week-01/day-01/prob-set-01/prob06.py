def prob06(hunny_jars: list[int]) -> list[int]:
    # Multiply EACH element by 2 (not the list by 2 — that would concatenate).
    # Time: O(n) — one pass building the new list.
    # Space: O(n) — the returned list holds n prob06 values.

    return [jar * 2 for jar in hunny_jars]
