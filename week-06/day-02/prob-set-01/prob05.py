from references import Node

def prob05(evidence: Node | None, k: int) -> Node | None:
    if not evidence or not evidence.next:
        return evidence  # 0 or 1 node: nothing to rotate

    n = 1
    tail = evidence
    while tail.next is not None:
        tail = tail.next
        n += 1

    k %= n
    if k == 0:
        return evidence

    tail.next = evidence
    new_tail = evidence
    for _ in range(n - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head
