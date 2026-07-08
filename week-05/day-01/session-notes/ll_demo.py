from __future__ import annotations   # lets a method reference its own class in type hints


# A LINKED LIST is a chain of Nodes. Each Node holds a value and a POINTER to
# the next Node. Unlike an array, items aren't in contiguous memory — you can
# only reach an item by walking the chain from the head. No random indexing.

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next: Node | None = None   # points to the next Node; None = end of chain.

class LinkedList:
    def __init__(self):
        self.head: Node | None = None   # the entry point. None = empty list.

    def add(self, val: int):
        new_node = Node(val)

        if not self.head:               # EDGE CASE: empty list — the new node
            self.head = new_node        # becomes the head, and we're done.
            return

        # TRAVERSAL PATTERN: to append at the end, we must first FIND the end.
        # Walk curr forward until curr.next is None (the last node).
        curr = self.head
        while curr.next:                # stop when there's no next node.
            curr = curr.next
        # curr is now the last node...
        curr.next = new_node            # ...so hook the new node on behind it.
        # NOTE: this add is O(n) — we walk the whole list every time. Keeping a
        # `tail` pointer would make it O(1); good to know the trade-off.

linked_list = LinkedList()
for val in [1, 2, 3, 4, 5]:
    linked_list.add(val)
# Result: head -> 1 -> 2 -> 3 -> 4 -> 5 -> None
