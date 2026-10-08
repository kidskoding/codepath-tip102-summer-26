class Node:
    # Superset: doubly linked list problems add a `prev` link; singly linked
    # code just leaves it as None.
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
