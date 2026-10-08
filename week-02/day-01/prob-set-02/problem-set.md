# Problem Set: Dictionaries & Sets (Space Station) — Week 2, Day 1

---

## Problem 1: Space Crew

### Description

Given two lists of length `n`, `crew` and `position`, write a function `prob01()` that maps each space station crew member to their position on board the International Space Station.

Crew member `crew[i]` has job `position[i]` on board, where `0 <= i < n` and `len(crew) == len(position)`.

### Function Signature

```python
def prob01(crew, position):
    pass
```

### Examples

**Example 1:**
```
Input:  crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"],
        position = ["Commander", "Flight Engineer", "Flight Engineer", "Flight Engineer", "Flight Engineer"]
Output: {"Andreas Mogensen": "Commander", "Jasmin Moghbeli": "Flight Engineer", "Satoshi Furukawa": "Flight Engineer",
         "Loral O'Hara": "Flight Engineer", "Konstantin Borisov": "Flight Engineer"}
```

**Example 2:**
```
Input:  crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"],
        position = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]
Output: {"Michael Lopez-Alegria": "Commander", "Walter Villadei": "Mission Pilot",
         "Alper Gezeravci": "Mission Specialist", "Marcus Wandt": "Mission Specialist"}
```

---

## Problem 2: Space Encyclopedia

### Description

A dictionary `planets` maps planet names to a dictionary containing the planet's number of moons and orbital period. Write a function `prob02()` that accepts a string `planet_name` and returns a string of the form:

`Planet <planet_name> has an orbital period of <orbital period> Earth days and has <number of moons> moons.`

If `planet_name` is not a key in `planets`, return `"Sorry, I have no data on that planet."`.

`planets` is a module-level dictionary, not a parameter:

```python
planets = {
    "Mercury": {"Moons": 0, "Orbital Period": 88},
    "Earth": {"Moons": 1, "Orbital Period": 365.25},
    "Mars": {"Moons": 2, "Orbital Period": 687},
    "Jupiter": {"Moons": 79, "Orbital Period": 10592}
}
```

### Function Signature

```python
def prob02(planet_name):
    pass
```

### Examples

**Example 1:**
```
Input:  planet_name = "Jupiter"
Output: "Planet Jupiter has an orbital period of 10592 Earth days and has 79 moons."
```

**Example 2:**
```
Input:  planet_name = "Pluto"
Output: "Sorry, I have no data on that planet."
```

---

## Problem 3: Breathing Room

### Description

As part of your job as an astronaut, you perform routine safety checks. You are given a dictionary `oxygen_levels` that maps room names to current oxygen levels, and two integers `min_val` and `max_val` that define the acceptable range (inclusive). Write a function `prob03()` that returns a list of the room names whose oxygen levels are outside that range.

### Function Signature

```python
def prob03(oxygen_levels, min_val, max_val):
    pass
```

### Examples

**Example 1:**
```
Input:  oxygen_levels = {"Command Module": 21, "Habitation Module": 20, "Laboratory Module": 19, "Airlock": 22, "Storage Bay": 18},
        min_val = 19, max_val = 22
Output: ['Storage Bay']
```

---

## Problem 4: Experiment Analysis

### Description

Write a function `prob04()` that accepts two dictionaries `experiment1` and `experiment2` and returns a new dictionary containing only the key-value pairs found in `experiment1` but not in `experiment2`.

### Function Signature

```python
def prob04(experiment1, experiment2):
    pass
```

### Examples

**Example 1:**
```
Input:  experiment1 = {'temperature': 22, 'pressure': 101.3, 'humidity': 45},
        experiment2 = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}
Output: {'temperature': 22, 'humidity': 45}
```

---

## Problem 5: Name the Node

### Description

NASA asked the public to vote on a new name for one of the nodes in the International Space Station. Given a list of strings `votes`, where each string is one voter's suggested name, write a function `prob05()` that returns the suggestion with the most votes.

If there is a tie, return any of the tied suggestions.

### Function Signature

```python
def prob05(votes):
    pass
```

### Examples

**Example 1:**
```
Input:  votes = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
Output: "Colbert"
```

**Example 2:**
```
Input:  votes = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]
Output: "Serenity"
Explanation: "Colbert" and "Serenity" are both acceptable answers.
```

---

## Problem 6: Check if the Transmission is Complete

### Description

Ground control has sent a transmission containing important information. A **complete** transmission is one where every letter of the English alphabet appears at least once.

Given a string `transmission` containing only lowercase English letters, write a function `prob06()` that returns `True` if the transmission is complete, or `False` otherwise.

### Function Signature

```python
def prob06(transmission):
    """
    :type transmission: str
    :rtype: bool
    """
```

### Examples

**Example 1:**
```
Input:  transmission = "thequickbrownfoxjumpsoverthelazydog"
Output: True
```

**Example 2:**
```
Input:  transmission = "spacetravel"
Output: False
```

---

## Problem 7: Signal Pairs

### Description

Ground control is analyzing signal patterns received from different probes. You are given a 0-indexed list `signals` of distinct strings.

`signals[i]` can be paired with `signals[j]` if `signals[i]` equals the reverse of `signals[j]`, where `0 <= i < j < len(signals)`. Each string can belong to at most one pair.

