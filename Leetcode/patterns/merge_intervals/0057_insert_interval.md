# Leetcode 0057 - Insert Interval

## ☀️ UMPIRE

- **Understand**:  
  You are given a list of **non-overlapping intervals**, sorted by their start times, and a new interval to insert.  
  Insert the new interval into the list so that the result still has non-overlapping intervals and remains sorted.

- **Match**:  
  This is a **merge intervals** variation — instead of merging all at once, we only merge around the new interval.

- **Plan**:
  1. Initialize an empty result list `res`.
  2. Add all intervals **ending before** `newInterval` starts → no overlap.
  3. Merge all intervals **overlapping** with `newInterval`:
     - Update `new_s = min(new_s, start)`
     - Update `new_e = max(new_e, end)`
  4. Append the merged `newInterval`.
  5. Append all intervals **starting after** `newInterval` ends.
  6. Return `res`.

- **Implement**: See code section below.

- **Review**:
  - Ensure the append for merged interval happens **after** processing all overlaps (not inside the while loop).
  - Maintain sorted order by processing left, then merged, then right intervals in sequence.

- **Evaluate**:
  - Time: **O(n)** — one pass over intervals.
  - Space: **O(n)** for the output list.

---

## ☀️ Why We Append After the Overlap Loop

We only append the merged interval **once** after the while loop because:
- The merging process extends `newInterval`’s start/end to cover **all overlapping intervals**.
- If we appended inside the loop, we might add incomplete or partially merged intervals, leading to incorrect results or extra merges later.

---

## ☀️ Edge Case Notes

| Input intervals | newInterval | Output | Notes |
| --------------- | ----------- | ------ | ----- |
| `[[1,3],[6,9]]` | `[2,5]`     | `[[1,5],[6,9]]` | Overlaps with `[1,3]` only |
| `[[1,2],[3,5],[6,7],[8,10],[12,16]]` | `[4,8]` | `[[1,2],[3,10],[12,16]]` | Overlaps with `[3,5],[6,7],[8,10]` |
| `[]`            | `[5,7]`     | `[[5,7]]` | Empty list → just add the interval |
| `[[1,5]]`       | `[2,3]`     | `[[1,5]]` | Fully inside existing interval |
| `[[1,5]]`       | `[2,7]`     | `[[1,7]]` | Extends existing interval’s end |
| `[[1,5]]`       | `[6,8]`     | `[[1,5],[6,8]]` | No overlap |

---

## ☀️ Code (Insert Interval - Linear Scan)

```python
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        new_s, new_e = newInterval

        # 1) Add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < new_s:
            res.append(intervals[i])
            i += 1

        # 2) Merge all overlapping intervals
        while i < n and intervals[i][0] <= new_e:
            new_s = min(new_s, intervals[i][0])
            new_e = max(new_e, intervals[i][1])
            i += 1

        # Append merged interval
        res.append([new_s, new_e])

        # 3) Add remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
```

---

## ☀️ Python Notes

- `while i < n and intervals[i][1] < new_s`: picks all **left-side non-overlapping** intervals.
- `while i < n and intervals[i][0] <= new_e`: detects overlap (including touching intervals) and expands new interval bounds.
- `res.append([new_s, new_e])` is done after merging all overlaps.

---

## ☀️ Coding Walkthrough Script

- First, I store `new_s` and `new_e` from `newInterval`.
- I scan from the start of `intervals` and append any interval that ends before `new_s` — these are safe, no overlap.
- Then I enter a loop for all overlapping intervals.  
  For each overlap, I adjust `new_s` to the smallest start, and `new_e` to the largest end so far.
- Once overlaps are done, I append the final merged interval.
- Finally, I append all remaining intervals that start after `new_e`.

---

## ☀️ Complexity Comparison

| Method                     | Time Complexity | Space Complexity | Notes |
| -------------------------- | --------------- | ---------------- | ----- |
| Brute Force (merge all)    | O(n log n)      | O(n)             | Sort then merge everything |
| Linear Scan (this method)  | O(n)            | O(n)             | Directly inserts new interval without full re-merge |
| In-place with write index  | O(n)            | O(1) extra       | Modifies original list, careful with indices |

---
