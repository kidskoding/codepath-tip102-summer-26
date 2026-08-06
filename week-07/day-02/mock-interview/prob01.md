# Problem Set: Ransom Note (Mock Interview) — Week 7, Day 2

---

## Problem 1: Ransom Note

**Difficulty:** Easy

### Description

You are given two strings, `ransomNote` and `magazine`. Return `True` if `ransomNote` can be constructed by using the letters from `magazine`, and `False` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

### Function Signature

```python
def prob01(ransomNote: str, magazine: str) -> bool:
    pass
```

### Examples

**Example 1:**
```
Input:  ransomNote = "a", magazine = "b"
Output: False
```

**Example 2:**
```
Input:  ransomNote = "aa", magazine = "ab"
Output: False
```

**Example 3:**
```
Input:  ransomNote = "aa", magazine = "aab"
Output: True
```

### Constraints

- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

---
