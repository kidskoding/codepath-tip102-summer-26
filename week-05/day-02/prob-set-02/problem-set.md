# Problem Set: Linked Lists (Mario Kart) — Week 5, Day 2

Linked list problems use the shared `Node` class (`from references import Node`):

```python
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
```

---

## Problem 1: Calculate Tournament Placement

### Description

In the `Player` class below, each player has a `race_outcomes` attribute: a list of integers giving the place they finished in each race of a tournament.

Write a method `get_tournament_place()` that takes one parameter, `opponents`, a list of other `Player` objects in the tournament, and returns the current player's place in the overall tournament.

- Tournament rank is determined by the lowest average race outcome (1st place is better than 2nd).
- Every opponent has raced the same number of races as the current player.

```python
class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes
```

### Function Signature

```python
def get_tournament_place(self, opponents):
    pass
```

### Examples

**Example 1:**
```
Input:  player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
        player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
        player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])
        player1.get_tournament_place([player2, player3])
Output: 1
Explanation: Mario's average place is 1.6, Luigi's is 2.0, and Peach's is 2.4.
```

---

## Problem 2: Update Linked List Sequence (SKIPPED)

_Linked-list construction problem — no function to implement._

### Description

Update the linked list `shy_guy -> diddy_kong -> dry_bones` to `shy_guy -> link -> diddy_kong -> toad -> dry_bones`.

```python
shy_guy = Node("Shy Guy")
diddy_kong = Node("Diddy Kong")
dry_bones = Node("Dry Bones")
shy_guy.next = diddy_kong
diddy_kong.next = dry_bones

# Add code to update the list here
```

Printing the list from `shy_guy` should give `Shy Guy -> Link -> Diddy Kong -> Toad -> Dry Bones`.

---

## Problem 3: Insert Node as Second Element

### Description

Write a function `prob03()` that takes the `head` of a linked list and a value `val`, inserts `val` as the second node in the list, and returns the head. You can assume `head` is not `None`.

### Function Signature

```python
def prob03(head, val):
    pass
```

### Examples

**Example 1:**
```
Input:  head = banana -> blue shell -> bullet bill, val = "red shell"
Output: banana -> red shell -> blue shell -> bullet bill
```

---

## Problem 4: Increment Linked List Node Values

### Description

Write a function `prob04()` that takes the `head` of a linked list of integers, increments each node's value by 1, and returns the head of the same list.

### Function Signature

```python
def prob04(head):
    pass
```

### Examples

**Example 1:**
```
Input:  head = 5 -> 6 -> 7
Output: 6 -> 7 -> 8
```

---

## Problem 5: Copy Linked List

### Description

Write a function `prob05()` that takes the `head` of a linked list and returns the head of a complete copy. The copy has the same structure and values as the original but uses none of the original node objects.

### Function Signature

```python
def prob05(head):
    pass
```

### Examples

**Example 1:**
```
Input:  head = Mario -> Daisy -> Luigi
        copy = prob05(head)
        head.value = "Original Mario"     # changing the original must not affect the copy
Output: original: Original Mario -> Daisy -> Luigi
        copy:     Mario -> Daisy -> Luigi
```

---

## Problem 6: Making the Cut

### Description

A linked list tracks the order players finished a race. Write a function `prob06()` that takes the `head` of the list and a non-negative integer `n`, and returns a list of the values of the first `n` nodes. If `n` is greater than the length of the list, return the values of all nodes.

### Function Signature

```python
def prob06(head, n):
    pass
```

### Examples

**Example 1:**
```
Input:  head = Daisy -> Mario -> Toad -> Yoshi, n = 3
Output: ["Daisy", "Mario", "Toad"]
```

**Example 2:**
```
Input:  head = Daisy -> Mario -> Toad -> Yoshi, n = 5
Output: ["Daisy", "Mario", "Toad", "Yoshi"]
```

---

## Problem 7: Remove Racer

### Description

Write a function `prob07()` that takes the `head` of a linked list and a value `racer`, removes the first node with value `racer`, and returns the head of the modified list. If `racer` is not in the list, return the original head.

### Function Signature

```python
def prob07(head, racer):
    pass
```

### Examples

**Example 1:**
```
Input:  head = Daisy -> Mario -> Toad -> Mario, racer = "Mario"
Output: Daisy -> Toad -> Mario
```

**Example 2:**
```
Input:  head = Daisy -> Mario -> Toad, racer = "Yoshi"
Output: Daisy -> Mario -> Toad
```

_Note: the source prints `Daisy -> Mario -> Toad` for Example 1, which removes the **last** `Mario`. Removing the **first** `Mario`, as the description requires, gives `Daisy -> Toad -> Mario`._

---

## Problem 8: Array to Linked List

### Description

Write a function `prob08()` that takes a list `arr` of `Player` instances and converts it into a linked list where each node's value is a `Player`. Return the head of the linked list, or `None` if `arr` is empty.

`Player` is the shared class (`from references import Player`), created as `Player(character, kart)`.

### Function Signature

```python
def prob08(arr):
    pass
```

### Examples

**Example 1:**
```
Input:  arr = [Player("Mario", "Mushmellow"), Player("Luigi", "Standard LG"), Player("Peach", "Bumble V")]
Output: Mario -> Luigi -> Peach      (printing each node's value.character)
```

**Example 2:**
```
Input:  arr = [Player("Peach", "Bumble V")]
Output: Peach
```

---

## Problem 9: Convert Singly Linked List to Doubly Linked List (SKIPPED)

_Linked-list construction problem — no function to implement._

### Description

A **doubly linked list** gives each node a `prev` attribute pointing to the node before it. Update the code below to convert the singly linked list into a doubly linked list.

```python
koopa_troopa = Node("Koopa Troopa")
toadette = Node("Toadette")
waluigi = Node("Waluigi")
koopa_troopa.next = toadette
toadette.next = waluigi

# Add code to convert to doubly linked list here
```

Printing forward from `koopa_troopa` should give `Koopa Troopa -> Toadette -> Waluigi`, and printing backward from `waluigi` should give `Waluigi -> Toadette -> Koopa Troopa`.

---

## Problem 10: Find Length of Doubly Linked List from Any Node

### Description

Write a function `prob10()` that takes a `node` at an unknown position in a doubly linked list and returns the length of the entire list.

### Function Signature

```python
def prob10(node):
    pass
```

### Examples

**Example 1:**
```
Input:  node = rainbow_road, for the list Yoshi Falls <-> Moo Moo Farm <-> Rainbow Road <-> DK Mountain
Output: 4
```

---
