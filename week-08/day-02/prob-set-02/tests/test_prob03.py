import pytest
from references import TreeNode
from prob03 import prob03


def build(values):
    """CodePath-style level-order list (None = no node) -> tree"""
    if not values:
        return None
    it = iter(values[1:])
    root = TreeNode(values[0])
    queue = [root]
    for node in queue:
        for side in ("left", "right"):
            v = next(it, None)
            if v is not None:
                child = TreeNode(v)
                setattr(node, side, child)
                queue.append(child)
    return root


def to_level_list(root):
    """tree -> level-order list with None gaps, trailing Nones stripped"""
    if root is None:
        return []
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


GROTTO = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", None, "Whozit"]


@pytest.mark.parametrize("values, new_item, expected", [
    # example: Thingamabob becomes Whatzit's left child
    (GROTTO, "Thingamabob",
     ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", "Thingamabob", "Whozit"]),
    # duplicate -> tree unchanged
    (GROTTO, "Gizmo",
     ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", None, "Whozit"]),
    # insert into empty tree -> new node is the root
    ([], "Thingamabob", ["Thingamabob"]),
])
def test_prob03(values, new_item, expected):
    assert to_level_list(prob03(build(values), new_item)) == expected
