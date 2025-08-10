# Leetcode 0056 - Merge Intervals

## ☀️ UMPIRE

- **Understand**: Given an array of intervals `intervals[i] = [start_i, end_i]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

- **Match**: This is a classic **Intervals** problem. The optimal approach is to **sort by start time** and then sweep through to merge overlapping intervals.

- **Plan**:
  - Sort the intervals by their start time.
  - Initialize an empty list `merged` to hold the merged intervals.
  - For each interval:
    - If `merged` is empty OR current start is greater than the last merged end → start a new interval.
    - Else → intervals overlap → update the last merged interval's end to `max(last_end, current_end)`.
  - Return `merged`.

- **Implement**: See the code section below.

- **Review**:
  - Ensure sorting is done by start time.
  - Be careful with the overlap condition: `>` not `>=` so that touching intervals `[1,4]` and `[4,5]` are merged.

- **Evaluate**:
  - Time: O(n log n) due to sorting + O(n) scan.
  - Space: O(1) auxiliary (excluding output), O(n) if counting output.

---

## ☀️ Why This Is an Intervals Problem

By sorting intervals by their start time, any possible overlap can only happen with the most recently merged interval. This allows a single linear pass to merge efficiently.

- No need for nested comparisons.
- Sorting ensures predictable processing order.
- Merging only requires comparing with the last merged interval.

---

## ☀️ Edge Case Notes

| Input                               | Description                                 | Expected Output                |
| ----------------------------------- | ------------------------------------------- | ------------------------------- |
| `[[1,3],[2,6],[8,10],[15,18]]`      | Overlapping and non-overlapping intervals   | `[[1,6],[8,10],[15,18]]`        |
| `[[1,4],[4,5]]`                     | Touching intervals                          | `[[1,5]]`                       |
| `[[1,10],[2,3],[4,8]]`              | Intervals fully contained within another    | `[[1,10]]`                      |
| `[[1,2],[3,4]]`                     | All non-overlapping                         | `[[1,2],[3,4]]`                  |
| `[[5,7]]`                           | Single interval                             | `[[5,7]]`                        |

These test:
- Merging of overlapping intervals.
- Merging of touching intervals.
- Handling of contained intervals.
- Cases with no merges.
- Single-element input.

---

## ☀️ Code (Sort + Single Pass)

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge Intervals - Canonical Solution
        Time: O(n log n) due to sorting + O(n) scan
        Space: O(1) auxiliary (excluding output), O(n) if counting output
        """
        if not intervals:
            return []

        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = []  # result list for merged intervals

        # Step 2: Sweep through the intervals
        for start, end in intervals:
            # Case 1: No merged intervals yet OR no overlap with last merged interval
            if not merged or start > merged[-1][1]:
                merged.append([start, end])  # start a new merged block
            else:
                # Case 2: Overlap exists → extend the last merged interval's end
                merged[-1][1] = max(merged[-1][1], end)

        return merged
```

---

## ☀️ Notes

- `intervals.sort(key=lambda x: x[0])` sorts the list of intervals by their start time.
- `if not merged or start > merged[-1][1]:`  
  - `not merged` handles the very first interval.
  - `start > merged[-1][1]` checks if there is **no overlap** with the last merged interval.
- Overlap is determined by comparing current start with last merged end.

---

## ☀️ Coding Walkthrough Script

- First, I check if `intervals` is empty and return an empty list if so.
- I sort `intervals` by start time so overlapping intervals are positioned consecutively.
- I create an empty list `merged` to store the merged intervals.
- For each interval `(start, end)` in `intervals`:
  - If `merged` is empty or there is no overlap (`start > merged[-1][1]`), I append a new interval `[start, end]` to `merged`.
  - Otherwise, I merge the intervals by updating `merged[-1][1]` to `max(merged[-1][1], end)`.
- At the end, I return `merged`.

---

## ☀️ Brute Force vs Sort + Single Pass vs In-Place

| Method                  | Time Complexity        | Space Complexity (aux) | Notes                                               |
| ----------------------- | ---------------------- | ----------------------- | --------------------------------------------------- |
| Brute Force             | O(n²) ~ O(n³)          | O(1)                    | Repeated pairwise merge until no change             |
| Sort + Single Pass      | O(n log n)             | O(1)                    | Recommended; clear and efficient                    |
| In-Place Write-Index    | O(n log n)             | O(1)                    | Same logic as single pass but reuses original array |

---

## ☀️ Intervals Insights

- Sorting by start time reduces the merging problem to a linear pass.
- Merging only requires maintaining the latest merged interval's end.
- Edge cases often involve:
  - Touching intervals `[a,b]` and `[b,c]`
  - Fully contained intervals
  - Inputs already sorted vs unsorted

---
