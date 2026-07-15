def prob05(hunny_jars: list[int]) -> int:
    # 1. Create another integer variable called sum
    # 2. Loop through your items list
        # 2.1. Update the sum variable to the current sum plus the current item in the list
    # 3. Return the final sum value

    # Time: O(n)
    # Space: O(1)

    total = 0
    for jar in hunny_jars:
        total += jar

    return total
