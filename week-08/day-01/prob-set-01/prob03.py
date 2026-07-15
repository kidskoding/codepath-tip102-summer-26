from references.treenode import TreeNode

# Input: Binary Tree
# Output: the right values of a Binary Tree
def prob03(root: TreeNode | None) -> list[str]:
    if not root:
        return []

    res = [root.val]
    
    def prob03_helper(node: TreeNode | None) -> list[str]:
        if not node.right:
            return res

        prob03_helper(node.right)

    return prob03_helper(root)

# Time:  O(h) - visits one node per level down the right spine (h = height; O(log n) if balanced)
# Space: O(h) - recursive: call stack depth h.
