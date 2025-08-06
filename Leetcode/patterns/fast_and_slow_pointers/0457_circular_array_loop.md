
# LeetCode 457: Circular Array Loop

## Problem Statement
Given a circular array `nums` of integers, where each value represents the number of steps to move forward (if positive) or backward (if negative), 
determine if the array contains a **cycle**:
- The cycle must have length > 1
- All movement within the cycle must follow the **same direction** (all positive or all negative)

Return `True` if there is such a cycle, otherwise return `False`.

---

## UMPIRE Approach

### Understand
- Movement wraps around the array (`% n`)
- Valid cycle:
  - Length > 1
  - All values in the path have the same sign (direction)
- Single-element loop (element pointing to itself) is **not valid**

### Match
- Detecting cycles in linked structures → **Floyd's Tortoise and Hare Algorithm**
- Additional check for direction consistency and single-element loops

### Plan
1. Iterate through each index as a potential start point.
2. Use two pointers (slow and fast) to detect a cycle.
3. Check direction consistency at every step.
4. Skip processing indexes already marked as visited.
5. Mark visited nodes as `0` to avoid reprocessing (O(n) overall).

### Implement (Python)
```python
from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        # Calculate next index (handles circular array wrapping)
        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:  # Already processed
                continue

            direction = nums[i] > 0  # True if forward, False if backward
            slow = fast = i

            # Floyd's Cycle Detection
            while True:
                # Move slow pointer one step
                if (nums[slow] > 0) != direction:
                    break
                slow = next_index(slow)
                if (nums[slow] > 0) != direction:
                    break

                # Move fast pointer two steps
                fast = next_index(fast)
                if (nums[fast] > 0) != direction:
                    break
                fast = next_index(fast)
                if (nums[fast] > 0) != direction:
                    break

                # Cycle detected
                if slow == fast:
                    # Single-element loop check
                    if slow == next_index(slow):
                        break
                    return True

            # Mark visited nodes as 0
            marker = i
            while nums[marker] != 0 and (nums[marker] > 0) == direction:
                next_pos = next_index(marker)
                nums[marker] = 0
                marker = next_pos

        return False
```

---

### Complexity Analysis
- **Time Complexity**: O(n) → Each element visited at most once
- **Space Complexity**: O(1) → In-place marking as visited

---

## Script 
We need to check if there is a cycle in this circular array where all movement is in the same direction and length greater than one.
A single element pointing to itself does not count as a valid cycle.
First, I define a helper function next_index(i) which moves from the current index by nums[i] steps and wraps around the array using modulo.
This ensures forward and backward moves always stay within valid indices.
I iterate through each index as a potential starting point.
If it’s already visited (marked as 0), I skip it.
For each start, I check the direction based on whether nums[i] is positive or negative.
Then I use two pointers, slow and fast.
Slow moves one step, fast moves two steps, and at every move I ensure the direction stays consistent.
If direction changes, that path is invalid, so I break.
If slow and fast meet, we might have a cycle.
But I check one more condition: if the cycle length is only one element (meaning it points back to itself), it’s invalid.
Otherwise, we return True.
After exploring one path and not finding a valid cycle,
I mark all visited nodes in this path as 0 so they won’t be checked again.
This step guarantees each index is processed at most once, giving O(n) time complexity.
This solution runs in O(n) time and O(1) space since we reuse the input array for visited marking.
It’s essentially Floyd’s cycle detection plus extra conditions for direction and cycle length.
