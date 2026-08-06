import pytest
from references import TreeNode
from prob06 import prob06


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


ECOSYSTEM = ["Dugong", "Brain Coral", "Lionfish", None, "Clownfish", "Giant Clam", "Seagrass"]


@pytest.mark.parametrize("values, name, expected", [
    # example: two children -> replaced by inorder successor (Seagrass)
    (ECOSYSTEM, "Lionfish",
     ["Dugong", "Brain Coral", "Seagrass", None, "Clownfish", "Giant Clam"]),
    # leaf removal
    (ECOSYSTEM, "Clownfish",
     ["Dugong", "Brain Coral", "Lionfish", None, None, "Giant Clam", "Seagrass"]),
    # one child -> replaced by its child
    (ECOSYSTEM, "Brain Coral",
     ["Dugong", "Clownfish", "Lionfish", None, None, "Giant Clam", "Seagrass"]),
    # root with two children -> successor (Giant Clam) takes root's place
    (ECOSYSTEM, "Dugong",
     ["Giant Clam", "Brain Coral", "Lionfish", None, "Clownfish", None, "Seagrass"]),
    # single-node tree -> empty
    (["Dugong"], "Dugong", []),
])
def test_prob06(values, name, expected):
    assert to_level_list(prob06(build(values), name)) == expected
