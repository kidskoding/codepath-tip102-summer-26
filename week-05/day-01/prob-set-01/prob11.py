from references import Node

# Linked list from Problem 10: tom_nook -> timmy -> tommy
tom_nook = Node("Tom Nook")
timmy = Node("Timmy")
tommy = Node("Tommy")
tom_nook.next = timmy
timmy.next = tommy

# Remove tom_nook and add saharah to the end here, so the list is timmy -> tommy -> saharah
