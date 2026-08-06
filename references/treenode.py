class TreeNode:
    # Binary tree node. Note the attribute is `.val` (not `.value` like Node).
    def __init__(self, value, left=None, right=None, key=None):
        self.val = value
        self.key = key  # used by key/val BST problems (e.g. plant rarity/price)
        self.left = left
        self.right = right
