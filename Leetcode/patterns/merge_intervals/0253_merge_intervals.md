# Leetcode 0253 - Meeting Rooms II

## ☀️ UMPIRE

- **Understand**: Given an array of meeting time intervals `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required so that all meetings can take place without conflicts.

- **Match**: This is an **Intervals / Scheduling** problem. A common optimal approach is to **sort starts and ends separately** and use a sweep line (two pointers) to track concurrent meetings.

- **Plan**:
  - Extract all start times into one list and all end times into another.
  - Sort both lists.
  - Use two pointers `i` (start index) and `j` (end index), and a counter `rooms` for current rooms in use.
  - While there are unprocessed starts:
    - If `starts[i] < ends[j]`: Need a new room → increment `rooms` and move `i`.
    - Else (`starts[i] >= ends[j]`): A meeting has ended → decrement `rooms` and move `j`.
    - Track the maximum `rooms` seen as the answer.
  - Return the maximum `rooms`.

- **Implement**: See the code section below.

- **Review**:
  - Ensure sorting is done on both starts and ends.
  - Use `<` not `<=` in the comparison to handle `[s,e)` semantics (free at exact end time).
  - Always update the maximum rooms after incrementing.

- **Evaluate**:
  - Time: O(n log n) due to sorting + O(n) scan.
  - Space: O(n) for storing separate start and end arrays.

---

## ☀️ Why This Is an Intervals / Scheduling Problem

By separating start and end times, we only need to track **when rooms are occupied and freed**. Sorting ensures that we process events in chronological order, allowing a single linear sweep to compute the maximum overlap (minimum rooms needed).

- Avoids comparing every pair of intervals.
- Processing is predictable and efficient.
- The maximum concurrent meetings = the answer.

---

## ☀️ Edge Case Notes

| Input                               | Description                                       | Expected Output |
| ----------------------------------- | ------------------------------------------------- | --------------- |
| `[[0,30],[5,10],[15,20]]`           | Overlaps cause max concurrency of 2               | `2`             |
| `[[7,10],[2,4]]`                    | No overlaps → only 1 room needed                  | `1`             |
| `[[1,5],[5,10]]`                    | Touching intervals can reuse the same room        | `1`             |
| `[[1,10],[2,3],[4,8]]`              | Fully contained intervals still need only 1 room  | `1`             |
| `[[1,2],[1,2],[1,2]]`               | All start together → rooms = number of meetings   | `3`             |

These test:
- Standard overlapping scenarios.
- Non-overlapping cases.
- Touching intervals reuse.
- Contained intervals.
- Worst-case simultaneous start.

---

## ☀️ Code (Two Pointers Approach)

```python
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Two-pointers approach for minimum meeting rooms.
        Time: O(n log n) for sorting starts and ends.
        Space: O(n) for the two lists of starts and ends.
        """
        if not intervals:
            return 0

        starts = [s for s, _ in intervals]
        ends   = [e for _, e in intervals]
        starts.sort()
        ends.sort()

        i = j = 0
        rooms = ans = 0
        n = len(intervals)

        while i < n:
            if starts[i] < ends[j]:
                rooms += 1
                ans = max(ans, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1

        return ans
```

---

## ☀️ Notes

- `starts.sort()` and `ends.sort()` guarantee chronological order of events.
- If `starts[i] < ends[j]`, a new meeting starts before any current meeting ends → need another room.
- If `starts[i] >= ends[j]`, a meeting ends before or exactly at the next meeting's start → free a room first.

---

## ☀️ Coding Walkthrough Script

- First, check for empty input; return 0 if there are no meetings.
- Extract start and end times into separate arrays and sort both.
- Initialize pointers `i` (start index) and `j` (end index) to 0.
- Initialize counters `rooms` (current occupied rooms) and `ans` (max rooms seen).
- While there are unprocessed starts:
  - If the next meeting starts before the earliest ending meeting ends, increment `rooms` and move `i`.
  - Else, decrement `rooms` and move `j`.
  - Update `ans` after any increment of `rooms`.
- Return `ans` as the final result.

---

## ☀️ Brute Force vs Min-Heap vs Two Pointers

| Method          | Time Complexity | Space Complexity | Notes |
| --------------- | --------------- | ---------------- | ----- |
| Brute Force     | O(n²)           | O(1)              | Compare each pair for overlap. Too slow for large n. |
| Min-Heap        | O(n log n)      | O(n)              | Sort by start, push end times in heap, pop when room frees. |
| Two Pointers    | O(n log n)      | O(n)              | Sort starts & ends, sweep once. Smaller constant than heap. |

---

## ☀️ Scheduling Insights

- Only start/end events affect room count; meeting length is irrelevant.
- Sorting separates concerns: starts allocate rooms, ends free rooms.
- Careful with equality: handle `[start == end]` as freeing first to avoid extra room allocation.

---
