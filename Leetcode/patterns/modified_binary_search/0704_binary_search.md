# Leetcode 0704 - Binary Search

## ☀️ UMPIRE

**Understand:** Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return -1.

**Match:** This is a classic Binary Search problem. The optimal approach is to use the divide-and-conquer strategy to eliminate half of the search space in each iteration.

**Plan:**
1. Initialize two pointers: `left = 0` and `right = len(nums) - 1`
2. While `left <= right`:
   - Calculate the middle index: `mid = left + (right - left) // 2`
   - If `nums[mid] == target`, return `mid`
   - If `nums[mid] < target`, search right half: `left = mid + 1`
   - If `nums[mid] > target`, search left half: `right = mid - 1`
3. If target not found, return -1

**Implement:** See the code section below.

**Review:**
- Ensure the loop condition is `left <= right` to handle single-element cases
- Use `left + (right - left) // 2` to prevent integer overflow in other languages
- Handle the case where target is not found

**Evaluate:**
- Time: O(log n) - we eliminate half of the search space each iteration
- Space: O(1) - only using constant extra space

## ☀️ Why This Is a Binary Search Problem

Since the array is sorted, we can leverage this property to eliminate half of the search space at each step:
- Compare target with middle element
- If target is smaller, it can only be in the left half
- If target is larger, it can only be in the right half
- This reduces the problem size by half each time

Key insights:
- Sorted array enables efficient search
- No need to check every element linearly
- Logarithmic time complexity is optimal for this problem

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `nums = [-1,0,3,5,9,12], target = 9` | Target exists in array | `4` |
| `nums = [-1,0,3,5,9,12], target = 2` | Target doesn't exist | `-1` |
| `nums = [5], target = 5` | Single element, target found | `0` |
| `nums = [5], target = -5` | Single element, target not found | `-1` |
| `nums = [1,2], target = 1` | Target at beginning | `0` |
| `nums = [1,2], target = 2` | Target at end | `1` |

These test:
- Standard binary search functionality
- Target not present in array
- Single-element arrays
- Boundary conditions (first/last elements)

## ☀️ Code (Iterative Binary Search)

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary Search - Optimal Solution
        Time: O(log n) - eliminate half search space each iteration
        Space: O(1) - only using constant extra space for pointers
        """
        left = 0
        right = len(nums) - 1
        
        # Continue searching while search space is valid
        while left <= right:
            # Calculate middle index (prevents overflow in other languages)
            mid = left + (right - left) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            # Target is in the right half
            elif nums[mid] < target:
                left = mid + 1
            # Target is in the left half
            else:
                right = mid - 1
        
        # Target not found in the array
        return -1
```

## ☀️ Notes

- `left + (right - left) // 2` prevents integer overflow in languages like C++/Java
- `while left <= right:` ensures we check single-element cases (when left == right)
- The `elif` structure makes the three mutually exclusive cases clear
- Time complexity is O(log n) because we halve the search space each iteration

## ☀️ Coding Walkthrough Script

"First, I initialize two pointers: left at index 0 and right at the last index of the array.
I use a while loop that continues as long as left is less than or equal to right, ensuring we check all valid search spaces including single elements.
In each iteration, I calculate the middle index using left plus right minus left divided by 2. This prevents integer overflow in languages like C++ or Java.
I then compare the middle element with the target. If they're equal, I return the middle index as we found our target.
If the middle element is less than the target, the target must be in the right half, so I update left to mid plus 1.
Otherwise, the target must be in the left half, so I update right to mid minus 1.
If the loop exits without finding the target, I return -1 to indicate the target is not in the array."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Notes |
|--------|----------------|------------------|-------|
| Linear Search | O(n) | O(1) | Brute force approach, ignores sorted property |
| Binary Search (Iterative) | O(log n) | O(1) | **Recommended**; optimal and clear |
| Binary Search (Recursive) | O(log n) | O(log n) | Same logic but uses recursion stack |

## ☀️ Binary Search Insights

- **Prerequisite:** Array must be sorted
- **Core idea:** Eliminate half of the search space each iteration
- **Loop invariant:** If target exists, it's always within [left, right] range
- **Termination:** Either find target or left > right (search space exhausted)
- **Overflow prevention:** Use `left + (right - left) // 2` instead of `(left + right) // 2`
