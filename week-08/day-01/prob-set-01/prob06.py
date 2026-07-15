from references import TreeNode

# Input: A Binary Tree that we need to do postorder traversal on
# Output: A list of strings that represent the postorder traversal of the binary tree
def prob06(root: TreeNode | None) -> list[str]:
	if not root:
		return []
	
	res = []
	
	def prob06_helper(node: TreeNode | None):
		if not node:
			return
	
		prob06_helper(node.left)
		prob06_helper(node.right)
		res.append(node.val)
	
	prob06_helper(root)
	return res
	
# Time: O(n) - every node is visited exactly once
# Space: O(h) - the recursion call stack is as deep as the tree's height h
