def prob06(song_audio):
    if not song_audio or (song_audio.next and song_audio.next.next):
        return 0

    prev = song_audio.value
    current = song_audio.next
    count = 0

    while current.next:
        if (current.value > prev and current.value > current.next.value) or (current.value < prev and current.value < current.next.value):
            count += 1

        prev = current.value
        current = current.next

    return count
