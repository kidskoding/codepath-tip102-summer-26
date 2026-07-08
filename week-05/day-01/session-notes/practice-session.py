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

# FAST & SLOW POINTERS (a.k.a. "tortoise and hare"): fast moves 2x slow's speed,
# so when fast reaches the end, slow is exactly halfway. One pass, no length count.
def find_middle(head):
    if head is None:        # EDGE CASE: empty list has no middle.
        return None

    slow = head
    fast = head

    # Loop guard needs BOTH checks: `fast` covers odd-length lists (fast lands
    # exactly on the last node), `fast.next` covers even-length (fast steps past).
    # Checking fast.next.next without them would crash on None.
    while fast and fast.next:
        slow = slow.next            # +1 step
        fast = fast.next.next       # +2 steps

    return slow
    # Trace 1 -> 2 -> 3 -> 4 -> 5:
    #   start: slow=1, fast=1
    #   step:  slow=2, fast=3
    #   step:  slow=3, fast=5   (fast.next is None -> loop stops)
    #   return slow=3  ✔ the middle
    # Trace even 1 -> 2 -> 3 -> 4:  ends slow=3 -> returns SECOND middle, as specified.
