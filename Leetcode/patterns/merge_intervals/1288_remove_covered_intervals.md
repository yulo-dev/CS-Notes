# Leetcode 1288 — Remove Covered Intervals

## ☀️ UMPIRE

- **Understand**: Given a list of **closed** intervals `intervals[i] = [start_i, end_i]`, remove all intervals that are **covered** by another interval. Coverage rule (closed): `[a,b]` is covered by `[c,d]` iff `c ≤ a` **and** `b ≤ d` (equality counts).
- **Match**: Classic **Intervals** problem. Optimal approach is a **sort + one-pass scan** with a rightmost frontier. For learning, a brute-force coverage check is a good prior stage.
- **Plan**:
  - **Solution 1 (Prior Stage)**: For each interval, check if any other interval covers it (O(n²)).
  - **Solution 2 (Optimal)**: Sort by `(start ↑, end ↓)`; scan once while tracking `max_end`. If `end ≤ max_end` → covered; else keep it and update `max_end`.
- **Implement**: See code blocks below.
- **Review**:
  - Tie-break is crucial: **end must be DESC** when starts tie; otherwise short intervals may be counted before their cover-ers.
  - Use `<=` when testing coverage (closed intervals).
- **Evaluate**:
  - **Time**: `O(n log n)` for sorting + `O(n)` scan (optimal). Brute-force is `O(n²)`.
  - **Space**: `O(1)` auxiliary for both (excluding input).


---

## ☀️ Why the Sorting Key is (start ↑, end ↓)

When two intervals share the same start, the longer one must come **first**. With `(start ↑, end ↓)`, potential **cover-ers** precede potential **cover-ees**. Then a single `max_end` suffices:

- Example (bad if you sort end ascending): `[[1,3],[1,4]]`
  - If `[1,3]` is visited first, you'll count it, then later see `[1,4]` (its cover-er) and **cannot undo** the mistake.
  - With `end ↓`: visit `[1,4]` first → set `max_end=4`; then `[1,3]` has `end=3 ≤ 4` → correctly marked as covered.


---

## ☀️ Edge Cases

| Case | Input | Explanation | Output |
|---|---|---|---|
| No cover | `[[1,2],[2,3]]` | Touching is **not** covering | `2` |
| Same start | `[[1,4],[1,3]]` | `[1,3]` covered by `[1,4]` | `1` |
| Fully nested | `[[1,10],[2,3],[4,8]]` | Only `[1,10]` remains | `1` |
| Multiple covers | `[[1,4],[3,6],[2,8]]` | `[3,6]` covered by `[2,8]` | `2` |
| Identical intervals | `[[1,4],[1,4]]` | One covers the other (equality counts) | `1` |


---

## ☀️ Code — Solution 1 (Prior Stage, Brute-Force O(n²))

```python
from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        Brute-force coverage check.
        For each interval i, search any interval j that covers it:
        [a,b] is covered by [c,d] iff c <= a and b <= d (closed intervals; equality counts).
        Time:  O(n^2)
        Space: O(1) extra
        """
        n = len(intervals)
        uncovered = 0

        for i in range(n):
            s_i, e_i = intervals[i]
            covered = False
            for j in range(n):
                if i == j:
                    continue
                s_j, e_j = intervals[j]
                if s_j <= s_i and e_i <= e_j:  # coverage check (<= on both sides)
                    covered = True
                    break
            if not covered:
                uncovered += 1

        return uncovered
```


---

## ☀️ Code — Solution 2 (Optimal, Sort + One Pass, O(n log n))

```python
from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        Optimal approach:
        1) Sort by (start asc, end desc) so longer intervals with the same start appear first.
        2) One pass, track the rightmost end 'max_end':
           - If current end <= max_end: the interval is covered → skip
           - Else: it's not covered → count += 1, update max_end

        Rationale for end DESC on ties:
        - For [1,4] and [1,3], we visit [1,4] first (max_end=4),
          then [1,3] has end 3 <= 4 → covered. Without DESC, we'd count [1,3] incorrectly.

        Time:  O(n log n) for sorting + O(n) scan
        Space: O(1) auxiliary
        """
        # Crucial tie-break: end DESC ensures potential cover-ers come first
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_end = float('-inf')

        for s, e in intervals:
            if e > max_end:       # not covered by any previous interval
                count += 1
                max_end = e       # extend frontier
            # else: covered → do nothing

        return count
```


---

## ☀️ Coding Walkthrough Script 

- I'll start by recognizing this is an **Intervals + Coverage** problem; I don't need the merged list, only how many remain after removing covered ones.
- To make a single pass possible, I'll sort the intervals by **start ascending** and, on ties, **end descending**. That guarantees that for the same start, the longer interval appears before the shorter one.
- I'll keep a single state variable, `max_end`, representing the **rightmost end** among all intervals I've kept so far, and a `count` for how many are not covered.
- Then I scan left to right:
  - For the current `[s, e]`, if `e > max_end`, it **cannot** be covered by any earlier interval (since earlier ones have `start ≤ s` and the largest `end` seen so far is `max_end < e`). I increment `count` and set `max_end = e`.
  - Otherwise (`e ≤ max_end`), the current interval is **covered** by some earlier interval (possibly the one with the same start and larger end), so I skip it.
- Because intervals are **closed**, coverage uses `<=` on the right end—equal ends still count as covered.
- The loop runs once, so the scan is `O(n)` after sorting; sorting dominates at `O(n log n)`. The extra space is `O(1)`.
- If asked about correctness, I highlight the **tie-break**: without `end` descending, a shorter interval with the same start might be counted before its longer coverer is seen, and we can't undo that in a one-pass scan.

---

## ☀️ Tags / Data Structure / Algorithm

**Tags**: Intervals, Sorting, Greedy, One-pass scan, Array  
**Data Structure**: `List[List[int]]` of closed intervals `[start, end]`; working vars: `max_end`, `count`.  
**Algorithm (Optimal)**:
1. Sort `intervals` by `(start asc, end desc)`.
2. Initialize `count = 0`, `max_end = -inf`.
3. For each `[s, e]`:
   - If `e > max_end` → **not covered** → `count += 1`, `max_end = e`.
   - Else (`e <= max_end`) → **covered** → skip.
4. Return `count`.


---

## ☀️ Complexity

- **Time**: `O(n log n)` (sort) + `O(n)` scan.
- **Space**: `O(1)` auxiliary.


---

## ☀️ Quick Dry‑Runs

### Example A
```
intervals = [[1,3],[1,4]]
sort -> [[1,4],[1,3]]
scan:
  [1,4]: e=4 > -inf → count=1, max_end=4
  [1,3]: e=3 <= 4   → covered
answer = 1
```

### Example B
```
intervals = [[1,4],[3,6],[2,8]]
sort -> [[1,4],[2,8],[3,6]]
scan:
  [1,4]: e=4  > -inf → count=1, max_end=4
  [2,8]: e=8  > 4    → count=2, max_end=8
  [3,6]: e=6 <= 8    → covered
answer = 2
```

### Example C
```
intervals = [[1,10],[2,3],[4,8]]
sort -> [[1,10],[2,3],[4,8]]
scan:
  [1,10]: e=10 > -inf → count=1, max_end=10
  [2,3]:  e=3  <= 10  → covered
  [4,8]:  e=8  <= 10  → covered
answer = 1
```
