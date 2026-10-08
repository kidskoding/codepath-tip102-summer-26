# Problem Set: Dynamic Programming (Pokémon) — Week 12, Day 1

---

## Problem 1: Counting Pikachu's Thunderbolt Charges

### Description

Pikachu's Thunderbolt charges for a number equal the number of `1`s in its binary form. Given an integer `n`, write a function `prob01()` that returns a list `ans` of length `n + 1`, where `ans[i]` is the number of `1`s in the binary form of `i`, for every `0 <= i <= n`.

### Function Signature

```python
def prob01(n: int) -> list[int]:
    pass
```

### Examples

**Example 1:**
```
Input:  n = 2
Output: [0, 1, 1]
Explanation: 0 is 0, 1 is 1, and 2 is 10 in binary.
```

**Example 2:**
```
Input:  n = 5
Output: [0, 1, 1, 2, 1, 2]
```

**Example 3:**
```
Input:  n = 10
Output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
```

---

## Problem 2: Gary's Pokédollar Trading Strategy

### Description

Given a list `prices`, where `prices[i]` is the price of a Pokéball on day `i`, write a function `prob02()` that returns the maximum profit from buying on one day and selling on a later day. If no profit is possible, return `0`.

### Function Signature

```python
def prob02(prices: list[int]) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy at 1 and sell at 6.
```

**Example 2:**
```
Input:  prices = [7, 6, 4, 3, 1]
Output: 0
```

---

## Problem 3: Caterpie's Evolution Sequence

### Description

The list `steps` holds positive integers, each the difficulty of a training step. A subarray (contiguous) is **strictly increasing** if each element is greater than the one before it. Write a function `prob03()` that uses dynamic programming to return the number of strictly increasing subarrays.

### Function Signature

```python
def prob03(steps: list[int]) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  steps = [1, 3, 5, 4, 4, 6]
Output: 10
Explanation: 6 subarrays of length 1, then [1,3], [3,5], [4,6], and [1,3,5]: 6 + 3 + 1 = 10.
```

**Example 2:**
```
Input:  steps = [1, 2, 3, 4, 5]
Output: 15
Explanation: Every subarray is strictly increasing.
```

---

## Problem 4: Ash's Team Battle Strategy

### Description

Ash has a list of Pokémon names `pokemon` and a list `types` of the same length, where each type is `0` (physical attacker) or `1` (special attacker). He wants the longest subsequence of Pokémon whose types alternate (no two consecutive team members share a type).

Write a function `prob04()` that uses dynamic programming to return a list of the names in a longest alternating subsequence. If there are several, return any of them.

### Function Signature

```python
def prob04(pokemon: list[str], types: list[int]) -> list[str]:
    pass
```

### Examples

**Example 1:**
```
Input:  pokemon = ["Pikachu", "Bulbasaur", "Charmander"], types = [0, 0, 1]
Output: ['Pikachu', 'Charmander']
Explanation: ['Bulbasaur', 'Charmander'] is also accepted. The longest length is 2.
```

**Example 2:**
```
Input:  pokemon = ["Squirtle", "Pidgey", "Rattata", "Gengar"], types = [1, 0, 1, 1]
Output: ['Squirtle', 'Pidgey', 'Rattata']
Explanation: ['Squirtle', 'Pidgey', 'Gengar'] is also accepted. The longest length is 3.
```

---

## Problem 5: Team Rocket's Heist Plan

### Description

Team Rocket is robbing a row of Pokémon Centers. The list `pokeballs` gives the rare Pokéballs in each center. Robbing two adjacent centers on the same night alerts Officer Jenny. Write a function `prob05()` that returns the most Pokéballs they can steal without robbing two adjacent centers.

### Function Signature

```python
def prob05(pokeballs: list[int]) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  pokeballs = [1, 2, 3, 1]
Output: 4
Explanation: Rob centers 1 and 3: 1 + 3 = 4.
```

**Example 2:**
```
Input:  pokeballs = [2, 7, 9, 3, 1]
Output: 12
Explanation: Rob centers 1, 3, and 5: 2 + 9 + 1 = 12.
```

---

## Problem 6: Mewtwo's Genetic Fusion

### Description

Write a function `prob06()` that returns `True` if the string `dna3` can be formed by **interleaving** `dna1` and `dna2`, and `False` otherwise. An interleaving splits both strings into substrings and merges them alternately, keeping each string's characters in their original order, and uses every character of both strings.

_2-D dynamic programming is an extra challenge for TIP102 (in scope for TIP103)._

### Function Signature

```python
def prob06(dna1: str, dna2: str, dna3: str) -> bool:
    pass
```

### Examples

**Example 1:**
```
Input:  dna1 = "aabcc", dna2 = "dbbca", dna3 = "aadbbcbcac"
Output: True
Explanation: "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
```

**Example 2:**
```
Input:  dna1 = "aabcc", dna2 = "dbbca", dna3 = "aadbbbaccc"
Output: False
```

**Example 3:**
```
Input:  dna1 = "", dna2 = "", dna3 = ""
Output: True
```

---
