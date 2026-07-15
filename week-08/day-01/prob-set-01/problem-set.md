# Problem Set #1: Binary Trees — Week 8, Day 1

All problems use the shared `TreeNode` class (note the attribute is `.val`):

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
```

---

## Problem 1: Grafting Apples (SKIPPED)

_Tree-construction problem — no function to implement._

Grafting different varieties of apple onto the same root tree can produce many varieties of apples! Using the `TreeNode` class, construct the binary tree below (the text of each node is its value). The root `TreeNode("Trunk")` is provided.

```
             Trunk
          /         \
      Mcintosh   Granny Smith
      /     \       /     \
    Fuji   Opal   Crab   Gala
```

Verify with the provided `print_tree(root)`, which should give:
`['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']`

---

## Problem 2: Calculating Yield

**Difficulty:** Easy

### Description

You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. Given the `root` of the tree, evaluate the amount of fruit your tree will yield this year:

- Leaf nodes have an integer value.
- The root has a string value of either `"+"`, `"-"`, or `"*"`.
- The yield is calculated by applying the operation to the two children.

Return the result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

### Function Signature

```python
def prob02(root):
    pass
```

### Examples

**Example 1:**
```
Input:  root = TreeNode("+", TreeNode(7), TreeNode(5))
Output: 12
```

---

## Problem 3: Ivy Cutting

**Difficulty:** Easy

### Description

You have a trailing ivy plant represented by a binary tree. You want to take a cutting using the rightmost vine. Given the `root` of the plant, return a list with the value of each node in the path from the root to the rightmost leaf node. If there is no right child, the rightmost path is just the root — return only the root node value.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced.

### Function Signature

```python
def prob03(root):
    pass
```

### Examples

**Example 1:**
```
Input:  Root -> (Node1 -> Leaf1) , (Node2 -> Leaf2, Leaf3)
Output: ['Root', 'Node2', 'Leaf3']
```

**Example 2:**
```
Input:  Root -> (Node1 -> Leaf1)   (no right child anywhere)
Output: ['Root']
```

---

## Problem 4: Ivy Cutting II

**Difficulty:** Easy

### Description

Implement `prob03()` again using the opposite approach: if you implemented it iteratively in Problem 3, implement it recursively here; if you implemented it recursively, implement it iteratively.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced.

### Function Signature

```python
def prob04(root):
    pass
```

### Examples

**Example 1:**
```
Input:  Root -> (Node1 -> Leaf1) , (Node2 -> Leaf2, Leaf3)
Output: ['Root', 'Node2', 'Leaf3']
```

**Example 2:**
```
Input:  Root -> (Node1 -> Leaf1)
Output: ['Root']
```

---

## Problem 5: Count the Tree Leaves

**Difficulty:** Easy

### Description

You've grown an oak tree from a tiny acorn and it's finally sprouting leaves! Given the `root` of a binary tree, count the number of leaf nodes in the tree. A leaf node is a node with no children.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced.

### Function Signature

```python
def prob05(root):
    pass
```

### Examples

**Example 1:**
```
Input:  Root -> (Node1 -> Leaf1) , (Node2 -> Leaf2, Leaf3)
Output: 3
```

**Example 2:**
```
Input:  Root -> (Node1 -> Leaf1)
Output: 1
```

---

## Problem 6: Pruning Plans

**Difficulty:** Medium

### Description

You have a large overgrown Magnolia tree in need of pruning. Before pruning, survey the whole tree. Given the `root` of a binary tree, return a list of the values of each node using a **postorder** traversal: explore the left subtree first, then the right subtree, and finally the root.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced.

### Function Signature

```python
def prob06(root):
    pass
```

### Examples

**Example 1:**
```
Input:  Root -> (Node1 -> Leaf1) , (Node2 -> Leaf2, Leaf3)
Output: ["Leaf1", "Node1", "Leaf2", "Leaf3", "Node2", "Root"]
```

---

## Problem 7: Foraging Berries

**Difficulty:** Medium

### Description

You've found a wild blueberry bush and want to forage — but leave some behind for the ecosystem. Given the `root` of a binary tree where each node's value is the number of berries on a branch, and a value `threshold`, write `prob07()` that returns the sum of all node values strictly greater than `threshold`.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced.

### Function Signature

```python
def prob07(root, threshold):
    pass
```

### Examples

**Example 1:**
```
Input:  bush = 4 -> (10 -> 5, 8) , (6 -> _, 20), threshold = 6
Output: 38
```
Explanation: nodes greater than 6 are 8, 10, 20 → 8 + 10 + 20 = 38

**Example 2:**
```
Input:  bush, threshold = 30
Output: 0
```
Explanation: no nodes greater than 30

---

## Problem 8: Flower Fields

**Difficulty:** Easy

### Description

You're looking for the perfect bloom for your bouquet. Given the `root` of a binary tree representing flower options and a target `flower`, return `True` if the bloom exists in the tree and `False` otherwise.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced.

### Function Signature

```python
def prob08(root, flower):
    pass
```

### Examples

**Example 1:**
```
Input:  Rose -> (Lily -> Orchid, Lilac) , (Daisy -> _, Dahlia), flower = "Lilac"
Output: True
```

**Example 2:**
```
Input:  same tree, flower = "Hibiscus"
Output: False
```
