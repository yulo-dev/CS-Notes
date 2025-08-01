
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

---
## ☀️ Coding Walkthrough Script

For this problem, I need to count all subarrays whose minimum equals `minK` and maximum equals `maxK`.  
To do it efficiently in one pass, I track three indices as I traverse the array:  
  - `minPos`: the last index where `minK` occurred,
  - `maxPos`: the last index where `maxK` occurred,
  - `leftBound`: the last index where any number was out of range `[minK, maxK]`.  
 
Why do I need these three?  
Because to form a valid subarray ending at index `i`, I must know:  
 - where both `minK` and `maxK` have appeared, and  
 - how far back I can start without including invalid numbers.  

I initialize all of them to `-1` before starting.  
That means:  
  - initially, I haven’t seen `minK` or `maxK`, so `minPos` and `maxPos` are `-1`;  
 - and I treat the region before the array start as an implicit out-of-range position, so `leftBound` is `-1`.  
   
This initialization lets me use one formula for every index without extra if-statements.  
If one of the required values hasn’t appeared yet, then `min(minPos, maxPos)` will still be `-1`,  
so the count for that position naturally becomes zero.  

The key formula for counting valid subarrays ending at index `i` is:  
 ```python
result += max(0, min(minPos, maxPos) - leftBound)
```

Why does it work?  
 - `min(minPos, maxPos)` is the earliest index where both required numbers exist in the subarray.  
 - `leftBound` marks the last invalid element; we can’t start before it.  
 - The difference gives us how many valid start indices there are for subarrays ending at `i`.

If one value is missing, the result would be negative, so we clamp it to zero with `max(0, …)`.  
Finally, I scan the entire array once, updating these three variables and applying this formula at each step.  
This gives O(n) time complexity and O(1) extra space.
