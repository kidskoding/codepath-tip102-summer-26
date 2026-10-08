# Problem Set: Dictionaries & Big O (Memes) — Week 4, Day 1

For every implementation problem, also evaluate the time and space complexity of your solution. Define your variables and explain why your solution has the stated complexity.

---

## Problem 1: Meme Length Filter

### Description

Memes that exceed a certain length are less likely to go viral. Write a function `prob01()` that takes a list of meme texts `memes` and an integer `max_length`, and returns a list of the memes whose length is within `max_length`.

### Function Signature

```python
def prob01(memes, max_length):
    pass
```

### Examples

**Example 1:**
```
Input:  memes = ["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"],
        max_length = 20
Output: ['This is hilarious!', 'Short and sweet']
```

**Example 2:**
```
Input:  memes = ["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"],
        max_length = 15
Output: ['Just right', 'Perfect length']
```

**Example 3:**
```
Input:  memes = ["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"],
        max_length = 10
Output: ['Short', 'Tiny meme']
```

---

## Problem 2: Top Meme Creators

### Description

Write a function `prob02()` that takes a list of meme dictionaries `memes` and returns a dictionary mapping each creator's name to the number of memes they created.

### Function Signature

```python
def prob02(memes):
    pass
```

### Examples

**Example 1:**
```
Input:  memes = [
            {"creator": "Alex", "text": "Meme 1"},
            {"creator": "Jordan", "text": "Meme 2"},
            {"creator": "Alex", "text": "Meme 3"},
            {"creator": "Chris", "text": "Meme 4"},
            {"creator": "Jordan", "text": "Meme 5"}
        ]
Output: {'Alex': 2, 'Jordan': 2, 'Chris': 1}
```

**Example 2:**
```
Input:  memes = [
            {"creator": "Sam", "text": "Meme 1"},
            {"creator": "Sam", "text": "Meme 2"},
            {"creator": "Sam", "text": "Meme 3"},
            {"creator": "Taylor", "text": "Meme 4"}
        ]
Output: {'Sam': 3, 'Taylor': 1}
```

**Example 3:**
```
Input:  memes = [{"creator": "Blake", "text": "Meme 1"}, {"creator": "Blake", "text": "Meme 2"}]
Output: {'Blake': 2}
```

---

## Problem 3: Meme Trend Identification

### Description

A meme is **trending** if it appears more than once in the dataset. Write a function `prob03()` that takes a list of meme texts `memes` and returns a list of the trending memes.

### Function Signature

```python
def prob03(memes):
    pass
```

### Examples

**Example 1:**
```
Input:  memes = ["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!",
                 "Distracted boyfriend", "One does not simply walk into Mordor"]
Output: ['Dogecoin to the moon!', 'One does not simply walk into Mordor']
```

**Example 2:**
```
Input:  memes = ["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"]
Output: ['Surprised Pikachu']
```

**Example 3:**
```
Input:  memes = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]
Output: []
```

---

## Problem 4: Reverse Meme Order

### Description

You want to see how memes would trend if they were posted in reverse order. Write a function `prob04()` that takes a list `memes` (in posting order) and returns a new list with the memes in reverse order.

### Function Signature

```python
def prob04(memes):
    pass
```

### Examples

**Example 1:**
```
Input:  memes = ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
Output: ['One does not simply walk into Mordor', 'Distracted boyfriend', 'Dogecoin to the moon!']
```

**Example 2:**
```
Input:  memes = ["Surprised Pikachu", "Expanding brain", "This is fine"]
Output: ['This is fine', 'Expanding brain', 'Surprised Pikachu']
```

**Example 3:**
```
Input:  memes = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]
Output: ['Bad Luck Brian', 'Philosoraptor', 'First world problems', 'Y U No?']
```

---

## Problem 5: Trending Meme Pairs (SKIPPED)

_Plan/code-review problem — no new implementation._

### Description

The partially completed code below finds pairs of memes that appear together in more than one post. Before completing it, check the plan and review the code.

**Plan:** write a detailed plan (pseudocode or step-by-step instructions). Consider how you would:
- Iterate through each post.
- Generate pairs of memes.
- Count the frequency of each pair.
- Identify pairs that appear more than once.
- Make the final result accurate and efficient.

**Review:** examine the code and answer:
- Are there logical errors? What are they, and how would you fix them?
- Are there inefficiencies? How would you optimize them?
- Does the code handle edge cases, such as an empty list of posts or posts with only one meme?

### Starter Code

```python
def find_trending_meme_pairs(meme_posts):
    pair_count = {}

    for post in meme_posts:
        for i in range(len(post)):
            for j in range(len(post)):
                if i != j:
                    meme1 = post[i]
                    meme2 = post[j]

                    if meme1 < meme2:
                        meme1, meme2 = meme2, meme1
                    pair = (meme1, meme2)
                    if pair in pair_count:
                        pair_count[pair] += 1
                    else:
                        pair_count[pair] = 1

    trending_pairs = []
    for pair in pair_count:
        if pair_count[pair] >= 2:
            trending_pairs.append(pair)

    return trending_pairs
```

### Examples

