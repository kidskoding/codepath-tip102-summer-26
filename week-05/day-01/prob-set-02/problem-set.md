# Problem Set: Object-Oriented Programming & Linked Lists — Week 5, Day 1 (Version 2)

---

## Problem 1: Instantiate an Instance of Player

### Description

Instantiate an instance of the `Player` class and store it in a variable named `player_one`.

The `Player` object should have the character `"Yoshi"` and the kart `"Super Blooper"`.

```python
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
```

### Examples

**Example 1:**
```
Input:  player_one = Player("Yoshi", "Super Blooper")
Output:
Yoshi
Super Blooper
[]
```

---

## Problem 2: Get Player

### Description

Using the `Player` class from Problem 1, add the `get_player()` method below to your existing code:

```python
def get_player(self):
    return f"{self.character} driving the {self.kart}"
```

Create a second `Player` instance named `player_two` with character `"Bowser"` and kart `"Pirahna Prowler"`.

Use `get_player()` to print `"Match: Yoshi driving the Super Blooper vs Bowser driving the Pirahna Prowler"`.

### Examples

**Example 1:**
```
Input:  player_two = Player("Bowser", "Pirahna Prowler")
        print(player_two.character)
        print(player_two.kart)
        print(player_two.items)
Output:
Bowser
Pirahna Prowler
[]
```

---

## Problem 3: Update Kart

### Description

Update `player_one` so that their kart is `"Dolphin Dasher"` instead of `"Super Blooper"` by directly modifying the attribute.

### Examples

**Example 1:**
```
Input:  player_one.get_player()
Output: Yoshi driving the Dolphin Dasher
```

---

## Problem 4: Set Character

### Description

Update the `Player` class with a method `set_character()` that takes in one parameter `name`.

- If `name` is valid, update the player's `character` attribute and print `"Character updated"`.
- Otherwise, print `"Invalid character"`.

Valid characters: `"Mario"`, `"Luigi"`, `"Peach"`, `"Yoshi"`, `"Toad"`, `"Wario"`, `"Donkey Kong"`, `"Bowser"`.

### Function Signature

```python
def set_character(self, name):
    pass
```

### Examples

**Example 1:**
```
Input:  player_three = Player("Donkey Kong", "Standard Kart")
        player_three.set_character("Peach")
        print(player_three.character)
        player_three.set_character("Baby Peach")
        print(player_three.character)
Output:
Character Updated
Peach
Invalid Character
Peach
```

---

## Problem 5: Add Special Item

### Description

Update the `Player` class with a method `add_item()` that takes in one parameter `item_name`.

- If `item_name` is valid, add it to the player's `items` list.
- The method does not return any values.

Valid items: `"banana"`, `"green shell"`, `"red shell"`, `"bob-omb"`, `"super star"`, `"lightning"`, `"bullet bill"`.

### Function Signature

```python
def add_item(self, item_name):
    pass
```

### Examples

**Example 1:**
```
Input:  player_one = Player("Yoshi", "Dolphin Dasher")
        player_one.add_item("red shell")
        player_one.add_item("super star")
        player_one.add_item("super smash")
Output:
[]
['red shell']
['red shell', 'super star']
['red shell', 'super star']
```

---

## Problem 6: Print Inventory

### Description

Update the `Player` class with a method `print_inventory()` that accepts no parameters except `self`.

- Print the name and quantity of each item in the format `"Inventory: item1: quantity, item2: quantity, ..."`.
- If the player has no items, print `"Inventory empty"`.

### Function Signature

```python
def print_inventory(self):
    pass
```

### Examples

**Example 1:**
```
Input:  player_one = Player("Yoshi", "Super Blooper")
        player_one.items = ["banana", "bob-omb", "banana", "super star"]
        player_one.print_inventory()
Output: Inventory: banana: 2, bob-omb: 1, super star: 1
```

**Example 2:**
```
Input:  player_two = Player("Peach", "Dolphin Dasher")
        player_two.print_inventory()
Output: Inventory empty
```

---

## Problem 7: Race Results

### Description

Given a list `race_results` of `Player` objects where position in the list corresponds to finishing place, write a function `prob07()` that prints each player's place and character name.

### Function Signature

```python
def prob07(race_results):
    pass
```

### Examples

**Example 1:**
```
Input:  peach = Player("Peach", "Daytripper")
        mario = Player("Mario", "Standard Kart M")
        luigi = Player("Luigi", "Super Blooper")
        prob07([peach, mario, luigi])
Output:
1. Peach
2. Mario
3. Luigi
```

---

## Problem 8: Get Rank

### Description

The `Player` class has been updated with an `ahead` attribute representing the player directly ahead in the race (another `Player` instance, defaulting to `None`).

Write a function `prob08()` that accepts a `Player` object `my_player` and returns their current place number in the race.

```python
class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent
```

### Function Signature

```python
def prob08(my_player):
    pass
```

### Examples

**Example 1:**
```
Input:  peach = Player("Peach", "Daytripper")
        mario = Player("Mario", "Standard Kart M", peach)
        luigi = Player("Luigi", "Super Blooper", mario)
        prob08(luigi)
Output: 3
```

**Example 2:**
```
Input:  prob08(peach)
Output: 1
```

**Example 3:**
```
Input:  prob08(mario)
Output: 2
```

---

## Problem 9: Tom and Jerry

### Description

A linked list stores data sequentially where each node holds a value and a pointer to the next node (unlike arrays, nodes are not stored in adjacent memory locations).

Using the `Node` class below, create a linked list `cat -> mouse` where `cat` has value `"Tom"` and points to `mouse` with value `"Jerry"`.

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
```

### Examples

**Example 1:**
```
Input:  cat = Node("Tom")
        mouse = Node("Jerry")
        cat.next = mouse
Output:
Tom
<Node object>   # cat.next, the node stored in mouse
Jerry
Jerry
None
```

---

## Problem 10: Chase List

### Description

Using the linked list from Problem 9, create a new `Node` `dog` with value `"Spike"` and point it to `cat` so the full list becomes `dog -> cat -> mouse`.

### Examples

**Example 1:**
```
Input:  (linked list: dog -> cat -> mouse)
Output:
Spike
<Node object>   # dog.next, the node stored in cat
Tom
<Node object>   # cat.next, the node stored in mouse
Jerry
None
```

---

## Problem 11: Update Chase

### Description

Using the linked list from Problem 10, remove the `dog` node and add a new node `cheese` with value `"Gouda"` to the end, so the resulting list is `cat -> mouse -> cheese`.

### Examples

**Example 1:**
```
Input:  (after modification)
Output: cat -> mouse -> cheese
```

---

## Problem 12: Chase String

### Description

Write a function `prob12()` that takes the head of a linked list and returns a string of all node values joined by `" chases "`.

### Function Signature

```python
def prob12(head):
    pass
```

### Examples

**Example 1:**
```
Input:  dog -> cat -> mouse -> cheese  (as linked list)
Output: "Spike chases Tom chases Jerry chases Gouda"
```

---
