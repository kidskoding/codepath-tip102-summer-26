from prob08 import Node, compare_graphs, prob08


def build_arrangement():
    lily = Node("Lily Gladstone")
    mark = Node("Mark Ruffalo")
    cillian = Node("Cillian Murphy")
    danielle = Node("Danielle Brooks")
    lily.neighbors.extend([mark, danielle])
    mark.neighbors.extend([lily, cillian])
    cillian.neighbors.extend([danielle, mark])
    danielle.neighbors.extend([lily, cillian])
    return lily


def test_prob08_is_a_clone():
    lily = build_arrangement()
    copy = prob08(lily)
    assert compare_graphs(lily, copy)


def test_prob08_is_a_deep_copy():
    lily = build_arrangement()
    copy = prob08(lily)
    assert copy is not lily
    assert all(c is not o for c, o in zip(copy.neighbors, lily.neighbors))


def test_prob08_single_node():
    solo = Node("Ke Huy Quan")
    copy = prob08(solo)
    assert copy is not solo
    assert copy.val == "Ke Huy Quan"
    assert copy.neighbors == []