**Example 1:**
```
Input:  meme_posts = [
            ["Dogecoin to the moon!", "Distracted boyfriend"],
            ["One does not simply walk into Mordor", "Dogecoin to the moon!"],
            ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"],
            ["Distracted boyfriend", "One does not simply walk into Mordor"]
        ]
Output: [('Distracted boyfriend', 'Dogecoin to the moon!'), ('Dogecoin to the moon!', 'One does not simply walk into Mordor'),
         ('Distracted boyfriend', 'One does not simply walk into Mordor')]
```

**Example 2:**
```
Input:  meme_posts = [
            ["Surprised Pikachu", "This is fine"],
            ["Expanding brain", "Surprised Pikachu"],
            ["This is fine", "Expanding brain"],
            ["Surprised Pikachu", "This is fine"]
        ]
Output: [('Surprised Pikachu', 'This is fine')]
```

**Example 3:**
```
Input:  meme_posts = [
            ["Y U No?", "First world problems"],
            ["Philosoraptor", "Bad Luck Brian"],
            ["First world problems", "Philosoraptor"],
            ["Y U No?", "First world problems"]
        ]
Output: [('First world problems', 'Y U No?')]
```

---

## Problem 6: Meme Popularity Queue

### Description

Memes are posted in a sequence, and their popularity grows as they are reposted. Write a function `prob06()` that takes a list `memes` (the initial posting order) and a list `reposts`, where `reposts[i]` is how many times `memes[i]` is processed.

Simulate the reposts with a queue: process the meme at the front, and if it still has reposts left, add it back to the end of the queue. Return the order in which all reposts are processed.

### Function Signature

```python
def prob06(memes, reposts):
    pass
```

### Examples

**Example 1:**
```
Input:  memes = ["Distracted boyfriend", "Dogecoin to the moon!", "One does not simply walk into Mordor"],
        reposts = [2, 1, 3]
Output: ['Distracted boyfriend', 'Dogecoin to the moon!', 'One does not simply walk into Mordor',
         'Distracted boyfriend', 'One does not simply walk into Mordor', 'One does not simply walk into Mordor']
```

**Example 2:**
```
Input:  memes = ["Surprised Pikachu", "This is fine", "Expanding brain"], reposts = [1, 2, 2]
Output: ['Surprised Pikachu', 'This is fine', 'Expanding brain', 'This is fine', 'Expanding brain']
```

**Example 3:**
```
Input:  memes = ["Y U No?", "Philosoraptor"], reposts = [3, 1]
Output: ['Y U No?', 'Philosoraptor', 'Y U No?', 'Y U No?']
```

---

## Problem 7: Search for Viral Meme Groups

### Description

Each meme has a popularity score. You want the two memes whose combined popularity score is closest to a target value. The list `memes` holds `(name, score)` tuples, already sorted by score.

Write a function `prob07()` that takes `memes` and a `target` score and returns a tuple of the names of the two memes whose combined score is closest to `target`.

### Function Signature

```python
def prob07(memes, target):
    pass
```

### Examples

**Example 1:**
```
Input:  memes = [("Distracted boyfriend", 5), ("Dogecoin to the moon!", 7), ("One does not simply walk into Mordor", 12)],
        target = 13
Output: ('Distracted boyfriend', 'Dogecoin to the moon!')
```

**Example 2:**
```
Input:  memes = [("Surprised Pikachu", 2), ("This is fine", 6), ("Expanding brain", 9), ("Y U No?", 15)],
        target = 10
Output: ('Surprised Pikachu', 'Expanding brain')
```

**Example 3:**
```
Input:  memes = [("Philosoraptor", 1), ("Bad Luck Brian", 4), ("First world problems", 8), ("Y U No?", 13)],
        target = 12
Output: ('Bad Luck Brian', 'First world problems')
```

### Constraints

- `memes` is sorted by score in ascending order

---

## Problem 8: Analyze Meme Trends

### Description

Each meme has a name and a list of daily repost counts. Write a function `prob08()` that takes a list `memes` and a time range `start_day` to `end_day` (inclusive, 0-indexed days), and returns the name of the meme with the highest average reposts over that range. If there is a tie, return the meme that appears first in the list.

### Function Signature

```python
def prob08(memes, start_day, end_day):
    pass
```

### Examples

**Example 1:**
```
Input:  memes = [
            {"name": "Distracted boyfriend", "reposts": [5, 3, 2, 7, 6]},
            {"name": "Dogecoin to the moon!", "reposts": [2, 4, 6, 8, 10]},
            {"name": "One does not simply walk into Mordor", "reposts": [3, 3, 5, 4, 2]}
        ],
        start_day = 1, end_day = 3
Output: "Dogecoin to the moon!"
```

**Example 2:**
```
Input:  memes = [
            {"name": "Surprised Pikachu", "reposts": [2, 1, 4, 5, 3]},
            {"name": "This is fine", "reposts": [3, 5, 2, 6, 4]},
            {"name": "Expanding brain", "reposts": [4, 2, 1, 4, 2]}
        ],
        start_day = 0, end_day = 2
Output: "This is fine"
```

**Example 3:**
```
Input:  memes = [
            {"name": "Y U No?", "reposts": [1, 2, 1, 2, 1]},
            {"name": "Philosoraptor", "reposts": [3, 1, 3, 1, 3]}
        ],
        start_day = 2, end_day = 4
Output: "Philosoraptor"
```

---
