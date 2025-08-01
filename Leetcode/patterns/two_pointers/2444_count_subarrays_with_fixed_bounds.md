
# Leetcode 2444 - Count Subarrays With Fixed Bounds

## ☀️ UMPIRE

### Understand:
- **Input**:
  - `nums`: An integer array.
  - `minK`: An integer representing the required minimum value in the subarray.
  - `maxK`: An integer representing the required maximum value in the subarray.
- **Output**: Count of contiguous subarrays where:
  - The minimum value equals `minK`.
  - The maximum value equals `maxK`.
- **Constraints**:
  - n can be up to 10^5 → need O(n) or O(n log n) solution.

### Match:
- **Category**: Array traversal and subarray counting.
- **Patterns**:
  - Sliding Window with index tracking for bounds.
  - State-based counting.

### Plan (Optimized O(n)):
1. Initialize:
   - `answer = 0`
   - `leftBound = -1` (last index of an invalid number)
   - `minPos = -1` (last index of minK)
   - `maxPos = -1` (last index of maxK)
2. Iterate through array index `i`:
   - If `nums[i] < minK or nums[i] > maxK`, update `leftBound = i`.
   - If `nums[i] == minK`, update `minPos = i`.
   - If `nums[i] == maxK`, update `maxPos = i`.
   - Add `max(0, min(minPos, maxPos) - leftBound)` to `answer`.
3. Return `answer`.

### Review:
- Are invalid values resetting correctly?
- Are both minK and maxK required for counting?
- Are indices handled correctly?

### Evaluate:
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

---

## ☀️ Code (Sliding Window Index Tracking)
```python
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        leftBound = -1   # last index of an invalid number
        minPos = -1      # last index of minK
        maxPos = -1      # last index of maxK

        for i, num in enumerate(nums):
            # If number is out of range, reset the boundary
            if num < minK or num > maxK:
                leftBound = i
            # Track positions of minK and maxK
            if num == minK:
                minPos = i
            if num == maxK:
                maxPos = i
            # Count valid subarrays ending at index i
            answer += max(0, min(minPos, maxPos) - leftBound)

        return answer
```

---

## ☀️ Coding Walkthrough Script
1. Traverse each number in `nums`.
2. Update the last index where `minK`, `maxK`, and any invalid number appeared.
3. At each step, find how many valid subarrays end at index `i` by checking how far back we can go while keeping `minK` and `maxK` present and avoiding invalid numbers.
4. Add this count to the result.

---

## ☀️ Complexity Comparison
| Method        | Time Complexity | Space Complexity | Notes                     |
|---------------|----------------|------------------|---------------------------|
| Brute Force   | O(n²)          | O(1)             | Check all subarrays       |
| Sliding Window| O(n)           | O(1)             | Index tracking solution   |

---

## ☀️ Edge Cases
- All values are equal to minK = maxK → every subarray is valid.
- No minK or maxK in array → return 0.
- Numbers outside [minK, maxK] split the array into segments.

---

## ☀️ Metadata
- **Tags**: Array, Sliding Window, Index Tracking, Subarray Counting
- **Data Structures**: Array (List), Scalar index trackers
- **Algorithms**:
  1. Sliding Window + Index Tracking (O(n), recommended)
  2. Brute Force (O(n²), for clarity only)
