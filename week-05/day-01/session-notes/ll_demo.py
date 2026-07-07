from __future__ import annotations


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next: Node | None = None

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def add(self, val: int):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

linked_list = LinkedList()
for val in [1, 2, 3, 4, 5]:
    linked_list.add(val)
