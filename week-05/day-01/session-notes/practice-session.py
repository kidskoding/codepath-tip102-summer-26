from ll_demo import Node, LinkedList

"""
    UMPIRE Practice

    (U) Understand:
        input: head of a singly linked list
        output: the middle node (if even, we return second middle)
        edge cases: empty list? single --> return that, two items --> return second item

    (M) Match:
        slow and fast pointer technique

    (P) Plan:
        start both slow and fast pointers at head of linkedlist
        slow moves 1 step, while fast moves 2
        when fast reaches end, we return slow

    (I) Implement - see below

    (R) Review - run the code by examples

    (E) Evaluate - evaluate the performance of the algorithm
        Time Complexity: O(n) - we visit each node once (fast pointer walks the whole list)
        Space Complexity: O(1) - just two pointers, no matter the list size
"""

def find_middle(head):
    if head is None:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
