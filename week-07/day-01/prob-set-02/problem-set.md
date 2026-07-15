# Problem Set #2: Recursion — Week 7, Day 1

---

## Problem 1: Calculating Village Size

**Difficulty:** Easy

### Description

In the kingdom of Codepathia, the queen determines how many resources to distribute to a village based on its class. A village's class is equal to the number of digits in its population.

Given an integer `population`, write a function `get_village_class()` that returns the number of digits in `population`. Implement it two ways — once iteratively and once recursively.

### Function Signature

```python
def get_village_class_iterative(population):
    pass

def get_village_class_recursive(population):
    pass
```

### Examples

**Example 1:**
```
Input:  population = 432
Output: 3
```

**Example 2:**
```
Input:  population = 9
Output: 1
```

---

## Problem 2: Counting the Castle Walls

**Difficulty:** Easy

### Description

In a faraway kingdom, a castle is surrounded by multiple defensive walls, where each wall is nested within another. Given a list of lists `walls` where each list `[]` represents a wall, write a recursive function `prob02()` that returns the total number of walls.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

### Function Signature

```python
def prob02(walls):
    pass
```

### Examples

**Example 1:**
```
Input:  walls = ["outer", ["inner", ["keep", []]]]
Output: 4
```

**Example 2:**
```
Input:  walls = []
Output: 1
```

---

## Problem 3: Reversing a Scroll

**Difficulty:** Easy

### Description

A wizard is deciphering an ancient scroll and needs to reverse the letters in a word to reveal a hidden message. Write a recursive function to reverse the letters in a given `scroll` and return the reversed scroll. Assume `scroll` only contains alphabetic characters.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

### Function Signature

```python
def prob03(scroll):
    pass
```

### Examples

**Example 1:**
```
Input:  scroll = "cigam"
Output: "magic"
```

**Example 2:**
```
Input:  scroll = "lleps"
Output: "spell"
```

---

## Problem 4: Palindromic Name

**Difficulty:** Easy

### Description

Queen Ada is superstitious and believes her children will only have good fortune if their name is symmetrical and reads the same forward and backward. Write a recursive function that takes in a string comprised of only lowercase alphabetic characters `name` and returns `True` if the name is palindromic and `False` otherwise.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

### Function Signature

```python
def prob04(name):
    pass
```

### Examples

**Example 1:**
```
Input:  name = "eve"
Output: True
```

**Example 2:**
```
Input:  name = "ling"
Output: False
```

**Example 3:**
```
Input:  name = ""
Output: True
```

---

## Problem 5: Doubling the Power of a Spell

**Difficulty:** Easy

### Description

The court magician is practicing a spell that doubles its power with each incantation. Given an integer `initial_power` and a non-negative integer `n`, write a recursive function that doubles `initial_power` `n` times.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

### Function Signature

```python
def prob05(initial_power, n):
    pass
```

### Examples

**Example 1:**
```
Input:  initial_power = 5, n = 3
Output: 40
```
Explanation: 5 doubled 3 times: 5 -> 10 -> 20 -> 40

**Example 2:**
```
Input:  initial_power = 7, n = 2
Output: 28
```
Explanation: 7 doubled 2 times: 7 -> 14 -> 28

---

## Problem 6: Checking the Knight's Path

**Difficulty:** Easy

### Description

A knight is traveling along a path marked by stones, and each stone has a number on it. The knight must check if the numbers on the stones form a strictly increasing sequence. Write a recursive function to determine if the sequence is strictly increasing.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

### Function Signature

```python
def prob06(path):
    pass
```

### Examples

**Example 1:**
```
Input:  path = [1, 2, 3, 4, 5]
Output: True
```

**Example 2:**
```
Input:  path = [3, 5, 2, 8]
Output: False
```

---

## Problem 7: Finding the Longest Winning Streak

**Difficulty:** Medium

### Description

In the kingdom's grand tournament, knights compete in a series of challenges. A knight's performance in the challenge is represented by a string `challenges`, where a success is represented by an `S` and each other outcome (like a draw or loss) is represented by an `O`. Write a recursive function to find the length of the longest consecutive streak of successful challenges (`S`).

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

### Function Signature

```python
def prob07(challenges, current_length=0, max_length=0):
    pass
```

### Examples

**Example 1:**
```
Input:  challenges = "SSOSSS"
Output: 3
```

**Example 2:**
```
Input:  challenges = "SOSOSOSO"
Output: 1
```

---

## Problem 8: Weaving Spells

**Difficulty:** Medium

### Description

A magician can double a spell's power if they merge two incantations together. Given the heads of two linked lists `spell_a` and `spell_b` where each node in the lists contains a spell segment, write a recursive function `prob08()` that weaves the spells in the pattern:

```
a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...
```

Return the head of the woven list.

### Function Signature

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def prob08(spell_a, spell_b):
    pass
```

### Examples

**Example 1:**
```
Input:  spell_a: A -> C -> E
        spell_b: B -> D -> F
Output: A -> B -> C -> D -> E -> F
```

---

## Problem 9: Weaving Spells II (SKIPPED)

_Discussion/comparison problem — no implementation._

Compare your recursive `prob08()` from Problem 8 to the iterative solution provided in the source, and discuss with your podmates which you prefer.
