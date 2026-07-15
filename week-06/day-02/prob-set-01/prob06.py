from references import Node


def prob06(head_a: Node | None, head_b: Node | None) -> Node | None:
    dummy = tail = Node(0)
    carry = 0
    curr_a = head_a
    curr_b = head_b

    while curr_a or curr_b:
        sum_a = curr_a.value if curr_a else 0
        sum_b = curr_b.value if curr_b else 0
        total = sum_a + sum_b + carry

        tail.next = Node(total % 10)
        tail = tail.next
        carry = total // 10

        curr_a = curr_a.next if curr_a else None
        curr_b = curr_b.next if curr_b else None

    if carry:
        tail.next = Node(carry)

    return dummy.next
