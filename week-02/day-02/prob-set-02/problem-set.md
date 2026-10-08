# Problem Set: Dictionaries & Sets (Travel) — Week 2, Day 2

---

## Problem 1: Filter Destinations

### Description

You are planning an epic trip and have a dictionary `destinations` that maps destinations to their rating scores. You want to visit only the best-rated ones. Write a function `prob01()` that takes `destinations` and a `rating_threshold`, removes every destination with a rating strictly below `rating_threshold`, and returns the updated dictionary.

### Function Signature

```python
def prob01(destinations, rating_threshold):
    pass
```

### Examples

**Example 1:**
```
Input:  destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}, rating_threshold = 4.0
Output: {"Paris": 4.8, "Addis Ababa": 4.9}
```

**Example 2:**
```
Input:  destinations = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}, rating_threshold = 4.9
Output: {}
```

---

## Problem 2: Unique Travel Souvenirs

### Description

You have a list of strings `souvenirs`, where each string is a type of souvenir. Write a function `prob02()` that returns `True` if the number of occurrences of each souvenir type is unique, or `False` otherwise.

### Function Signature

```python
def prob02(souvenirs):
    pass
```

### Examples

**Example 1:**
```
Input:  souvenirs = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
Output: True
Explanation: "keychain" occurs 3 times, "hat" 2 times, and "postcard" once. No two types share a count.
```

**Example 2:**
```
Input:  souvenirs = ["postcard", "postcard", "postcard", "postcard"]
Output: True
Explanation: There is only one count (4), so it is unique.
```

**Example 3:**
```
Input:  souvenirs = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]
Output: False
Explanation: Every item occurs once, so the counts are not unique.
```

---

## Problem 3: Secret Beach

### Description

A local gives you a coded message with the name of a secret beach. You are given strings `key` (a cipher key) and `message` (the secret message). Decode the message as follows:

1. Use the first appearance of each of the 26 lowercase English letters in `key` as the order of the substitution table.
2. Align the substitution table with the regular English alphabet.
3. Substitute each letter in `message` using the table.
4. Spaces `' '` stay as spaces.

For example, `key = "travel the world"` gives the partial table `'t' -> 'a'`, `'r' -> 'b'`, `'a' -> 'c'`, `'v' -> 'd'`, `'e' -> 'e'`, `'l' -> 'f'`, `'h' -> 'g'`, `'w' -> 'h'`, `'o' -> 'i'`, `'d' -> 'j'`. (A real key contains every letter at least once.)

Write a function `prob03()` that accepts `key` and `message` and returns the decoded message.

### Function Signature

```python
def prob03(key, message):
    pass
```

### Examples

**Example 1:**
```
Input:  key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
```

**Example 2:**
```
Input:  key = "eljuxhpwnyrdgtqkviszcfmabo", message = "hntu depcte lxejw lxwntu zwx piqfx"
Output: "find laguna beach behind the grove"
```

### Constraints

- `key` contains every lowercase English letter at least once

---

## Problem 4: Longest Harmonious Travel Sequence (SKIPPED)

_Debugging problem — no new implementation._

### Description

A **harmonious** travel sequence is one where the difference between its maximum and minimum ratings is exactly 1. Given an integer list `ratings`, return the length of the longest harmonious subsequence. A subsequence is derived by deleting some or no elements without changing the order of the rest.

The code below is partially implemented and buggy. Identify and fix the bugs so the solution works correctly.

### Starter Code

```python
def find_longest_harmonious_travel_sequence(ratings):
    # Initialize a dictionary to store the frequency of each rating
    frequency = {}

    # Count the occurrences of each rating
    for rating in ratings:
        frequency[rating] += 1

    max_length = 0

    # Find the longest harmonious sequence
    for rating in frequency:
        if rating + 1 in frequency:
            max_length = max(max_length,
                        frequency[rating] + frequency[rating - 1])

    return max_length
```

### Examples

**Example 1:**
```
Input:  ratings = [1, 3, 2, 2, 5, 2, 3, 7]
Output: 5
```

**Example 2:**
```
Input:  ratings = [1, 2, 3, 4]
Output: 2
```

**Example 3:**
```
Input:  ratings = [1, 1, 1, 1]
Output: 0
```

---

## Problem 5: Check if All Destinations in a Route are Covered

### Description

