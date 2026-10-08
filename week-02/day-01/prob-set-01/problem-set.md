# Problem Set: Dictionaries & Sets (Music Festival) — Week 2, Day 1

---

## Problem 1: Festival Lineup

### Description

Given two lists of strings `artists` and `set_times` of length `n`, write a function `prob01()` that maps each artist to their set time.

Artist `artists[i]` has set time `set_times[i]`, where `0 <= i < n` and `len(artists) == len(set_times)`.

### Function Signature

```python
def prob01(artists, set_times):
    pass
```

### Examples

**Example 1:**
```
Input:  artists = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"],
        set_times = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]
Output: {"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalia": "7:30 PM"}
```

**Example 2:**
```
Input:  artists = [], set_times = []
Output: {}
```

---

## Problem 2: Planning App

### Description

You are designing an app that lets festival attendees search for their favorite artist and find the day, time, and stage the artist plays. Write a function `prob02()` that accepts a string `artist` and a dictionary `festival_schedule` mapping artist names to dictionaries containing the day, time, and stage they play on. Return the dictionary containing the information about the given artist.

If the artist is not in `festival_schedule`, return the dictionary `{"message": "Artist not found"}`.

### Function Signature

```python
def prob02(artist, festival_schedule):
    pass
```

### Examples

```python
festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}
```

**Example 1:**
```
Input:  artist = "Blood Orange", festival_schedule
Output: {'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}
```

**Example 2:**
```
Input:  artist = "Taylor Swift", festival_schedule
Output: {'message': 'Artist not found'}
```

---

## Problem 3: Ticket Sales

### Description

A dictionary `ticket_sales` maps ticket type to number of tickets sold. Write a function `prob03()` that returns the total number of tickets sold across all types.

### Function Signature

```python
def prob03(ticket_sales):
    pass
```

### Examples

**Example 1:**
```
Input:  ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
Output: 4500
```

---

## Problem 4: Scheduling Conflict

### Description

Your festival now spans two venues. Some artists perform at both venues, others at just one. To catch scheduling conflicts, write a function `prob04()` that accepts two dictionaries `venue1_schedule` and `venue2_schedule`, each mapping the artists playing at that venue to their set times. Return a dictionary containing the key-value pairs that are the same in both schedules.

### Function Signature

```python
def prob04(venue1_schedule, venue2_schedule):
    pass
```

### Examples

**Example 1:**
```
Input:  venue1_schedule = {"Stromae": "9:00 PM", "Janelle Monáe": "8:00 PM", "HARDY": "7:00 PM", "Bruce Springsteen": "6:00 PM"},
        venue2_schedule = {"Stromae": "9:00 PM", "Janelle Monáe": "10:30 PM", "HARDY": "7:00 PM", "Wizkid": "6:00 PM"}
Output: {"Stromae": "9:00 PM", "HARDY": "7:00 PM"}
```

---

## Problem 5: Best Set

### Description

Attendees vote for their favorite set. Given a dictionary `votes` that maps attendee id numbers to the artist they voted for, write a function `prob05()` that returns the artist with the most votes. If there is a tie, return any artist with the top number of votes.

### Function Signature

```python
def prob05(votes):
    pass
```

### Examples

**Example 1:**
```
Input:  votes = {1234: "SZA", 1235: "Yo-Yo Ma", 1236: "Ethel Cain", 1237: "Ethel Cain", 1238: "SZA", 1239: "SZA"}
Output: "SZA"
```

**Example 2:**
```
Input:  votes = {1234: "SZA", 1235: "Yo-Yo Ma", 1236: "Ethel Cain", 1237: "Ethel Cain", 1238: "SZA"}
Output: "Ethel Cain"
Explanation: "SZA" and "Ethel Cain" are both acceptable answers.
```

---

## Problem 6: Performances with Maximum Audience

### Description

You are given a list `audiences` of positive integers, each the audience size of a performance at a music festival. Write a function `prob06()` that returns the combined size of every audience that had the maximum size.

### Function Signature

```python
def prob06(audiences):
    pass
```

### Examples

**Example 1:**
```
Input:  audiences = [100, 200, 200, 150, 100, 250]
Output: 250
```

**Example 2:**
```
Input:  audiences = [120, 180, 220, 150, 220]
Output: 440
```

---

## Problem 7: Performances with Maximum Audience II

### Description

If you used a dictionary in your solution to Problem 6, reimplement it without a dictionary. If you solved Problem 6 without a dictionary, solve it with one. Then compare the two solutions: is one better than the other? Why or why not?

The function behaves exactly like Problem 6.

### Function Signature

```python
def prob07(audiences):
    pass
```

### Examples

**Example 1:**
```
Input:  audiences = [100, 200, 200, 150, 100, 250]
Output: 250
```

**Example 2:**
```
Input:  audiences = [120, 180, 220, 150, 220]
Output: 440
```

---

