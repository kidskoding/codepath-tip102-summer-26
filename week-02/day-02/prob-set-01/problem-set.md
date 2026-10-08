# Problem Set: Dictionaries & Sets (Wildlife Conservation) — Week 2, Day 2

---

## Problem 1: Most Endangered Species

### Description

You are working on a wildlife conservation database. Write a function `prob01()` that returns the species with the highest conservation priority based on its population.

The function takes a list of dictionaries `species_list`. Each dictionary holds data for one species: its name, habitat, and wild population. Return the name of the species with the lowest population.

If multiple species share the lowest population, return the one with the lowest index.

### Function Signature

```python
def prob01(species_list):
    pass
```

### Examples

**Example 1:**
```
Input:  species_list = [
            {"name": "Amur Leopard", "habitat": "Temperate forests", "population": 84},
            {"name": "Javan Rhino", "habitat": "Tropical forests", "population": 72},
            {"name": "Vaquita", "habitat": "Marine", "population": 10}
        ]
Output: "Vaquita"
```

---

## Problem 2: Identifying Endangered Species

### Description

The string `endangered_species` represents species considered endangered; each character is a different endangered species. The string `observed_species` is a record of all species observed in a region; each character is one observed species.

Write a function `prob02()` that returns how many of the observed species instances are also endangered.

Species are case-sensitive, so `"a"` is a different species from `"A"`.

### Function Signature

```python
def prob02(endangered_species, observed_species):
    pass
```

### Examples

**Example 1:**
```
Input:  endangered_species = "aA", observed_species = "aAAbbbb"
Output: 3
Explanation: 'a' and 'A' are endangered. 'a' appears once and 'A' appears twice.
```

**Example 2:**
```
Input:  endangered_species = "z", observed_species = "ZZ"
Output: 0
```

---

## Problem 3: Navigating the Research Station

### Description

In a wildlife research station, each letter of the alphabet is a different observation point, laid out in a single row. The string `station_layout` of length 26 gives the layout of these points (indexed 0 to 25). You start at the first observation point (index 0). You must visit points in the order given by the string `observations`.

Moving from the point at index `i` to the point at index `j` takes `|i - j|` time.

Write a function `prob03()` that returns the total time it takes to visit all the required observation points in the given order.

### Function Signature

```python
def prob03(station_layout, observations):
    pass
```

### Examples

**Example 1:**
```
Input:  station_layout = "pqrstuvwxyzabcdefghijklmno", observations = "wildlife"
Output: 45
```

**Example 2:**
```
Input:  station_layout = "abcdefghijklmnopqrstuvwxyz", observations = "cba"
Output: 4
Explanation: Move from 0 to 2 to observe 'c', then to 1 for 'b', then to 0 for 'a'.
Total time = 2 + 1 + 1 = 4.
```

### Constraints

- `len(station_layout) == 26` and it contains each lowercase letter exactly once

---

## Problem 4: Prioritizing Endangered Species Observations

### Description

You have two lists, `observed_species` and `priority_species`. The elements of `priority_species` are distinct, and every element of `priority_species` is also in `observed_species`.

Write a function `prob04()` that sorts `observed_species` so the relative order of its items matches the order in `priority_species`. Species that do not appear in `priority_species` go at the end, in ascending order.

### Function Signature

```python
def prob04(observed_species, priority_species):
    pass
```

### Examples

**Example 1:**
```
Input:  observed_species = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"],
        priority_species = ["🐯", "🦌", "🐘", "🦁"]
Output: ["🐯", "🐯", "🐯", "🦌", "🐘", "🦁", "🦁", "🐍", "🐻", "🐼", "🦑"]
```

**Example 2:**
```
Input:  observed_species = ["bluejay", "sparrow", "cardinal", "robin", "crow"],
        priority_species = ["cardinal", "sparrow", "bluejay"]
Output: ["cardinal", "sparrow", "bluejay", "crow", "robin"]
```

---

## Problem 5: Calculating Conservation Statistics

### Description

