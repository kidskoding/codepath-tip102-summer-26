# Problem Set #1: Binary Search Trees — Week 8, Day 2

All problems use the shared `TreeNode` class (attribute is `.val`; Problems 5–6
also use an integer `.key`):

```python
class TreeNode:
    def __init__(self, value, left=None, right=None, key=None):
        self.val = value
        self.key = key
        self.left = left
        self.right = right
```

---

## Problem 1: Monstera Madness

**Difficulty:** Easy

### Description

Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, return the number of Monstera leaves that have an odd number of splits.

Note: The term leaf here refers to the plant leaf of a Monstera plant (i.e. every node), not leaf nodes (nodes with no children).

Evaluate the time complexity of your function. Define your variables and provide a rationale for the stated time complexity.

### Function Signature

```python
def prob01(root):
    pass
```

### Examples

**Example 1:**
```
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12

Input:  root of the tree above
Output: 3
```
Three nodes have an odd number of splits (3, 5, and 7).

**Example 2:**
```
Input:  None
Output: 0
```

---

## Problem 2: Flower Finding

**Difficulty:** Easy

### Description

You are looking to buy a new flower plant for your garden. The nursery you visit stores its inventory in a binary search tree (BST) where each node represents a plant in the store. The plants are organized according to their names (`val`) in alphabetical order in the BST.

Given the root of the binary search tree `inventory` and a target flower `name`, return `True` if the flower is present in the garden and `False` otherwise.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob02(inventory, name):
    pass
```

### Examples

**Example 1:**
```
         Rose
        /    \
      Lilac   Tulip
     /  \       \
  Daisy  Lily  Violet

Input:  inventory = root of the tree above, name = "Lilac"
Output: True
```

**Example 2:**
```
Input:  inventory = same tree, name = "Sunflower"
Output: False
```

---

## Problem 3: Flower Finding II (SKIPPED)

### Description

_Discussion/comparison problem — no implementation._ Compare `find_flower()` from Problem 2 against a given `non_bst_find_flower()` that searches a non-BST binary tree; discuss the difference in code and time complexity, and how Problem 2's complexity changes if the tree is unbalanced.

---

## Problem 4: Adding a New Plant to the Collection

**Difficulty:** Medium

### Description

Your houseplant collection is organized using a BST where each node represents a houseplant, organized alphabetically by name (`val`).

Given the root of your BST `collection` and a new houseplant `name`, insert a new node with value `name` into your collection. Return the root of the updated collection. If another plant with `name` already exists in the tree, add the new node in the existing node's right subtree.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob04(collection, name):
    pass
```

### Examples

**Example 1:**
```
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant

Input:  collection = root of the tree above, name = "Aloe"
Output: root of the updated tree:

           Money Tree
        /              \
 Fiddle Leaf Fig   Snake Plant
   /
 Aloe
```

---

## Problem 5: Sorting Plants by Rarity

**Difficulty:** Medium

### Description

You track your plant collection in a BST where each node has a `key` and a `val`. The `val` contains the plant name, and the `key` is an integer representing the plant's rarity. Plants are organized in the BST by their `key`.

Given the BST root `collection`, return an array of plant nodes as tuples in the form `(key, val)` sorted from least to most rare. Sorted order can be achieved by performing an inorder traversal of the BST.

### Function Signature

```python
def prob05(collection):
    pass
```

### Examples

**Example 1:**
```
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")

Input:  collection = root of the tree above
Output: [(1, 'Pothos'), (2, 'Spider Plant'), (3, 'Monstera'), (4, 'Hoya Motoskei'), (5, 'Witchcraft Orchid')]
```

---

## Problem 6: Finding a New Plant Within Budget

**Difficulty:** Medium

### Description

The plant store you are shopping at stores its inventory in a BST where each node has a `key` representing the price of the plant and `val` containing the plant's name. Plants are ordered by their prices.

Given the root of the BST `inventory` and an integer `budget`, return the name of the plant with the highest price strictly below `budget`. If no such plant exists, return `None`.

### Function Signature

```python
def prob06(inventory, budget):
    pass
```

### Examples

**Example 1:**
```
               (50, "Fiddle Leaf Fig")
             /                       \
    (25, "Monstera")           (70, "Snake Plant")
       /        \                   /         \
(15, "Aloe")  (40, "Pothos")  (60, "Fern")  (80, "ZZ Plant")

Input:  inventory = root of the tree above, budget = 50
Output: "Pothos"
```

**Example 2:**
```
Input:  inventory = same tree, budget = 25
Output: "Aloe"
```

**Example 3:**
```
Input:  inventory = same tree, budget = 15
Output: None
```

---

## Problem 7: Remove Plant

**Difficulty:** Hard

### Description

Given the root of a BST `collection` where each node represents a plant in your collection, and a plant `name`, remove the plant node with value `name` from the collection. Return the root of the modified collection. Plants are organized alphabetically in the tree by `val`.

If the node with `name` has two children in the tree, replace it with its inorder predecessor (rightmost node in its left subtree). You do not need to maintain a balanced tree.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob07(collection, name):
    # Find the node to remove
    # If the node has no children
        # Remove the node by setting parent pointer to None
    # If the node has one child
        # Replace the node with its child
    # If the node has two children
        # Find the inorder predecessor
        # Replace the node's value with inorder predecessor value
        # Remove inorder predecessor
    # Return root of updated tree
    pass
```

### Examples

**Example 1:**
```
              Money Tree
             /         \
           Hoya        Pilea
              \        /   \
             Ivy    Orchid  ZZ Plant

Input:  collection = root of the tree above, name = "Pilea"
Output: root of the updated tree:

             Money Tree
            /         \
          Hoya       Orchid
              \          \
              Ivy      ZZ Plant
```

---
