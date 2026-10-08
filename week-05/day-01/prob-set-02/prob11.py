from references import Node

# Linked list from Problem 10: dog -> cat -> mouse
dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
dog.next = cat
cat.next = mouse

# Remove dog and add cheese to the end here, so the list is cat -> mouse -> cheese
