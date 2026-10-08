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


def test_prob03_example():
    door = TreeNode("Door", TreeNode("Attic"), TreeNode("Cursed Room", TreeNode("Crypt"), TreeNode("Haunted Cellar")))
    assert prob03(door) == 2


@pytest.mark.parametrize("values, expected", [
    ([], 0),
    (["Door"], 1),
    (["Door", "Attic"], 2),  # root has a child, so it is not a leaf
    (["Door", "Attic", None, "Crypt"], 3),  # one-sided chain
])
def test_prob03(values, expected):
    assert prob03(build(values)) == expected
