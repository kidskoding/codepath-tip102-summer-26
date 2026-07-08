from references import Node


def prob06(song_audio: Node | None):
    if not song_audio or not song_audio.next or not song_audio.next.next:
        return 0

    prev = song_audio.value
    current = song_audio.next
    count = 0

    while current and current.next:
        if (current.value > prev and current.value > current.next.value) or (current.value < prev and current.value < current.next.value):
            count += 1

        prev = current.value
        current = current.next

    return count
