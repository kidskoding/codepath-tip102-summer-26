# Build the weighted, undirected graph from the source's diagram as an adjacency
# dictionary: collaborations[actor] = [(costar, num_collaborations), ...]
#
# From the source, collaborations["Chadwick Boseman"] should be:
# [("Lupita Nyong'o", 2), ("Robert Downey Jr.", 3), ("Mark Ruffalo", 2)]

collaborations: dict[str, list[tuple[str, int]]] = {
    # Add the graph here
}
