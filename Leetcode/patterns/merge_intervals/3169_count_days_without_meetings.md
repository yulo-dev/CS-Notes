# Leetcode 3169 — Count Days Without Meetings

## ☀️ UMPIRE

- **Understand**: You are given `days` (total days, labeled from 1..days) and a list of **closed** meeting intervals `meetings[i] = [s_i, e_i]`. Each closed interval covers all days `d` with `s_i ≤ d ≤ e_i`. Return the number of days **without** meetings.
  
- **Match**: This is an **Intervals / Union Coverage** problem. The natural approach is to:
  1) **Merge** overlapping/adjacent meeting intervals (explicitly or implicitly), then  
  2) Either compute the **union length** and do `days - union_len`, **or** sum **gaps** directly.
  
- **Plan**:
  - **Solution 1 (Explicit Merge)**: Sort by start → merge overlapping/adjacent intervals like LC56 → sum merged lengths → return `days - sum`.
  - **Solution 2 (Implicit Merge / Single Pass Gaps)**: Sort by start → maintain `prev_end` as current coverage → when a new block starts strictly after `prev_end`, add the gap `s - prev_end - 1` → extend `prev_end = max(prev_end, e)` → at the end, add tail `days - prev_end`.
  
- **Implement**: See code below (both solutions included with full comments).

- **Review**:
  - Intervals are **closed** → length is `(e - s + 1)`; gap between two closed blocks `[a,b]` then `[c,d]` is `(c - b - 1)`.
  - **Adjacency** (e.g., `[1,3]` and `[4,5]`) means **no free day** in between → treat as **mergeable**.
  - If input is not guaranteed sorted, **sort** by start first.

- **Evaluate**:
  - Sorting dominates → **Time** `O(n log n)`; single scan `O(n)`. If input already sorted, overall `O(n)`.
  - **Space** `O(1)` auxiliary (excluding any output-like temp list).


---

## ☀️ Why This Is an Intervals Problem

We only care about the **union** of all covered days. Once intervals are sorted by start, overlapping or adjacent meetings can be combined into a single covered block. The final answer is the **complement** of this union over `1..days`. This is identical in spirit to LC56 (merge intervals), except the output we want is a **scalar (free-day count)** rather than the merged list itself.


---

## ☀️ Edge Case Notes

| Case | Input `meetings` (unsorted example) | Sorted | Explanation | Expected |
|---|---|---|---|---|
| Empty | `[]`, `days=7` | `[]` | No meetings at all | `7` |
| Single block | `[[2,5]]`, `days=7` | `[[2,5]]` | Covered 2..5 → free days `1,6,7` | `3` |
| Overlap | `[[1,3],[2,6]]`, `days=7` | `[[1,3],[2,6]]` | Merged → `[1,6]` | `1` |
| Adjacent | `[[1,3],[4,4]]`, `days=7` | `[[1,3],[4,4]]` | Closed intervals touch → no gap → merged `[1,4]` | `3` |
| Contained | `[[1,10],[2,3]]`, `days=10` | `[[1,10],[2,3]]` | `[2,3]` inside `[1,10]` | `0` |
| Multiple blocks | `[[1,3],[5,7],[9,10]]`, `days=10` | same | Gaps at `4` and `8` → free = `2` | `2` |


---

## ☀️ Code — Solution 1 (Explicit Merge then Subtract)

```python
from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        Explicitly merge meetings (like LC56), then subtract union length from total days.
        - Closed intervals: length([s, e]) = (e - s + 1)
        - Adjacent blocks (e.g., [1,3] and [4,5]) should be merged (no free day between).
        Time:  O(n log n) for sorting + O(n) merging
        Space: O(1) auxiliary (excluding the temporary merged list)
        """
        if not meetings:
            return days  # no meetings at all

        # 1) Sort by start time
        meetings.sort(key=lambda it: it[0])

        # 2) Merge overlapping or adjacent intervals
        merged: List[List[int]] = []
        cur_s, cur_e = meetings[0]

        for s, e in meetings[1:]:
            # Overlap or adjacency (closed intervals): s <= cur_e + 1
            if s <= cur_e + 1:
                cur_e = max(cur_e, e)   # extend the current merged block
            else:
                merged.append([cur_s, cur_e])  # finalize current block
                cur_s, cur_e = s, e            # start a new block

        merged.append([cur_s, cur_e])           # don't forget the last one

        # 3) Compute the union (covered) length
        covered = 0
        for s, e in merged:
            covered += (e - s + 1)  # closed interval length

        # 4) Free days = total days - covered length
        free_days = days - covered
        return max(0, free_days)  # guard if inputs exceed [1..days]
```


