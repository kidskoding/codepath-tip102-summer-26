# Problem Set: Strings & Arrays (Batman) — Week 1, Day 1

---

## Problem 1: Batman

**Difficulty:** Easy

### Description

Write a function `batman()` that prints the string `"I am vengeance. I am the night. I am Batman!"`.

### Function Signature

```python
def batman():
    pass
```

### Examples

**Example 1:**
```
Input:  batman()
Output: I am vengeance. I am the night. I am Batman!
```

---

## Problem 2: Mad Libs

**Difficulty:** Easy

### Description

Write a function `madlib()` that accepts one parameter, a string `verb`. The function should print the sentence: `"I have one power. I never <verb>. - Batman"`.

### Function Signature

```python
def madlib(verb):
    pass
```

### Examples

**Example 1:**
```
Input:  madlib("give up")
Output: I have one power. I never give up. - Batman
```

**Example 2:**
```
Input:  madlib("nap")
Output: I have one power. I never nap. - Batman
```

---

## Problem 3: Trilogy

**Difficulty:** Easy

### Description

Write a function `trilogy()` that accepts an integer `year` and prints the title of the Batman trilogy movie released that year as outlined below.

| Year | Movie Title |
| --- | --- |
| 2005 | `"Batman Begins"` |
| 2008 | `"The Dark Knight"` |
| 2012 | `"The Dark Knight Rises"` |

If the given year does not match one of the years above, print `"Christopher Nolan did not release a Batman movie in <year>."`.

### Function Signature

```python
def trilogy(year):
    pass
```

### Examples

**Example 1:**
```
Input:  trilogy(2008)
Output: The Dark Knight
```

**Example 2:**
```
Input:  trilogy(1998)
Output: Christopher Nolan did not release a Batman movie in 1998.
```

---

## Problem 4: Last

**Difficulty:** Easy

### Description

Implement a function `get_last()` that accepts a list of items `items` and returns the last item in the list. If the list is empty, return `None`.

### Function Signature

```python
def get_last(items):
    pass
```

### Examples

**Example 1:**
```
Input:  items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
Output: "black adam"
```

**Example 2:**
```
Input:  items = []
Output: None
```

---

## Problem 5: Concatenate

**Difficulty:** Easy

### Description

Write a function `concatenate()` that takes in a list of strings `words` and returns a string `concatenated` that concatenates all elements in `words`.

### Function Signature

```python
def concatenate(words):
    pass
```

### Examples

**Example 1:**
```
Input:  words = ["vengeance", "darkness", "batman"]
Output: "vengeancedarknessbatman"
```

**Example 2:**
```
Input:  words = []
Output: ""
```

---

## Problem 6: Squared

**Difficulty:** Easy

### Description

Write a function `squared()` that accepts a list of integers `numbers` as a parameter and squares each item in the list. Return the squared list.

### Function Signature

```python
def squared(numbers):
    pass
```

### Examples

**Example 1:**
```
Input:  numbers = [1, 2, 3]
Output: [1, 4, 9]
```

---

## Problem 7: NaNaNa Batman!

**Difficulty:** Easy

### Description

Write a function `nanana_batman()` that accepts an integer `x` and prints the string `"nanana batman!"` where `"na"` is repeated `x` times. Do not use the `*` operator.

### Function Signature

```python
def nanana_batman(x):
    pass
```

### Examples

**Example 1:**
```
Input:  nanana_batman(6)
Output: nananananana batman!
```

**Example 2:**
```
Input:  nanana_batman(0)
Output: batman!
```

---

## Problem 8: Find the Villain

**Difficulty:** Easy

### Description

Write a function `find_villain()` that accepts a list `crowd` and a value `villain` as parameters and returns a list of all indices where the villain is found hiding in the crowd.

### Function Signature

```python
def find_villain(crowd, villain):
    pass
```

### Examples

**Example 1:**
```
Input:  crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker'], villain = 'The Joker'
Output: [1, 4, 6]
```

---

## Problem 9: Odd

**Difficulty:** Easy

### Description

Write a function `get_odds()` that takes in a list of integers `nums` and returns a new list containing all the odd numbers in `nums`.

### Function Signature

```python
def get_odds(nums):
    pass
```

### Examples

**Example 1:**
```
Input:  nums = [1, 2, 3, 4]
Output: [1, 3]
```

**Example 2:**
```
Input:  nums = [2, 4, 6, 8]
Output: []
```

---

## Problem 10: Up and Down

**Difficulty:** Easy

### Description

Write a function `up_and_down()` that accepts a list of integers `lst` as a parameter. The function should return the number of odd numbers minus the number of even numbers in the list.

### Function Signature

```python
def up_and_down(lst):
    pass
```

### Examples

**Example 1:**
```
Input:  lst = [1, 2, 3]
Output: 1
```

**Example 2:**
```
Input:  lst = [1, 3, 5]
Output: 3
```

**Example 3:**
```
Input:  lst = [2, 4, 10, 2]
Output: -4
```

---

## Problem 11: Running Sum

**Difficulty:** Medium

### Description

Write a function `running_sum()` that accepts a list of integers `superhero_stats` representing the number of crimes Batman has stopped each month in Gotham City. The function should modify the list to return the running sum such that `superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i])`. You must modify the list in place; you may not create any new lists as part of your solution.

### Function Signature

```python
def running_sum(superhero_stats):
    pass
```

### Examples

**Example 1:**
```
Input:  superhero_stats = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
```

**Example 2:**
```
Input:  superhero_stats = [1, 1, 1, 1, 1]
Output: [1, 2, 3, 4, 5]
```

**Example 3:**
```
Input:  superhero_stats = [3, 1, 2, 10, 1]
Output: [3, 4, 6, 16, 17]
```

---

## Problem 12: Shuffle

**Difficulty:** Medium

### Description

Write a function `shuffle()` that accepts a list `cards` of `2n` elements in the form `[x1,x2,...,xn,y1,y2,...,yn]`. Return the list in the form `[x1,y1,x2,y2,...,xn,yn]`.

### Function Signature

```python
def shuffle(cards):
    pass
```

### Examples

**Example 1:**
```
Input:  cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
Output: ['Joker', 3, 'Queen', 'Ace', 2, 7]
```

**Example 2:**
```
Input:  cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
Output: [9, 'Joker', 2, 3, 3, 2, 'Joker', 9]
```

**Example 3:**
```
Input:  cards = [10, 10, 2, 2]
Output: [10, 2, 10, 2]
```

---
