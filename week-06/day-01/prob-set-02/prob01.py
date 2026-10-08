from references import Node


# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


# Add your single assignment statement here: head = ...  (Harry -> Ron -> Hermione)