---

## ☀️ Code — Solution 2 (Implicit Merge / Single-Pass Gap Sum)

```python
from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        Implicitly merge by tracking 'prev_end' and summing gaps directly.
        - If the next block starts at s > prev_end, there is a gap of length (s - prev_end - 1).
        - Always extend coverage: prev_end = max(prev_end, e).
        - Tail gap (after the last covered day): max(0, days - prev_end).
        Time:  O(n log n) for sorting + O(n) scan  (or O(n) total if already sorted)
        Space: O(1) auxiliary
        """
        if not meetings:
            return days

        meetings.sort(key=lambda it: it[0])

        free = 0
        prev_end = 0  # rightmost covered day so far (0 means before day 1)

        for s, e in meetings:
            # When a new block starts strictly after prev_end, the free gap is (prev_end+1 .. s-1).
            if s > prev_end:
                free += max(0, s - prev_end - 1)
            # Extend the coverage to the farthest right
            prev_end = max(prev_end, e)

        # Tail gap after the last covered day until 'days'
        free += max(0, days - prev_end)

        return free
```


---

## ☀️ Tags / Data Structure / Algorithm

**Tags**: Intervals (Union), Line Sweep, Sorting, Greedy  
**Data Structure**: List of 2‑element lists `[start, end]` (closed).  
**Algorithm**:
- **Implicit Merge (recommended)**: sort by start → sum gaps with `prev_end` → add tail.
- **Explicit Merge**: sort by start → merge overlapping/adjacent → `days - Σ(e - s + 1)`.
- **Alternative** (when `days` is small): difference array + prefix sum in `O(n + days)` time and `O(days)` space.


---

## ☀️ Complexity

- **Time**: `O(n log n)` for sorting + `O(n)` scan. If meetings are already sorted by start, overall `O(n)`.
- **Space**: `O(1)` auxiliary (excluding any temporary merged list in Solution 1; the result is a scalar).


---

## ☀️ Coding Walkthrough Script 

- I sort the meeting intervals by start so I can process them chronologically.
- For counting free days I don’t need to materialize the merged list; instead, I track the rightmost covered day `prev_end`.
- For each interval `[s, e]`:
  - If `s > prev_end`, the gap `(prev_end+1 .. s-1)` contributes `s - prev_end - 1` free days.
  - I extend coverage with `prev_end = max(prev_end, e)` to absorb overlaps or adjacency.
- After scanning all intervals, I add the tail gap `days - prev_end` if any.
- Because intervals are closed, I use `-1` and `+1` carefully for gaps and lengths.
- The overall time is `O(n log n)` due to sorting and uses `O(1)` extra space.


---

## ☀️ Common Pitfalls

- **Forgetting adjacency rule**: With closed intervals, `[a,b]` and `[b+1,c]` leave zero free days; treat them as mergeable.
- **Off‑by‑one**: Gap should be `s - prev_end - 1`; block length should be `e - s + 1`.
- **Forgetting the tail**: Always add `max(0, days - prev_end)` after the loop.
- **Not sorting**: If input isn’t sorted by start, sort first or logic breaks.


---

## ☀️ Quick Dry‑Run Example

```
days = 12
meetings = [[2,5],[1,3],[4,4],[6,6],[10,11],[11,12]]
sort -> [[1,3],[2,5],[4,4],[6,6],[10,11],[11,12]]

prev_end = 0, free = 0
[1,3]: s>prev_end? 1>0 → free += 0; prev_end = 3
[2,5]: 2<=3 → no gap; prev_end = 5
[4,4]: 4<=5 → no gap; prev_end = 5
[6,6]: 6>5  → free += 6-5-1 = 0; prev_end = 6
[10,11]: 10>6 → free += 10-6-1 = 3; prev_end = 11
[11,12]: 11<=11 → no gap; prev_end = 12
tail: days - prev_end = 12-12 = 0
answer = 3 (days 7, 8, 9)
```