Write a function `prob07()` that returns the maximum number of pairs that can be formed from `signals`.

### Function Signature

```python
def prob07(signals):
    pass
```

### Examples

**Example 1:**
```
Input:  signals = ["cd", "ac", "dc", "ca", "zz"]
Output: 2
```

**Example 2:**
```
Input:  signals = ["ab", "ba", "cc"]
Output: 1
```

**Example 3:**
```
Input:  signals = ["aa", "ab"]
Output: 0
```

### Constraints

- All strings in `signals` are distinct

---

## Problem 8: Find the Difference of Two Signal Arrays

### Description

You are given two 0-indexed integer lists `signals1` and `signals2`, representing signal data from two probes. Write a function `prob08()` that returns a list `answer` of size 2 where:

- `answer[0]` is a list of all distinct integers in `signals1` that are not present in `signals2`.
- `answer[1]` is a list of all distinct integers in `signals2` that are not present in `signals1`.

The integers in each list may be returned in any order.

Implement this pseudocode, then explain your implementation step by step:

1. Convert `signals1` and `signals2` to sets.
2. Find the difference between `set1` and `set2` and store it in `diff1`.
3. Find the difference between `set2` and `set1` and store it in `diff2`.
4. Return the list `[diff1, diff2]`.

### Function Signature

```python
def prob08(signals1, signals2):
    pass
```

### Examples

**Example 1:**
```
Input:  signals1 = [1, 2, 3], signals2 = [2, 4, 6]
Output: [[1, 3], [4, 6]]
```

**Example 2:**
```
Input:  signals1 = [1, 2, 3, 3], signals2 = [1, 1, 2, 2]
Output: [[3], []]
```

---

## Problem 9: Common Signals Between Space Probes

### Description

Two space probes have collected signals, represented by integer lists `signals1` and `signals2` of sizes `n` and `m`. Calculate:

- `answer1`: the number of indices `i` such that `signals1[i]` exists in `signals2`.
- `answer2`: the number of indices `j` such that `signals2[j]` exists in `signals1`.

Write a function `prob09()` that returns `[answer1, answer2]`.

### Function Signature

```python
def prob09(signals1, signals2):
    pass
```

### Examples

**Example 1:**
```
Input:  signals1 = [2, 3, 2], signals2 = [1, 2]
Output: [2, 1]
```

**Example 2:**
```
Input:  signals1 = [4, 3, 2, 3, 1], signals2 = [2, 2, 5, 2, 3, 6]
Output: [3, 4]
```

**Example 3:**
```
Input:  signals1 = [3, 4, 2, 3], signals2 = [1, 5]
Output: [0, 0]
```

---

## Problem 10: Common Signals Between Space Probes II

### Description

If you solved Problem 9 with dictionaries, solve it again with sets. If you solved it with sets, solve it again with dictionaries. Then compare the two solutions: is one better than the other? How so? Why or why not?

The function behaves exactly like Problem 9.

### Function Signature

```python
def prob10(signals1, signals2):
    pass
```

### Examples

**Example 1:**
```
Input:  signals1 = [2, 3, 2], signals2 = [1, 2]
Output: [2, 1]
```

**Example 2:**
```
Input:  signals1 = [4, 3, 2, 3, 1], signals2 = [2, 2, 5, 2, 3, 6]
Output: [3, 4]
```

**Example 3:**
```
Input:  signals1 = [3, 4, 2, 3], signals2 = [1, 5]
Output: [0, 0]
```

---

## Problem 11: Sort Signal Data (SKIPPED)

_Debugging/code-review problem — no new implementation._

### Description

Ground control needs to analyze the frequency of signal data received from different probes. Given a list of integers `signals`, sort it in increasing order of value frequency. If multiple values have the same frequency, sort them in decreasing order. Return the sorted list.

The code below is buggy or incomplete. Identify and fix the bugs, then perform a code review and suggest improvements.

### Starter Code

```python
def frequency_sort(signals):
    freq = {}
    for signal in signals:
        if signal in freq:
            freq[signal] += 1
        else:
            freq[signal] = 0

    sorted_signals = sorted(signals, key=lambda x: (freq[x], x))

    return sorted_signals
```

### Examples

**Example 1:**
```
Input:  signals = [1, 1, 2, 2, 2, 3]
Output: [3, 1, 1, 2, 2, 2]
```

**Example 2:**
```
Input:  signals = [2, 3, 1, 3, 2]
Output: [1, 3, 3, 2, 2]
```

**Example 3:**
```
Input:  signals = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]
```

---

## Problem 12: Final Communication Hub

### Description

You are given a list `paths`, where `paths[i] = [hubA, hubB]` means there is a direct communication path from `hubA` to `hubB`. Write a function `prob12()` that returns the final communication hub: the hub with no outgoing path to another hub.

The paths are guaranteed to form a line without any loops, so there is exactly one final communication hub.

### Function Signature

```python
def prob12(paths):
    pass
```

### Examples

**Example 1:**
```
Input:  paths = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
Output: "Europa"
```

**Example 2:**
```
Input:  paths = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
Output: "Delta"
```

**Example 3:**
```
Input:  paths = [["StationA", "StationZ"]]
Output: "StationZ"
```

---
