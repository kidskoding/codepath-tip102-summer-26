# Problem Set: Strings & Arrays (Hundred Acre Wood) — Week 1, Day 1

---

## Problem 1: Hundred Acre Wood

**Difficulty:** Easy

### Description

Write a function `prob01()` that prints the string `"Welcome to The Hundred Acre Wood!"`.

### Function Signature

```python
def prob01():
    pass
```

### Examples

**Example 1:**
```
Input:  prob01()
Output: Welcome to The Hundred Acre Wood!
```

---

## Problem 2: Greeting

**Difficulty:** Easy

### Description

Write a function `prob02()` that accepts a single parameter, a string `name`, and prints the string `"Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."`.

### Function Signature

```python
def prob02(name):
    pass
```

### Examples

**Example 1:**
```
Input:  prob02("Michael")
Output: Welcome to The Hundred Acre Wood Michael! My name is Christopher Robin.
```

**Example 2:**
```
Input:  prob02("Winnie the Pooh")
Output: Welcome to The Hundred Acre Wood Winnie the Pooh! My name is Christopher Robin.
```

---

## Problem 3: Catchphrase

**Difficulty:** Easy

### Description

Write a function `prob03()` that accepts a string `character` as a parameter and prints the catchphrase of the given character as outlined in the table below.

| Character | Catchphrase |
| --- | --- |
| `"Pooh"` | `"Oh bother!"` |
| `"Tigger"` | `"TTFN: Ta-ta for now!"` |
| `"Eeyore"` | `"Thanks for noticing me."` |
| `"Christopher Robin"` | `"Silly old bear."` |

If the given character does not match one of the characters above, print `"Sorry! I don't know <character>'s catchphrase!"`.

### Function Signature

```python
def prob03(character):
    pass
```

### Examples

**Example 1:**
```
Input:  prob03("Pooh")
Output: Oh bother!
```

**Example 2:**
```
Input:  prob03("Piglet")
Output: Sorry! I don't know Piglet's catchphrase!
```

---

## Problem 4: Return Item

**Difficulty:** Easy

### Description

Implement a function `prob04()` that accepts a 0-indexed list `items` and a non-negative integer `x` and returns the element at index `x` in `items`. If `x` is not a valid index of `items`, return `None`.

### Function Signature

```python
def prob04(items, x):
    pass
```

### Examples

**Example 1:**
```
Input:  items = ["piglet", "pooh", "roo", "rabbit"], x = 2
Output: "roo"
```

**Example 2:**
```
Input:  items = ["piglet", "pooh", "roo", "rabbit"], x = 5
Output: None
```

---

## Problem 5: Total Honey

**Difficulty:** Easy

### Description

Winnie the Pooh wants to know how much honey he has. Write a function `prob05()` that accepts a list of integers `hunny_jars` and returns the sum of all elements in the list. Do not use the built-in function `sum()`.

### Function Signature

```python
def prob05(hunny_jars):
    pass
```

### Examples

**Example 1:**
```
Input:  hunny_jars = [2, 3, 4, 5]
Output: 14
```

**Example 2:**
```
Input:  hunny_jars = []
Output: 0
```

---

## Problem 6: Double Trouble

**Difficulty:** Easy

### Description

Help Winnie the Pooh double his honey! Write a function `prob06()` that accepts a list of integers `hunny_jars` as a parameter and multiplies each element in the list by two. Return the prob06 list.

### Function Signature

```python
def prob06(hunny_jars):
    pass
```

### Examples

**Example 1:**
```
Input:  hunny_jars = [1, 2, 3]
Output: [2, 4, 6]
```

---

## Problem 7: Poohsticks

**Difficulty:** Easy

### Description

Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them. They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.

Write a function `prob07()` to help Pooh and his friends determine how many players should move on to the next round. `prob07()` accepts a list of integers `race_times` and an integer `threshold` and returns the number of race times less than `threshold`.

### Function Signature

```python
def prob07(race_times, threshold):
    pass
```

### Examples

**Example 1:**
```
Input:  race_times = [1, 2, 3, 4, 5, 6], threshold = 4
Output: 3
```

**Example 2:**
```
Input:  race_times = [], threshold = 4
Output: 0
```

---

## Problem 8: Pooh's To Do's

**Difficulty:** Easy

### Description

Write a function `prob08()` that accepts a list of strings named `tasks`. The function should number and print each task on a new line using the format:

```
Pooh's To Dos:
1. Task 1
2. Task 2
...
```

### Function Signature

```python
def prob08(tasks):
    pass
```

### Examples

**Example 1:**
```
Input:  tasks = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
Output:
Pooh's To Dos:
1. Count all the bees in the hive
2. Chase all the clouds from the sky
3. Think
4. Stoutness Exercises
```

**Example 2:**
```
Input:  tasks = []
Output:
Pooh's To Dos:
```

---

## Problem 9: Pairs

**Difficulty:** Easy

### Description

Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. Write a function `prob09()` that accepts a list of integers `item_quantities`. Return `True` if each number in `item_quantities` is even. Return `False` otherwise.

### Function Signature

```python
def prob09(item_quantities):
    pass
```

### Examples

**Example 1:**
```
Input:  item_quantities = [2, 4, 6, 8]
Output: True
```

**Example 2:**
```
Input:  item_quantities = [1, 2, 3, 4]
Output: False
```

**Example 3:**
```
Input:  item_quantities = []
Output: True
```

---

## Problem 10: Split Haycorns

**Difficulty:** Medium

### Description

Piglet has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. Write a function `prob10()` to help Piglet determine the number of ways he can split his haycorns into even groups. `prob10()` accepts a positive integer `quantity` and returns a list of all divisors of `quantity`.

### Function Signature

```python
def prob10(quantity):
    pass
```

### Examples

**Example 1:**
```
Input:  quantity = 6
Output: [1, 2, 3, 6]
```

**Example 2:**
```
Input:  quantity = 1
Output: [1]
```

---

## Problem 11: T-I-Double Guh-ER

**Difficulty:** Easy

### Description

Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. Write a function `prob11()` that accepts a string `s`, and returns a new string with the letters `t`, `i`, `g`, `e`, and `r` removed from it.

### Function Signature

```python
def prob11(s):
    pass
```

### Examples

**Example 1:**
```
Input:  s = "suspicerous"
Output: "suspcous"
```

**Example 2:**
```
Input:  s = "Trigger"
Output: ""
```

**Example 3:**
```
Input:  s = "Hunny"
Output: "Hunny"
```

---

## Problem 12: Thistle Hunt

**Difficulty:** Easy

### Description

Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function `prob12()` that takes in a list of strings `items` and returns a list of the indices of any elements with value `"thistle"`. The indices in the resulting list should be ordered from least to greatest.

### Function Signature

```python
def prob12(items):
    pass
```

### Examples

**Example 1:**
```
Input:  items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
Output: [0, 3]
```

**Example 2:**
```
Input:  items = ["book", "bouncy ball", "leaf", "red balloon"]
Output: []
```

---
