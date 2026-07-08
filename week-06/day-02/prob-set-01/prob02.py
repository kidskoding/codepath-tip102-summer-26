from references import Node

# Time: O(n + k) ~ O(n) - each node is walked at a maximum of n times, where n is the number of nodes in the evidence linked list
#                       - then each node is traversed a constant number of k times, where k represents the number of nodes in the cycle
# Space: O(k) - only the res list, where k = number of nodes in the cycle
def prob02(evidence: Node | None):
    slow = evidence
    fast = evidence
    has_cycle = False

    while fast and fast.next and not has_cycle:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True

    if not has_cycle:
        return []

    curr = slow.next
    res = [slow.value]
    while curr != slow:
        res.append(curr.value)
        curr = curr.next

    return res
