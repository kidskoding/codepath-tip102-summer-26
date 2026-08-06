# Problem Set #2: Binary Trees — Week 8, Day 1

All problems use the shared `TreeNode` class (attribute is `.val`):

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
```

---

## Problem 1: Building an Underwater Kingdom (SKIPPED)

_Tree-construction problem — no function to implement._

Using the `TreeNode` class, construct the binary tree below (the text of each node is its value). The root `TreeNode("Poseidon")` is provided.

```
            Poseidon
          /         \
      Atlantis      Oceania
      /     \       /     \
  Coral     Pearl  Kelp    Reef
```

---

## Problem 2: Are Twins?

**Difficulty:** Easy

### Description

Given the root of a binary tree that has at most three nodes: the root, its left child, and its right child.

Return `True` if the root's children are twins (have equal value) and `False` otherwise. If the root has no children, return `False`.

Evaluate the time complexity of your function.

### Function Signature

```python
def prob02(root):
    pass
```

### Examples

**Example 1:**
```
      Mermother
       /    \
    Coral   Coral

Input:  root of the tree above
Output: True
```

**Example 2:**
```
      Merpapa
       /    \
   Calypso  Coral

Input:  root of the tree above
Output: False
```

**Example 3:**
```
      Merenby
           \
         Calypso

Input:  root of the tree above
Output: False
```

---

## Problem 3: Poseidon's Decision

**Difficulty:** Easy

### Description

Poseidon has received advice from his council of advisors. You are given the advice as the root of a binary tree representing a boolean expression that has at most three nodes. The root may have exactly 0 or 2 children.

- Leaf nodes have a boolean value of either `True` or `False`.
- Non-leaf nodes have a string value of either `"AND"` or `"OR"`.

The evaluation of a node is as follows:
- If the node is a leaf node, the evaluation is the value of the node, i.e. `True` or `False`.
- Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.

Return the boolean result of evaluating the root node.

Evaluate the time complexity of your function.

### Function Signature

```python
def prob03(root):
    pass
```

### Examples

**Example 1:**
```
        OR
      /    \
    True  False

Input:  root of the tree above
Output: True
```

**Example 2:**
```
       False

Input:  root of the tree above
Output: False
```

---

## Problem 4: Escaping the Sea Caves

**Difficulty:** Easy

### Description

You are given the root of a binary tree representing a possible route through a system of sea caves. So long as you take the leftmost branch at every fork in the route, you'll find your way back home. Return an array with the value of each node in the leftmost path. If there is no left child, return only the root node value (the leftmost path in this case is just the root node).

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob04(root):
    pass
```

### Examples

**Example 1:**
```
        CaveA
       /      \
    CaveB    CaveC
    /   \        \
CaveD CaveE     CaveF

Input:  root of the tree above
Output: ['CaveA', 'CaveB', 'CaveD']
```

**Example 2:**
```
  CaveA
      \
      CaveB
        \
        CaveC

Input:  root of the tree above
Output: ['CaveA']
```

---

## Problem 5: Escaping the Sea Caves II

**Difficulty:** Easy

### Description

If you implemented the previous problem iteratively, implement it recursively. If you implemented it recursively, implement it iteratively. Same behavior as Problem 4.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob05(root):
    pass
```

### Examples

Same as Problem 4:

**Example 1:**
```
Input:  root of the CaveA tree with left children
Output: ['CaveA', 'CaveB', 'CaveD']
```

**Example 2:**
```
Input:  root of the right-only CaveA tree
Output: ['CaveA']
```

---

## Problem 6: Documenting Reefs

**Difficulty:** Easy

### Description

You are exploring a vast coral reef system represented as a binary tree, where each node corresponds to a specific coral formation. Perform a preorder traversal of the reef and return a list of the names of the coral formations in the order you visited them. In a preorder exploration, you explore the current node first, then the left subtree, and finally the right subtree.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob06(root):
    pass
```

### Examples

**Example 1:**
```
         CoralA
        /     \
     CoralB  CoralC
     /   \
 CoralD CoralE

Input:  root of the tree above
Output: ['CoralA', 'CoralB', 'CoralD', 'CoralE', 'CoralC']
```

---

## Problem 7: Coral Count

**Difficulty:** Easy

### Description

Given the root of a binary tree where each node represents a coral in the reef, return the number of corals in the reef.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob07(root):
    pass
```

### Examples

**Example 1:**
```
          Staghorn
         /        \
        /          \
    Sea Fan      Sea Whip
    /     \       /
 Bubble  Table  Star
  /
Fire

Input:  root of the tree above
Output: 7
```

**Example 2:**
```
     Fire
    /    \
   /      \
Black    Star
        /
     Lettuce
           \
        Sea Whip

Input:  root of the tree above
Output: 5
```

---

## Problem 8: Ocean Layers

**Difficulty:** Easy

### Description

Given the root of a binary tree that represents different sections of the ocean, return the depth of the ocean. The depth or height of the tree is defined as the number of nodes on the longest path from the root node to a leaf node.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob08(root):
    pass
```

### Examples

**Example 1:**
```
                Sunlight
               /        \
              /          \
          Twilight      Squid
         /       \           \
      Abyss  Anglerfish    Giant Squid
      /
  Trenches

Input:  root of the tree above
Output: 4
```

**Example 2:**
```
    Spray Zone
    /         \
   /           \
Beach       High Tide
            /
      Middle Tide
              \
            Low Tide

Input:  root of the tree above
Output: 4
```

---
