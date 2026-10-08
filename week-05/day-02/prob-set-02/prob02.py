from references import Node

shy_guy = Node("Shy Guy")
diddy_kong = Node("Diddy Kong")
dry_bones = Node("Dry Bones")
shy_guy.next = diddy_kong
diddy_kong.next = dry_bones

# Update the list here to: shy_guy -> link -> diddy_kong -> toad -> dry_bones