## Problem 8: Popular Song Pairs

### Description

Given a list of integers `popularity_scores` representing the popularity scores of songs in a festival playlist, write a function `prob08()` that returns the number of popular song pairs.

A pair `(i, j)` is **popular** if the songs have the same popularity score and `i < j`.

### Function Signature

```python
def prob08(popularity_scores):
    pass
```

### Examples

**Example 1:**
```
Input:  popularity_scores = [1, 2, 3, 1, 1, 3]
Output: 4
```

**Example 2:**
```
Input:  popularity_scores = [1, 1, 1, 1]
Output: 6
```

**Example 3:**
```
Input:  popularity_scores = [1, 2, 3]
Output: 0
```

---

## Problem 9: Stage Arrangement Difference Between Two Performances

### Description

You are given two lists of strings `s` and `t` representing the stage arrangements of performers in two performances. Every performer occurs at most once in `s` and in `t`, and `t` is a permutation of `s`.

The **stage arrangement difference** between `s` and `t` is the sum, over every performer, of the absolute difference between that performer's index in `s` and their index in `t`.

Write a function `prob09()` that returns the stage arrangement difference between `s` and `t`.

A permutation is a rearrangement of a sequence. For example, `[3, 1, 2]` and `[2, 1, 3]` are both permutations of `[1, 2, 3]`.

### Function Signature

```python
def prob09(s, t):
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """
```

### Examples

**Example 1:**
```
Input:  s = ["Alice", "Bob", "Charlie"], t = ["Bob", "Alice", "Charlie"]
Output: 2
```

**Example 2:**
```
Input:  s = ["Alice", "Bob", "Charlie", "David", "Eve"], t = ["Eve", "David", "Bob", "Alice", "Charlie"]
Output: 12
```

---

## Problem 10: VIP Passes and Guests

### Description

You are given a string `vip_passes` representing the types of guests that hold VIP passes, and a string `guests` representing the guests at the festival. Each character in `guests` is one guest's type. Write a function `prob10()` that returns how many of your guests are also VIP pass holders.

Letters are case sensitive, so `"a"` is a different type of guest from `"A"`.

Implement this pseudocode, then explain your implementation step by step:

1. Create an empty set called `vip_set`.
2. For each character in `vip_passes`, add it to `vip_set`.
3. Initialize a counter variable to 0.
4. For each character in `guests`, if the character is in `vip_set`, increment the counter by 1.
5. Return the counter.

### Function Signature

```python
def prob10(vip_passes, guests):
    pass
```

### Examples

**Example 1:**
```
Input:  vip_passes = "aA", guests = "aAAbbbb"
Output: 3
```

**Example 2:**
```
Input:  vip_passes = "z", guests = "ZZ"
Output: 0
```

---

## Problem 11: Performer Schedule Pattern (SKIPPED)

_Debugging/code-review problem — no new implementation._

### Description

Given a string `pattern` and a string `schedule`, return `True` if `schedule` follows the same pattern, and `False` otherwise. "Follows" means a full match: there is a one-to-one correspondence between each letter in `pattern` and each non-empty word in `schedule`.

The code below is partially implemented and buggy. Identify and fix the bugs, then perform a thorough code review and suggest improvements.

### Starter Code

```python
def schedule_pattern(pattern, schedule):

    genres = schedule.split()

    if len(genres) == len(pattern):
        return True

    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] == genre:
                return True
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] == char:
                return True
        else:
            genre_to_char[genre] = char

    return False
```

### Examples

**Example 1:**
```
Input:  pattern = "abba", schedule = "rock jazz jazz rock"
Output: True
```

**Example 2:**
```
Input:  pattern = "abba", schedule = "rock jazz jazz blues"
Output: False
```

**Example 3:**
```
Input:  pattern = "aaaa", schedule = "rock jazz jazz rock"
Output: False
```

---

## Problem 12: Sort the Performers

### Description

You are given a list of strings `performer_names` and a list `performance_times` of distinct positive integers representing performance durations in minutes. Both lists have length `n`. For each index `i`, `performer_names[i]` and `performance_times[i]` are the name and performance duration of the `i`th performer.

Write a function `prob12()` that returns `performer_names` sorted in descending order by performance duration.

### Function Signature

```python
def prob12(performer_names, performance_times):
    """
    :type performer_names: List[str]
    :type performance_times: List[int]
    :rtype: List[str]
    """
```

### Examples

**Example 1:**
```
Input:  performer_names = ["Mary", "John", "Emma"], performance_times = [180, 165, 170]
Output: ["Mary", "Emma", "John"]
```

**Example 2:**
```
Input:  performer_names = ["Alice", "Bob", "Bob"], performance_times = [155, 185, 150]
Output: ["Bob", "Alice", "Bob"]
```

### Constraints

- `performance_times` contains distinct positive integers
- `len(performer_names) == len(performance_times)`

---
