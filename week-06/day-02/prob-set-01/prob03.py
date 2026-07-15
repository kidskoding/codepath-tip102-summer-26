from references import Node

def prob03(suspect_ratings: Node | None, threshold: int) -> Node | None:
    if not suspect_ratings:
        return None

    greater = gt = Node(0)
    lesser = le = Node(0)

    curr = suspect_ratings
    while curr is not None:
        if curr.value > threshold:
            gt.next = curr
            gt = gt.next
        else:
            le.next = curr
            le = le.next
        curr = curr.next

    le.next = None
    gt.next = lesser.next
    return greater.next
