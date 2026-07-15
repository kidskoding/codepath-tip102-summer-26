# Problem Set: Object-Oriented Programming & Linked Lists — Week 5, Day 1 (Version 1)

---

## Problem 1: New Horizons

### Description

Instantiate an instance of the `Villager` class, which represents characters in Animal Crossing. Store the instance in a variable named `apollo`.

The `Villager` object should have the name `"Apollo"`, the species `"Eagle"`, and the catchphrase `"pah"`.

```python
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
```

### Examples

**Example 1:**
```
Input:  apollo = Villager("Apollo", "Eagle", "pah")
Output:
Apollo
Eagle
pah
[]
```

---

## Problem 2: Greet Player

### Description

Using the `Villager` class from Problem 1, add the `greet_player()` method below to your existing code:

```python
def greet_player(self, player_name):
    return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
```

Create a second `Villager` instance named `bones` with name `"Bones"`, species `"Dog"`, and catchphrase `"yip yip"`.

Call `greet_player()` with your name and print the result.

### Examples

**Example 1:**
```
Input:  bones.greet_player("Tram")
Output: Bones: Hey there, Tram! How's it going, yip yip!
```

---

## Problem 3: Update Catchphrase

### Description

Update `bones` so that his catchphrase is `"ruff it up"` instead of `"yip yip"` by directly modifying the attribute.

### Examples

**Example 1:**
```
Input:  bones.greet_player("Samia")
Output: Bones: Hey there, Samia! How's it going, ruff it up!
```

---

## Problem 4: Set Character

### Description

Update the `Villager` class with a method `set_catchphrase()` that takes in one parameter `new_catchphrase`.

- If `new_catchphrase` is valid, update the villager's `catchphrase` attribute and print `"Catchphrase updated"`.
- Otherwise, print `"Invalid catchphrase"`.

A catchphrase is valid if it is less than 20 characters in length and contains only alphabetic and whitespace characters.

### Function Signature

```python
def set_catchphrase(self, new_catchphrase):
    pass
```

### Examples

**Example 1:**
```
Input:  alice = Villager("Alice", "Koala", "guvnor")
        alice.set_catchphrase("sweet dreams")
        print(alice.catchphrase)
        alice.set_catchphrase("#?!")
        print(alice.catchphrase)
Output:
Catchphrase Updated!
sweet dreams
Invalid catchphrase
sweet dreams
```

---

## Problem 5: Add Furniture

### Description

Update the `Villager` class with a method `add_item()` that takes in one parameter `item_name`.

- If `item_name` is valid, add it to the villager's `furniture` list.
- The method does not return any values.

Valid items: `"acoustic guitar"`, `"ironwood kitchenette"`, `"rattan armchair"`, `"kotatsu"`, `"cacao tree"`.

### Function Signature

```python
def add_item(self, item_name):
    pass
```

### Examples

**Example 1:**
```
Input:  alice = Villager("Alice", "Koala", "guvnor")
        alice.add_item("acoustic guitar")
        alice.add_item("cacao tree")
        alice.add_item("nintendo switch")
Output:
[]
["acoustic guitar"]
["acoustic guitar", "cacao tree"]
["acoustic guitar", "cacao tree"]
```

---

## Problem 6: Print Inventory

### Description

Update the `Villager` class with a method `print_inventory()` that accepts no parameters except `self`.

- Print the name and quantity of each item in the villager's `furniture` list in the format `"item1: quantity, item2: quantity, ..."`.
- If the villager has no items, print `"Inventory empty"`.

### Function Signature

```python
def print_inventory(self):
    pass
```

### Examples

**Example 1:**
```
Input:  alice = Villager("Alice", "Koala", "guvnor")
        alice.print_inventory()
Output: Inventory empty
```

**Example 2:**
```
Input:  alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
        alice.print_inventory()
Output: acoustic guitar: 1, ironwood kitchenette: 1, kotatsu: 2
```

---

## Problem 7: Group by Personality

### Description

The `Villager` class has been updated to include a `personality` attribute. Outside of the class, write a function `prob07()` that takes a list of `Villager` instances `townies` and a string `personality_type`, and returns a list of names of all villagers with that personality. Return names in any order.

```python
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
```

### Function Signature

```python
def prob07(townies, personality_type):
    pass
```

### Examples

**Example 1:**
```
Input:  isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
        bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
        stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")
        prob07([isabelle, bob, stitches], "Lazy")
Output: ["Bob", "Stitches"]
```

**Example 2:**
```
Input:  prob07([isabelle, bob, stitches], "Cranky")
Output: []
```

---

## Problem 8: Telephone

### Description

The `Villager` class has been updated with a `neighbor` attribute representing a villager's closest neighbor (another `Villager` instance, defaulting to `None`).

Write a function `prob08()` that takes two `Villager` instances `start_villager` and `target_villager`, and returns `True` if a message can be passed from `start_villager` to `target_villager` through a chain of neighbors, and `False` otherwise.

```python
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
```

### Function Signature

```python
def prob08(start_villager, target_villager):
    pass
```

### Examples

**Example 1:**
```
Input:  isabelle.neighbor = tom_nook
        tom_nook.neighbor = kk_slider
        prob08(isabelle, kk_slider)
Output: True
Explanation: Isabelle → Tom Nook → K.K. Slider. Target reached.
```

**Example 2:**
```
Input:  prob08(kk_slider, isabelle)
Output: False
Explanation: K.K. Slider has no neighbor, so the message cannot be passed.
```

---

## Problem 9: Nook's Cranny

### Description

A linked list stores data sequentially where each node holds a value and a pointer to the next node (unlike arrays, nodes are not stored in adjacent memory locations).

Using the `Node` class below, create a linked list `tom_nook -> tommy` where `tom_nook` has value `"Tom Nook"` and points to `tommy` with value `"Tommy"`.

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
```

### Examples

**Example 1:**
```
Input:  tom_nook = Node("Tom Nook")
        tommy = Node("Tommy")
        tom_nook.next = tommy
Output:
Tom Nook
Tommy
Tommy
None
```

---

## Problem 10: Timmy and Tommy

### Description

Using the linked list from Problem 9, create a new `Node` `timmy` with value `"Timmy"` and insert it between `tom_nook` and `tommy` so the list becomes `tom_nook -> timmy -> tommy`.

### Examples

**Example 1:**
```
Input:  (linked list: tom_nook -> timmy -> tommy)
Output:
Tom Nook
Timmy
Timmy
Tommy
Tommy
None
```

---

## Problem 11: Saharah

### Description

Using the linked list from Problem 10, remove the `tom_nook` node and add a new node `saharah` with value `"Saharah"` to the end, so the resulting list is `timmy -> tommy -> saharah`.

### Examples

**Example 1:**
```
Input:  (after modification)
Output:
None         # tom_nook.next
Timmy
Tommy
Tommy
Saharah
Saharah
None
```

---

## Problem 12: Print Players Linked List

### Description

Write a function `prob12()` that takes the head of a linked list and returns a string of all node values joined by `" -> "`.

### Function Signature

```python
def prob12(head):
    pass
```

### Examples

**Example 1:**
```
Input:  isabelle -> saharah -> cj  (as linked list)
Output: "Isabelle -> Saharah -> C.J."
```

---
