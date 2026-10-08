# Problem Set: Strings & Arrays (Hundred Acre Wood) — Week 1, Day 2

---

## Problem 1: Reverse Sentence

### Description

Write a function `prob01()` that takes in a string `sentence` and returns the sentence with the order of the words reversed. The sentence contains only alphabetic characters and spaces separating the words. If there is only one word in the sentence, return the original string.

### Function Signature

```python
def prob01(sentence):
    pass
```

### Examples

**Example 1:**
```
Input:  sentence = "tubby little cubby all stuffed with fluff"
Output: "fluff with stuffed all cubby little tubby"
```

**Example 2:**
```
Input:  sentence = "Pooh"
Output: "Pooh"
```

---

## Problem 2: Goldilocks Number

### Description

Goldilocks finds an enticing list of numbers in the Three Bears' house. She doesn't want a number that's too high or too low — she wants one that's juuust right.

Write a function `prob02()` that takes in a list of distinct positive integers `nums` and returns any number from the list that is neither the minimum nor the maximum value, or `-1` if there is no such number.

### Function Signature

```python
def prob02(nums):
    pass
```

### Examples

**Example 1:**
```
Input:  nums = [3, 2, 1, 4]
Output: 2
```

**Example 2:**
```
Input:  nums = [1, 2]
Output: -1
```

**Example 3:**
```
Input:  nums = [2, 1, 3]
Output: 2
```

### Constraints

- All values in `nums` are distinct positive integers

---

## Problem 3: Delete Minimum

### Description

Pooh eats all of his hunny jars in order from smallest to largest. Given a list of integers `hunny_jar_sizes`, write a function `prob03()` that repeatedly removes the minimum element until the list is empty. Return a new list of the elements of `hunny_jar_sizes` in the order in which they were removed.

### Function Signature

```python
def prob03(hunny_jar_sizes):
    pass
```

### Examples

**Example 1:**
```
Input:  hunny_jar_sizes = [5, 3, 2, 4, 1]
Output: [1, 2, 3, 4, 5]
```

**Example 2:**
```
Input:  hunny_jar_sizes = [5, 2, 1, 8, 2]
Output: [1, 2, 2, 5, 8]
```

---

## Problem 4: Sum of Digits

### Description

Write a function `prob04()` that accepts an integer `num` and returns the sum of `num`'s digits.

### Function Signature

```python
def prob04(num):
    pass
```

### Examples

**Example 1:**
```
Input:  num = 423
Output: 9
Explanation: 4 + 2 + 3 = 9
```

**Example 2:**
```
Input:  num = 4
Output: 4
```

---

## Problem 5: Bouncy, Flouncy, Trouncy, Pouncy

### Description

Tigger has developed a new programming language, Tiger, with only four operations and one variable, `tigger`.

- `"bouncy"` and `"flouncy"` both increment `tigger` by 1.
- `"trouncy"` and `"pouncy"` both decrement `tigger` by 1.

Initially, `tigger` is `1` because he's the only tigger around. Given a list of strings `operations`, write a function `prob05()` that returns the final value of `tigger` after performing all the operations.

### Function Signature

```python
def prob05(operations):
    pass
```

### Examples

**Example 1:**
```
Input:  operations = ["trouncy", "flouncy", "flouncy"]
Output: 2
```

**Example 2:**
```
Input:  operations = ["bouncy", "bouncy", "flouncy"]
Output: 4
```

---

## Problem 6: Acronym

### Description

Given a list of strings `words` and a string `s`, write a function `prob06()` that returns `True` if `s` is an acronym of `words` and `False` otherwise.

`s` is an acronym of `words` if it can be formed by concatenating the first character of each string in `words`, in order. For example, `"pb"` can be formed from `["pooh", "bear"]`, but not from `["bear", "pooh"]`.

### Function Signature

```python
def prob06(words, s):
    pass
```

### Examples

**Example 1:**
```
Input:  words = ["christopher", "robin", "milne"], s = "crm"
Output: True
```

---

## Problem 7: Good Things Come in Threes

### Description

Write a function `prob07()` that accepts an integer list `nums`. In one operation, you can add or subtract 1 from any element of `nums`. Return the minimum number of operations needed to make every element of `nums` divisible by 3.

### Function Signature

```python
def prob07(nums):
    pass
```

### Examples

**Example 1:**
```
Input:  nums = [1, 2, 3, 4]
Output: 3
```

**Example 2:**
```
Input:  nums = [3, 6, 9]
Output: 0
```

---

## Problem 8: Exclusive Elements

### Description

Given two lists `lst1` and `lst2`, write a function `prob08()` that returns a new list containing the elements that are in `lst1` but not in `lst2`, followed by the elements that are in `lst2` but not in `lst1`.

### Function Signature

```python
def prob08(lst1, lst2):
    pass
```

### Examples

**Example 1:**
```
Input:  lst1 = ["pooh", "roo", "piglet"], lst2 = ["piglet", "eeyore", "owl"]
Output: ["pooh", "roo", "eeyore", "owl"]
```

**Example 2:**
```
Input:  lst1 = ["pooh", "roo"], lst2 = ["piglet", "eeyore", "owl", "kanga"]
Output: ["pooh", "roo", "piglet", "eeyore", "owl", "kanga"]
```

**Example 3:**
```
Input:  lst1 = ["pooh", "roo", "piglet"], lst2 = ["pooh", "roo", "piglet"]
Output: []
```

---

## Problem 9: Merge Strings Alternately

### Description

Write a function `prob09()` that accepts two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If one string is longer than the other, append its remaining letters to the end of the merged string.

Return the merged string.

### Function Signature

```python
def prob09(word1, word2):
    pass
```

### Examples

**Example 1:**
```
Input:  word1 = "wol", word2 = "oze"
Output: "woozle"
```

**Example 2:**
```
Input:  word1 = "hfa", word2 = "eflump"
Output: "heffalump"
```

**Example 3:**
```
Input:  word1 = "eyre", word2 = "eo"
Output: "eeyore"
```

---

## Problem 10: Eeyore's House

### Description

Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose lengths are the right proportion. Write a function `prob10()` that accepts two integer lists `pile1` and `pile2`, where each integer is the length of a stick, and a positive integer `k`. Return the number of good pairs.

A pair `(i, j)` is **good** if `pile1[i]` is divisible by `pile2[j] * k`.

### Function Signature

```python
def prob10(pile1, pile2, k):
    pass
```

### Examples

**Example 1:**
```
Input:  pile1 = [1, 3, 4], pile2 = [1, 3, 4], k = 1
Output: 5
```

**Example 2:**
```
Input:  pile1 = [1, 2, 4, 12], pile2 = [2, 4], k = 3
Output: 2
```

### Constraints

- `0 <= i <= len(pile1) - 1`
- `0 <= j <= len(pile2) - 1`
- `k` is a positive integer

---
