def prob03(rooms):
    low, high = 0, len(rooms)
    while low < high:
        mid = (low + high) // 2
        if rooms[mid] == 1:
            high = mid
        else:
            low = mid + 1

    return len(rooms) - low
