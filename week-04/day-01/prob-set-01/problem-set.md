# Problem Set: Dictionaries & Big O — Week 4, Day 1

---

## Problem 1: NFT Name Extractor

### Description

You're curating a large collection of NFTs for a digital art gallery, and your first task is to extract the names of these NFTs from a given list of dictionaries. Each dictionary in the list represents an NFT, and contains information such as the name, creator, and current value.

Write the `prob01()` function, which takes in this list and returns a list of all NFT names.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  [{"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
         {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
         {"name": "Future City", "creator": "UrbanArt", "value": 3.8}]
Output: ['Abstract Horizon', 'Pixel Dreams', 'Future City']
```

**Example 2:**
```
Input:  [{"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
         {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}]
Output: ['Crypto Kitty', 'Galactic Voyage']
```

**Example 3:**
```
Input:  [{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}]
Output: ['Golden Hour']
```

---

## Problem 2: NFT Collection Review

### Description

You're responsible for ensuring the quality of the NFT collection before it is displayed in the virtual gallery. One of your tasks is to review and debug the code that extracts the names of NFTs from the collection. A junior developer wrote the initial version of this function, but it contains some bugs that prevent it from working correctly.

**Task:**
- Review the provided code and identify the bug(s).
- Explain what the bug is and how it affects the output.
- Refactor the code to fix the bug(s) and provide the correct implementation.

### Starter Code

```python
def prob01(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names += nft["name"]
    return nft_names
```

### Examples

**Example 1:**
```
Input:  [{"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
         {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}]
Output: ['Abstract Horizon', 'Pixel Dreams']
```

**Example 2:**
```
Input:  [{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}]
Output: ['Golden Hour']
```

**Example 3:**
```
Input:  []
Output: []
```

---

## Problem 3: Identify Popular Creators

### Description

You have been tasked with identifying the most popular NFT creators in your collection. A creator is considered "popular" if they have created more than one NFT in the collection.

Write the `prob03()` function, which takes a list of NFTs and returns a list of the names of popular creators.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  [{"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
         {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
         {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}]
Output: ['ArtByAlex']
```

**Example 2:**
```
Input:  [{"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
         {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
         {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}]
Output: ['SpaceArt']
```

**Example 3:**
```
Input:  [{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}]
Output: []
```

---

## Problem 4: NFT Collection Statistics

### Description

You want to provide an overview of the NFT collection to potential buyers. One key statistic is the average value of the NFTs in the collection. However, if the collection is empty, the average value should be reported as 0.

Write the `prob04()` function, which calculates and returns the average value of the NFTs in the collection.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  [{"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
         {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
         {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}]
Output: 5.7
```

**Example 2:**
```
Input:  [{"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
         {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}]
Output: 9.15
```

**Example 3:**
```
Input:  []
Output: 0
```

---

## Problem 5: NFT Tag Search

### Description

Some NFTs are grouped into collections, and each collection might contain multiple NFTs. Additionally, each NFT can have a list of tags describing its style or theme (e.g., "abstract", "landscape", "modern"). You need to search through these nested collections to find all NFTs that contain a specific tag.

Write the `prob05()` function, which takes in a nested list of NFT collections and a tag to search for. The function should return a list of NFT names that have the specified tag.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  [[{"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
          {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}],
         [{"name": "Urban Jungle", "tags": ["urban", "landscape"]},
          {"name": "City Lights", "tags": ["modern", "landscape"]}]], tag = "landscape"
Output: ['Urban Jungle', 'City Lights']
```

**Example 2:**
```
Input:  [[{"name": "Golden Hour", "tags": ["sunset", "landscape"]},
          {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}],
         [{"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}]], tag = "sunset"
Output: ['Golden Hour', 'Sunset Serenade']
```

**Example 3:**
```
Input:  [[{"name": "The Last Piece", "tags": ["finale", "abstract"]}],
         [{"name": "Ocean Waves", "tags": ["seascape", "calm"]},
          {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}]], tag = "modern"
Output: []
```

---

## Problem 6: NFT Queue Processing

### Description

NFTs are processed in a queue that follows First-In, First-Out (FIFO). Given a list of NFT names in their initial queue order, return the order in which they are processed.

Write the `prob06()` function, which takes a list of NFTs. The function should return a list of NFT names in the order they were processed.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  [{"name": "Abstract Horizon", "processing_time": 2},
         {"name": "Pixel Dreams", "processing_time": 3},
         {"name": "Urban Jungle", "processing_time": 1}]
Output: ['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']
```

**Example 2:**
```
Input:  [{"name": "Golden Hour", "processing_time": 4},
         {"name": "Sunset Serenade", "processing_time": 2},
         {"name": "Ocean Waves", "processing_time": 3}]
Output: ['Golden Hour', 'Sunset Serenade', 'Ocean Waves']
```

**Example 3:**
```
Input:  [{"name": "Crypto Kitty", "processing_time": 5},
         {"name": "Galactic Voyage", "processing_time": 6}]
Output: ['Crypto Kitty', 'Galactic Voyage']
```

---

## Problem 7: Validate NFT Addition

### Description

You want to ensure that NFTs are added in a balanced way. For example, every "add" action must be properly closed by a corresponding "remove" action.

Write the `prob07()` function, which takes a list of actions (either "add" or "remove") and returns `True` if the actions are balanced, and `False` otherwise.

A sequence of actions is considered balanced if every "add" has a corresponding "remove" and no "remove" occurs before an "add".

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  ["add", "add", "remove", "remove"]
Output: True
```

**Example 2:**
```
Input:  ["add", "remove", "add", "remove"]
Output: True
```

**Example 3:**
```
Input:  ["add", "remove", "remove", "add"]
Output: False
```

["remove", "add"]

---

## Problem 8: Find Closest NFT Values

### Description

Buyers often look for NFTs that are closest in value to their budget. Given a sorted list of NFT values and a budget, you need to find the two NFT values that are closest to the given budget: one that is just below or equal to the budget and one that is just above or equal to the budget. If an exact match exists, it should be included as one of the values.

Write the `prob08()` function, which takes a sorted list of NFT values and a budget, and returns the pair of the two closest NFT values.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Examples

**Example 1:**
```
Input:  [3.5, 5.4, 7.2, 9.0, 10.5], budget = 8.0
Output: (7.2, 9.0)
```

**Example 2:**
```
Input:  [2.0, 4.5, 6.3, 7.8, 12.1], budget = 6.5
Output: (6.3, 7.8)
```

**Example 3:**
```
Input:  [1.0, 2.5, 4.0, 6.0, 9.0], budget = 3.0
Output: (2.5, 4.0)
```

---
