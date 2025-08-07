# ☀️ Leetcode 904 - Fruit Into Baskets

## ☀️ Problem Summary

You are given an array `fruits` where each element represents a type of fruit on a tree.  
You have two baskets, and each basket can only hold one type of fruit.  
Pick a subarray (contiguous) with at most two different fruit types to maximize the total number of fruits.

Return the length of the longest such subarray.

---

## ☀️ Examples

```python
Input: fruits = [1,2,1]
Output: 3  # [1,2,1]

Input: fruits = [0,1,2,2]
Output: 3  # [1,2,2]

Input: fruits = [1,2,3,2,2]
Output: 4  # [2,3,2,2]
```

---

## ☀️ Brute Force Version (TLE)

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        n = len(fruits)

        for i in range(n):
            fruit_types = set()
            for j in range(i, n):
                fruit_types.add(fruits[j])
                if len(fruit_types) > 2:
                    break
                max_len = max(max_len, j - i + 1)

        return max_len
```

- Time: O(n²)
- Space: O(1) — set size is max 2

---

## ☀️ Sliding Window with Counter (Intermediate)

```python
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_len = 0
        count = Counter()

        for right in range(len(fruits)):
            count[fruits[right]] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len
```

- Time: O(n)
- Space: O(1)

---

## ☀️ Optimized Sliding Window with HashMap (Last Seen Index)

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        visited = {}
        left = 0
        max_len = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            visited[fruit] = right

            if len(visited) > 2:
                min_fruit = min(visited, key=visited.get)
                left = visited[min_fruit] + 1
                del visited[min_fruit]

            max_len = max(max_len, right - left + 1)

        return max_len
```

- Time: O(n)
- Space: O(1)

---

## ☀️ Time and Space Complexity Summary

| Version                  | Time      | Space     | Notes                         |
|--------------------------|-----------|-----------|-------------------------------|
| Brute Force              | O(n²)     | O(1)      | Nested loop, intuitive        |
| Counter Sliding Window   | O(n)      | O(1)      | Tracks counts per fruit       |
| HashMap Last Seen Index  | O(n)      | O(1)      | Most concise & optimal        |

---

## ☀️ Core Insight

You can **update the map first** in this problem.  
If adding a fruit causes the map to exceed 2 types, then that **new fruit must be the extra one**,  
so it's safe to update first and then remove the oldest one.
