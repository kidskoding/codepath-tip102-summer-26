from references import Node


def prob04(playlist_head: Node) -> bool:
    if not playlist_head:
        return False 

    slow = playlist_head
    fast = playlist_head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