You are given a 0-indexed integer list `species_populations` of even length. Each element is the population of one species in a wildlife reserve.

While `species_populations` is not empty, repeat:

1. Find the species with the minimum population and remove it.
2. Find the species with the maximum population and remove it.
3. Calculate the average population of the two removed species.

The average of `a` and `b` is `(a + b) / 2`. For example, the average of 200 and 300 is 250.

Write a function `prob05()` that returns the number of distinct averages calculated by this process. When there is a tie for minimum or maximum, any of the tied values can be removed.

### Function Signature

```python
def prob05(species_populations):
    pass
```

### Examples

**Example 1:**
```
Input:  species_populations = [4, 1, 4, 0, 3, 5]
Output: 2
Explanation:
1. Remove 0 and 5. The average is (0 + 5) / 2 = 2.5. Now the list is [4, 1, 4, 3].
2. Remove 1 and 4. The average is (1 + 4) / 2 = 2.5. Now the list is [4, 3].
3. Remove 3 and 4. The average is (3 + 4) / 2 = 3.5.
There are 2 distinct values among 2.5, 2.5, and 3.5.
```

**Example 2:**
```
Input:  species_populations = [1, 100]
Output: 1
Explanation: Only one average is calculated, after removing 1 and 100.
```

### Constraints

- `len(species_populations)` is even

---

## Problem 6: Wildlife Reintroduction

### Description

Your research center is ready to reintroduce endangered species into their native habitats. You are given two 0-indexed strings `raised_species` and `target_species`. `raised_species` lists the species available to release, where each character is a different species. `target_species` is a specific sequence of species you want to form and release together.

You can take species from `raised_species` and rearrange them to form new sequences. Write a function `prob06()` that returns the maximum number of copies of `target_species` you can form this way.

### Function Signature

```python
def prob06(raised_species, target_species):
    pass
```

### Examples

**Example 1:**
```
Input:  raised_species = "abcba", target_species = "abc"
Output: 1
Explanation: Take the letters at indices 0, 1, and 2 to make one copy of "abc".
The extra 'a' and 'b' at indices 3 and 4 can't make a second copy because the only 'c' is used.
```

**Example 2:**
```
Input:  raised_species = "aaaaabbbbcc", target_species = "abc"
Output: 2
Explanation: Take indices 0, 5, and 9 for one copy, and indices 1, 6, and 10 for a second.
After that there are no more 'c' letters.
```

---

## Problem 7: Count Unique Species

### Description

You are given a string `ecosystem_data` of digits and lowercase English letters. The digits are observed counts of species in a protected ecosystem.

Replace every non-digit character with a space. For example, `"f123de34g8hi34"` becomes `" 123  34 8  34"`. You are left with species counts separated by at least one space: `"123"`, `"34"`, `"8"`, and `"34"`.

Write a function `prob07()` that returns the number of unique species counts after the replacement.

Two counts are different if their decimal representations without leading zeros are different.

### Function Signature

```python
def prob07(ecosystem_data):
    pass
```

### Examples

**Example 1:**
```
Input:  ecosystem_data = "f123de34g8hi34"
Output: 3
```

**Example 2:**
```
Input:  ecosystem_data = "species1234forest234"
Output: 2
```

**Example 3:**
```
Input:  ecosystem_data = "x1y01z001"
Output: 1
```

---

## Problem 8: Equivalent Species Pairs

### Description

Researchers are analyzing pairs of species observed together. Each pair is a list `[a, b]`.

Pair `[a, b]` is **equivalent** to pair `[c, d]` if and only if `(a == c and b == d)` or `(a == d and b == c)`. In other words, order within a pair does not matter.

Write a function `prob08()` that returns the number of equivalent pairs `(i, j)` with `i < j` in the list `species_pairs`.

### Function Signature

```python
def prob08(species_pairs):
    pass
```

### Examples

**Example 1:**
```
Input:  species_pairs = [[1, 2], [2, 1], [3, 4], [5, 6]]
Output: 1
```

**Example 2:**
```
Input:  species_pairs = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
Output: 3
```

---
