from references import Node

# Time: O(n) - at the worst case have to go through every node in the LinkedList 
# Space: O(1) - only storing constant variables, therefore constant space
def prob01(clues: Node | None) -> bool:
    if clues is None:
        return False

    curr = clues
    while curr.next is not None and curr.next != clues:
        curr = curr.next
        
    return curr.next == clues