You are given a 2D integer list `trips` and two integers `start_dest` and `end_dest`. Each `trips[i] = [start_i, end_i]` is an inclusive travel interval.

A destination `x` is covered by trip `trips[i]` if `start_i <= x <= end_i`.

Write a function `prob05()` that returns `True` if every destination in the inclusive route `[start_dest, end_dest]` is covered by at least one trip, and `False` otherwise.

### Function Signature

```python
def prob05(trips, start_dest, end_dest):
    pass
```

### Examples

**Example 1:**
```
Input:  trips = [[1, 2], [3, 4], [5, 6]], start_dest = 2, end_dest = 5
Output: True
```

**Example 2:**
```
Input:  trips = [[1, 10], [10, 20]], start_dest = 21, end_dest = 21
Output: False
```

**Example 3:**
```
Input:  trips = [[1, 2], [3, 5]], start_dest = 2, end_dest = 5
Output: True
```

---

## Problem 6: Most Popular Even Destination

### Description

Given a list of integers `destinations`, where each integer is a destination's popularity score, write a function `prob06()` that returns the most frequent even value.

If there is a tie, return the smallest one. If there is no even value, return `-1`.

### Function Signature

```python
def prob06(destinations):
    pass
```

### Examples

**Example 1:**
```
Input:  destinations = [0, 1, 2, 2, 4, 4, 1]
Output: 2
```

**Example 2:**
```
Input:  destinations = [4, 4, 4, 9, 2, 4]
Output: 4
```

**Example 3:**
```
Input:  destinations = [29, 47, 21, 41, 13, 37, 25, 7]
Output: -1
```

---

## Problem 7: Check if Itinerary is Valid

### Description

You are given an `itinerary`: a list of cities, each represented by an integer. An itinerary is **valid** if it is a permutation of the template `base[n]`.

`base[n]` is `[1, 2, ..., n - 1, n, n]`: a list of length `n + 1` that contains `1` to `n - 1` exactly once and `n` twice. For example, `base[1] = [1, 1]` and `base[3] = [1, 2, 3, 3]`.

Write a function `prob07()` that returns `True` if the itinerary is valid, and `False` otherwise.

A permutation is a rearrangement of elements. For example, `[3, 2, 1]` and `[2, 3, 1]` are both permutations of `1, 2, 3`.

### Function Signature

```python
def prob07(itinerary):
    pass
```

### Examples

**Example 1:**
```
Input:  itinerary = [2, 1, 3]
Output: False
Explanation: The maximum element is 3, so the only candidate is n = 3. base[3] has four elements,
but the itinerary has three, so it can't be a permutation of base[3] = [1, 2, 3, 3].
```

**Example 2:**
```
Input:  itinerary = [1, 3, 3, 2]
Output: True
Explanation: The maximum element is 3, so the only candidate is n = 3. Swapping the second and
fourth elements gives base[3] = [1, 2, 3, 3].
```

**Example 3:**
```
Input:  itinerary = [1, 1]
Output: True
Explanation: The maximum element is 1, so the only candidate is n = 1, and the itinerary is base[1] = [1, 1].
```

---

## Problem 8: Finding Common Tourist Attractions with Least Travel Time

### Description

Given two lists of tourist attractions, `tourist_list1` and `tourist_list2`, find the common attractions with the least total travel time.

A **common** attraction appears in both lists. If a common attraction is at `tourist_list1[i]` and `tourist_list2[j]`, its total travel time is `i + j`. The common attractions with the least total travel time are those whose `i + j` is the minimum among all common attractions.

Write a function `prob08()` that returns all common attractions with the least total travel time, in any order.

### Function Signature

```python
def prob08(tourist_list1, tourist_list2):
    pass
```

### Examples

**Example 1:**
```
Input:  tourist_list1 = ["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Disneyland"],
        tourist_list2 = ["Colosseum", "Trevi Fountain", "Pantheon", "Eiffel Tower"]
Output: ["Eiffel Tower"]
```

**Example 2:**
```
Input:  tourist_list1 = ["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Disneyland"],
        tourist_list2 = ["Disneyland", "Eiffel Tower", "Notre-Dame"]
Output: ["Eiffel Tower"]
```

**Example 3:**
```
Input:  tourist_list1 = ["beach", "mountain", "forest"], tourist_list2 = ["mountain", "beach", "forest"]
Output: ["mountain", "beach"]
```

---
