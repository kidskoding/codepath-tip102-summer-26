import pytest
from references import TreeNode
from prob02 import prob02


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


GROTTO = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", None, "Whozit"]


@pytest.mark.parametrize("values, treasure, expected", [
    (GROTTO, "Dinglehopper", True),   # example 1
    (GROTTO, "Thingamabob", False),   # example 2
    (GROTTO, "Snarfblat", True),      # root
    (GROTTO, "Whozit", True),         # leaf
    ([], "Gizmo", False),             # empty tree
])
def test_prob02(values, treasure, expected):
    assert prob02(build(values), treasure) == expected
