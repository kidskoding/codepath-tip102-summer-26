# Problem Set: Linked Lists (Animal Crossing) — Week 5, Day 2

Linked list problems use the shared `Node` class (`from references import Node`):

```python
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
```

---

## Problem 1: Mutual Friends

### Description

In the `Villager` class below, each villager has a `friends` attribute: a list of other villagers they are friends with.

Write a method `get_mutuals()` that takes one parameter, a `Villager` instance `new_contact`, and returns a list of the names of all friends the current villager and `new_contact` have in common.

```python
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []
```

### Function Signature

```python
def get_mutuals(self, new_contact):
    pass
```

### Examples

```python
bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")
```

**Example 1:**
```
Input:  bob.friends = [stitches, raymond, fauna]
        marshal.friends = [raymond, ankha, fauna]
        bob.get_mutuals(marshal)
Output: ['Raymond', 'Fauna']
```

**Example 2:**
```
Input:  ankha.friends = [marshal]
        bob.get_mutuals(ankha)
Output: []
```

---

## Problem 2: Linked Up (SKIPPED)

_Linked-list construction problem — no function to implement._

### Description

Connect the provided nodes to create the linked list `kk_slider -> harriet -> saharah -> isabelle`.

```python
kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# Add code here to link the above nodes
```

Printing the list from `kk_slider` should give `K.K. Slider -> Harriet -> Saharah -> Isabelle`.

---

## Problem 3: Daily Tasks

### Description

A linked list is used as a daily task list, where each node is a task. Write a function `prob03()` that takes the `head` of the list and a string `task`, inserts a new `Node` with value `task` at the front of the list, and returns the new head.

### Function Signature

```python
def prob03(head, task):
    pass
```

### Examples

**Example 1:**
```
Input:  head = shake tree -> dig fossils -> catch bugs, task = "check turnip prices"
Output: check turnip prices -> shake tree -> dig fossils -> catch bugs
```

---

## Problem 4: Halve List

### Description

Write a function `prob04()` that takes the `head` of a linked list of integers, divides each value by two, and returns the head of the modified list.

### Function Signature

```python
def prob04(head):
    pass
```

### Examples

**Example 1:**
```
Input:  head = 5 -> 6 -> 7
Output: 2.5 -> 3.0 -> 3.5
```

---

## Problem 5: Remove Last

### Description

Write a function `prob05()` that takes the `head` of a linked list, removes the last node (the **tail**), and returns the head of the modified list.

### Function Signature

```python
def prob05(head):
    pass
```

### Examples

**Example 1:**
```
Input:  head = Common Butterfly -> Ladybug -> Scarab Beetle
Output: Common Butterfly -> Ladybug
```

---

## Problem 6: Find Minimum in Linked List

### Description

Write a function `prob06()` that takes the `head` of a linked list of numbers and returns the minimum value in the list.

### Function Signature

```python
def prob06(head):
    pass
```

### Examples

**Example 1:**
```
Input:  head = Node(5, Node(6, Node(7, Node(8))))     # 5 -> 6 -> 7 -> 8
Output: 5
```

**Example 2:**
```
Input:  head = Node(8, Node(5, Node(6, Node(7))))     # 8 -> 5 -> 6 -> 7
Output: 5
```

---

## Problem 7: Remove From Inventory

### Description

A linked list stores a player's inventory. Write a function `prob07()` that takes the `head` of the list and a value `item`, removes the first node with value `item`, and returns the head of the modified list. If no node has value `item`, return the list unchanged.

### Function Signature

```python
def prob07(head, item):
    pass
```

### Examples

**Example 1:**
```
Input:  head = Slingshot -> Peaches -> Scarab Beetle, item = "Peaches"
Output: Slingshot -> Scarab Beetle
```

**Example 2:**
```
Input:  head = Slingshot -> Scarab Beetle, item = "Triceratops Torso"
Output: Slingshot -> Scarab Beetle
```

---

## Problem 8: Move Tail to Front of Linked List

### Description

Write a function `prob08()` that takes the `head` of a linked list, moves the tail node to the front, and returns the new head.

### Function Signature

```python
def prob08(head):
    pass
```

### Examples

**Example 1:**
```
Input:  head = Daisy -> Mario -> Toad -> Peach
Output: Peach -> Daisy -> Mario -> Toad
```

---

## Problem 9: Create Double Links (SKIPPED)

_Linked-list construction problem — no function to implement._

### Description

A **doubly linked list** gives each node a `prev` attribute pointing to the node before it, as well as `next` (e.g. `A <-> B <-> C`). Using the `Node` class with `next` and `prev`, create the doubly linked list `head <-> tail`:

```python
head = Node("Isabelle")
tail = Node("K.K. Slider")

head.next = tail
tail.prev = head
```

`print(head.value, "<->", head.next.value)` and `print(tail.prev.value, "<->", tail.value)` should both print `Isabelle <-> K.K. Slider`.

---

## Problem 10: Print Backwards

### Description

Write a function `prob10()` that takes the `tail` of a doubly linked list and prints the values of the list in reverse order, separated by spaces.

### Function Signature

```python
def prob10(tail):
    pass
```

### Examples

**Example 1:**
```
Input:  tail = saharah, for the list Isabelle <-> K.K. Slider <-> Saharah
Output (printed): Saharah K.K. Slider Isabelle
```

---
