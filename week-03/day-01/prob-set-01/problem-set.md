# Problem Set: Stacks, Queues & Two Pointers — Week 3, Day 1

---

## Problem 1: Post Format Validator

### Description

You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags: `()` for mentions, `[]` for hashtags, and `{}` for links. Given a string representing a post's content, determine if the tags in the post are correctly formatted.

**A solution is considered valid if:**
- Every opening tag has a corresponding closing tag of the same type.
- Tags are closed in the correct order.

### Examples

**Example 1:**
```
Input:  "()"
Output: True
```

**Example 2:**
```
Input:  "()[]{}"`
Output: True
```

**Example 3:**
```
Input:  "(]"
Output: False
```

---

## Problem 2: Reverse User Comments Queue

### Description

On your platform, comments on posts are displayed in the order they are received. For a special feature, you need to reverse the order of comments before displaying them. Given a queue of comments represented as a list of strings, reverse the order using a stack.

### Examples

**Example 1:**
```
Input:  ["Great post!", "Love it!", "Thanks for sharing."]
Output: ['Thanks for sharing.', 'Love it!', 'Great post!']
```

**Example 2:**
```
Input:  ["First!", "Interesting read.", "Well written."]
Output: ['Well written.', 'Interesting read.', 'First!']
```

---

## Problem 3: Check Symmetry in Post Titles

### Description

As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical — meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string, use the two-pointer method to determine if the title is symmetrical.

### Examples

**Example 1:**
```
Input:  "A Santa at NASA"
Output: True
```

**Example 2:**
```
Input:  "Social Media"
Output: False
```

---

## Problem 4: Engagement Boost - SKIP

### Description

You track your daily engagement rates as a list of integers sorted in non-decreasing order. To analyze the impact of certain strategies, you square each engagement rate and return the results sorted in non-decreasing order.

**Your tasks:**
1. Read through the starter code and add comments so your pod understands how it works.
2. Modify the solution to use the two-pointer technique.

### Starter Code

```python
def prob04(engagements):
    squared_engagements = []

    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))

    squared_engagements.sort(reverse=True)

    result = [0] * len(engagements)
    position = len(engagements) - 1

    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1

    return result
```

### Examples

**Example 1:**
```
Input:  [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
```

**Example 2:**
```
Input:  [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]
```

---

## Problem 5: Content Cleaner

### Description

You want to make sure your posts are clean and professional. Given a string `post` of lowercase and uppercase English letters, remove any pairs of adjacent characters where one is the lowercase version of a letter and the other is the uppercase version of the same letter. Keep removing such pairs until the post is clean.

A clean post does not have two adjacent characters `post[i]` and `post[i + 1]` where one is the lowercase version of the other (or vice versa). Return the clean post. An empty string is also considered clean.

### Examples

**Example 1:**
```
Input:  "poOost"
Output: "post"
```

**Example 2:**
```
Input:  "abBAcC"
Output: ""
```

**Example 3:**
```
Input:  "s"
Output: "s"
```

---

## Problem 6: Post Editor

### Description

You want to add a creative twist to your posts by reversing the order of characters in each word while still preserving whitespace and the original word order. Given a string `post`, reverse the order of characters in each word within the sentence.

### Examples

**Example 1:**
```
Input:  "Boost your engagement with these tips"
Output: "tsooB ruoy tnemegegna htiw esehT spit"
```

**Example 2:**
```
Input:  "Check out my latest vlog"
Output: "kcehC tuo ym tseval golv"
```

---

## Problem 7: Post Compare

### Description

You often draft your posts and edit them before publishing. Given two draft strings `draft1` and `draft2`, return `True` if they are equal when both are typed into empty text editors. The `#` character means a backspace. After backspacing an empty text, the text remains empty.

### Examples

**Example 1:**
```
Input:  draft1 = "ab#c", draft2 = "ad#c"
Output: True
```

**Example 2:**
```
Input:  draft1 = "ab##", draft2 = "c#d#"
Output: True
```

**Example 3:**
```
Input:  draft1 = "a#c", draft2 = "b"
Output: False
```

---
