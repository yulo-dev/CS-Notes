
# Leetcode 2824 - Count Pairs Whose Sum is Less than Target

## ☀️ UMPIRE

### Understand:
- **Input**:  
  - `nums`: A list of integers.  
  - `target`: An integer target value.
- **Output**: Count the number of index pairs `(i, j)` such that:  
  - `i < j`  
  - `nums[i] + nums[j] < target`
- **Goal**: Count valid pairs efficiently.

### Match:
- **Category**: Array pair counting.
- **Patterns**:
  - Sorting + Two Pointers.
  - Brute Force vs Optimized.

### Plan:
#### Method 1: Brute Force (for clarity)
1. Initialize `count = 0`.
2. Double loop through `nums`, check all pairs `(i, j)` with `i < j`.
3. Increment count if `nums[i] + nums[j] < target`.

#### Method 2 (Preferred): Sort + Two Pointers
1. Sort `nums`.
2. Initialize `left = 0`, `right = len(nums) - 1`, `count = 0`.
3. While `left < right`:
   - If `nums[left] + nums[right] < target`:
     - Add `(right - left)` to count.
     - Move `left` rightward.
   - Else move `right` leftward.

### Review:
- Are indices correctly handled (`i < j`)?
- Are duplicates handled correctly? (Yes, naturally counted.)
- Is time complexity acceptable? (Yes, O(n log n) due to sorting.)

### Evaluate:
- Method 1: Time O(n²), Space O(1)
- Method 2: Time O(n log n), Space O(1)

---

## ☀️ Code (Method 1: Brute Force)
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Initialize pair count
        count = 0
        n = len(nums)
        
        # Check all possible pairs (i, j) where i < j
        for i in range(n):
            for j in range(i + 1, n):
                # If the sum of the pair is less than target, count it
                if nums[i] + nums[j] < target:
                    count += 1
        
        # Return the total count of valid pairs
        return count
```

---

## ☀️ Code (Method 2: Sort + Two Pointers)
```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Sort the numbers to use the two-pointer technique
        nums.sort()
        count = 0
        
        # Initialize two pointers
        left, right = 0, len(nums) - 1
        
        # Move pointers until they meet
        while left < right:
            # If the sum of the smallest and largest numbers is less than target
            if nums[left] + nums[right] < target:
                # All elements from (left+1) to right with nums[left] are valid pairs
                count += (right - left)
                # Move left pointer to consider next element
                left += 1
            else:
                # Sum is too large, decrease the right pointer to reduce sum
                right -= 1
        
        # Return the total count of valid pairs
        return count
```

---

## ☀️ Coding Walkthrough Script
1. Sort the array.
2. Use two pointers to find valid pairs efficiently.
3. If `nums[left] + nums[right] < target`, then all pairs between left and right are valid.
4. Adjust pointers until they meet.

---

## ☀️ Complexity Comparison
| Method       | Time Complexity | Space Complexity | Notes                     |
|--------------|----------------|------------------|---------------------------|
| Brute Force  | O(n²)          | O(1)             | Simple but inefficient    |
| Two Pointers | O(n log n)     | O(1)             | Sort dominates complexity |

---

## ☀️ Edge Cases
- Empty array → returns 0
- Single element array → returns 0
- Negative numbers and mixed signs handled naturally
- Very small target → possibly 0 valid pairs
