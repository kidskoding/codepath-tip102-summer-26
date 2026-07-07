# Problem Set: Dictionaries & Hashing — Week 4, Day 2

---

## Problem 1: Planning Your Daily Work Schedule

### Description

Your day consists of various tasks, each requiring a certain amount of time. To optimize your workday, you want to find a pair of tasks that fits exactly into a specific time slot you have available.

Given a list of integers representing the time required for each task and an integer representing the available time slot, write a function that returns `True` if there exists a pair of tasks whose combined time exactly matches the available time slot, and `False` otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  task_times = [30, 45, 60, 90, 120], available_time = 105
Output: True
```

**Example 2:**
```
Input:  task_times = [15, 25, 35, 45, 55], available_time = 100
Output: True
```

**Example 3:**
```
Input:  task_times = [20, 30, 50, 70], available_time = 60
Output: False
```

---

## Problem 2: Minimizing Workload Gaps

### Description

You work with clients across different time zones and often have gaps between your work sessions. You want to minimize these gaps to make your workday more efficient. You have a list of work sessions, each with a start time and an end time.

Given a list of tuples where each tuple represents a work session with a start and end time (both in 24-hour format as integers, e.g., `1300` for 1:00 PM), write a function to find the smallest gap between any two consecutive work sessions. The gap is measured in minutes.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
Output: 60
```

**Example 2:**
```
Input:  work_sessions = [(1000, 1130), (1200, 1300), (1400, 1500)]
Output: 30
```

**Example 3:**
```
Input:  work_sessions = [(900, 1100), (1115, 1300), (1315, 1500)]
Output: 15
```

---

## Problem 3: Expense Tracking and Categorization

### Description

You travel frequently and need to keep track of your expenses. You categorize your expenses into different categories such as "Food," "Transport," "Accommodation," etc. At the end of each month, you want to calculate the total expenses for each category to better understand where your money is going.

Given a list of tuples where each tuple contains an expense category (string) and an expense amount (float), write a function that returns the expense categories with the total expenses for each category. Additionally, the function should return the category with the highest total expense.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
                     ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
Output: ({'Food': 30.0, 'Transport': 25.0, 'Accommodation': 50.0}, 'Accommodation')
```

**Example 2:**
```
Input:  expenses = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
                     ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
Output: ({'Entertainment': 25.0, 'Food': 40.0, 'Transport': 10.0, 'Accommodation': 40.0}, 'Food')
```

**Example 3:**
```
Input:  expenses = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
                     ("Utilities", 50.0), ("Food", 25.0)]
Output: ({'Utilities': 150.0, 'Food': 75.0, 'Transport': 75.0}, 'Utilities')
```

---

## Problem 4: Analyzing Word Frequency

### Description

As a digital nomad who writes blogs, articles, and reports regularly, it's important to analyze the text you produce to ensure clarity and avoid overusing certain words. You want to create a tool that analyzes the frequency of each word in a given text and identifies the most frequent word(s).

Given a string of text, write a function that returns the unique words and the number of times each word appears in the text. Additionally, return a list of the word(s) that appear most frequently.

**Assumptions:**
- The text is case-insensitive, so "Word" and "word" should be treated as the same word.
- Punctuation should be ignored.
- In case of a tie, return all words that have the highest frequency.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
Output: ({'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 2, 'was': 1, 'not': 1, 'amused': 1}, ['the'])
```

**Example 2:**
```
Input:  text = "Digital nomads love to travel. Travel is their passion."
Output: ({'digital': 1, 'nomads': 1, 'love': 1, 'to': 1, 'travel': 2, 'is': 1, 'their': 1, 'passion': 1}, ['travel'])
```

**Example 3:**
```
Input:  text = "Stay connected. Stay productive. Stay happy."
Output: ({'stay': 3, 'connected': 1, 'productive': 1, 'happy': 1}, ['stay'])
```

---

## Problem 5: Validating HTML Tags

### Description

As a digital nomad who frequently writes and edits HTML for your blog, you want to ensure that your HTML code is properly structured. One important aspect of HTML structure is ensuring that all opening tags have corresponding closing tags and that they are properly nested.

Given a string of HTML-like tags (simplified for this problem), write a function to determine if the tags are properly nested and closed. The tags will be in the form of `<tag>` for opening tags and `</tag>` for closing tags. The function should return `True` if the tags are properly nested and closed, and `False` otherwise.

**Assumptions:**
- You can assume that tags are well-formed (e.g., `<div>`, `</div>`, `<a>`, `</a>`, etc.).
- Tags can be nested but cannot overlap improperly (e.g., `<div><p></div></p>` is invalid).

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  html = "<div><p></p></div>"
Output: True
```

**Example 2:**
```
Input:  html = "<div><p></div></p>"
Output: False
```

**Example 3:**
```
Input:  html = "<div><p><a></a></p></div>"
Output: True
```

**Example 4:**
```
Input:  html = "<div><p></a></p></div>"
Output: False
```

---

## Problem 6: Task Prioritization with Limited Time

### Description

You often have a long list of tasks to complete, but limited time to do so. Each task has a specific duration, and you only have a certain amount of time available in your schedule. You need to prioritize and complete as many tasks as possible within the given time limit.

Given a list of task durations and a time limit, determine the maximum number of tasks you can complete within that time.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  tasks = [5, 10, 7, 8], time_limit = 20
Output: 3
```

**Example 2:**
```
Input:  tasks = [2, 4, 6, 3, 1], time_limit = 10
Output: 4
```

**Example 3:**
```
Input:  tasks = [8, 5, 3, 2, 7], time_limit = 15
Output: 3
```

---

## Problem 7: Frequent Co-working Spaces

### Description

You often work from various co-working spaces. You want to analyze your usage patterns to identify which co-working spaces you visit the most frequently.

Given a list of co-working spaces you visited over the past month, write a function to determine which co-working space(s) you visited most frequently. If there is a tie, return all of the most visited spaces.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  visits = ["WeWork", "Regus", "Spaces", "WeWork", "Regus", "WeWork"]
Output: ['WeWork']
```

**Example 2:**
```
Input:  visits = ["IndieDesk", "Spaces", "IndieDesk", "WeWork", "Spaces", "IndieDesk", "WeWork"]
Output: ['IndieDesk']
```

**Example 3:**
```
Input:  visits = ["Hub", "Regus", "WeWork", "Hub", "WeWork", "Regus", "Hub", "Regus"]
Output: ['Hub', 'Regus']
```

---

## Problem 8: Track Popular Destinations

### Description

You want to track the most popular destinations you visited based on the number of times you have visited them.

Given a list of visited destinations with timestamps, determine the destination that has been visited the most and the total number of times it was visited. If there is a tie, return the one with the latest visit.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  visits = [("Paris", "2024-07-15"), ("Tokyo", "2024-08-01"), ("Paris", "2024-08-05"),
                   ("New York", "2024-08-10"), ("Tokyo", "2024-08-15"), ("Paris", "2024-08-20")]
Output: ('Paris', 3)
```

**Example 2:**
```
Input:  visits = [("London", "2024-06-01"), ("Berlin", "2024-06-15"), ("London", "2024-07-01"),
                   ("Berlin", "2024-07-10"), ("London", "2024-07-15")]
Output: ('London', 3)
```

**Example 3:**
```
Input:  visits = [("Sydney", "2024-05-01"), ("Dubai", "2024-05-15"), ("Sydney", "2024-05-20"),
                   ("Dubai", "2024-06-01"), ("Dubai", "2024-06-15")]
Output: ('Dubai', 3)
```

---
