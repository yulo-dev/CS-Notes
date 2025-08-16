# Leetcode 0034 - Find First and Last Position of Element in Sorted Array

## ☀️ UMPIRE

**Understand:** Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.

**Match:** This is a Modified Binary Search problem specifically for boundary search. The key insight is that we need to find the leftmost and rightmost occurrences of the target using two separate binary searches with different convergence strategies.

**Plan:**
1. Use two modified binary searches instead of one standard binary search
2. First search: Find the leftmost occurrence of target
3. Second search: Find the rightmost occurrence of target
4. Key modification: Continue searching even after finding target to locate boundaries

**Implement:** See the code section below.

**Review:**
- Ensure we meet the O(log n) time complexity requirement
- Verify that >= and <= conditions correctly guide boundary search
- Handle edge cases like empty array and target not found
- Test with arrays containing duplicates

**Evaluate:**
- Time: O(log n) - two separate binary searches
- Space: O(1) - only using constant extra space

## ☀️ Why This Is a Modified Binary Search Problem

This problem requires boundary search rather than standard binary search:
- **Standard binary search**: Stops when target is found
- **Boundary search**: Continues searching even after finding target to locate edges
- **Duplicate elements**: Multiple occurrences of target require finding range
- **Different convergence**: Left search converges to first occurrence, right search to last

Key insights:
- We can't just find one target and expand linearly (would be O(n))
- Need to "greedily" search for boundaries using modified conditions
- Left boundary: Use >= condition to keep searching left when target found
- Right boundary: Use <= condition to keep searching right when target found

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `nums = [5,7,7,8,8,10], target = 8` | Target exists with duplicates | `[3,4]` |
| `nums = [5,7,7,8,8,10], target = 6` | Target doesn't exist | `[-1,-1]` |
| `nums = [], target = 0` | Empty array | `[-1,-1]` |
| `nums = [1], target = 1` | Single element, target found | `[0,0]` |
| `nums = [1], target = 2` | Single element, target not found | `[-1,-1]` |
| `nums = [2,2,2,2,2], target = 2` | All elements are target | `[0,4]` |
| `nums = [1,2,3,4,5], target = 3` | Target exists once | `[2,2]` |
| `nums = [1,1,2,2,3,3], target = 2` | Target in middle with duplicates | `[2,3]` |

These test:
- Normal boundary search scenarios
- Single vs multiple occurrences
- Edge positions (first, last, middle)
- Empty input validation
- Complete array being target

## ☀️ Code

### Solution 1: Linear Search (Naive Approach)
**Time: O(n) → May need to scan entire array**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Linear search to find first and last occurrence
        
        This approach is straightforward but doesn't meet the O(log n) requirement.
        Used here to demonstrate the basic idea before optimization.
        """
        if not nums:
            return [-1, -1]
        
        first = -1
        last = -1
        
        # Find first occurrence
        for i in range(len(nums)):
            if nums[i] == target:
                first = i
                break
        
        if first == -1:
            return [-1, -1]
        
        # Find last occurrence
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                last = i
                break
        
        return [first, last]
```

### Solution 2: Two Binary Searches (Optimal Approach)
**Time: O(log n) → Two separate binary searches**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Use two modified binary searches to find left and right boundaries
        
        Key Insight:
        - Find left boundary: Continue searching left even after finding target
        - Find right boundary: Continue searching right even after finding target
        - Use >= and <= conditions to control search direction
        """
        if not nums:
            return [-1, -1]
        
        def findLeft(nums, target):
            """Find the leftmost (first) occurrence of target"""
            left, right = 0, len(nums) - 1
            index = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] >= target:
                    right = mid - 1  # Continue searching left
                else:
                    left = mid + 1   # Search right
                
                if nums[mid] == target:
                    index = mid      # Record this occurrence
            
            return index
        
        def findRight(nums, target):
            """Find the rightmost (last) occurrence of target"""
            left, right = 0, len(nums) - 1
            index = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] <= target:
                    left = mid + 1   # Continue searching right
                else:
                    right = mid - 1  # Search left
                
                if nums[mid] == target:
                    index = mid      # Record this occurrence
            
            return index
        
        return [findLeft(nums, target), findRight(nums, target)]
```

### Solution 3: Unified Binary Search (Most Elegant)
**Time: O(log n) → Two separate binary searches**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Most elegant approach using a helper function for boundary search
        """
        if not nums:
            return [-1, -1]
        
        def binarySearch(nums, target, findLeft):
            """
            Generic binary search for finding boundaries
            
            Args:
                findLeft: If True, find left boundary; if False, find right boundary
            """
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    result = mid
                    if findLeft:
                        right = mid - 1  # Continue searching left
                    else:
                        left = mid + 1   # Continue searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        left_bound = binarySearch(nums, target, True)
        if left_bound == -1:
            return [-1, -1]
        
        right_bound = binarySearch(nums, target, False)
        return [left_bound, right_bound]
```

## ☀️ Notes

**Key Algorithm Components:**
- **Boundary search template**: Modified binary search that continues after finding target
- **Left boundary strategy**: Use `nums[mid] >= target` to keep searching left
- **Right boundary strategy**: Use `nums[mid] <= target` to keep searching right
- **Recording mechanism**: Save each found occurrence, final one is the boundary

**Critical Insight:**
The algorithm works by being "greedy" about finding boundaries. Instead of stopping when target is found, it continues searching in the direction of the desired boundary, recording each occurrence along the way.

## ☀️ Boundary Search Logic Explained

```
Array: [1, 3, 8, 8, 8, 10, 15]
Index:  0  1  2  3  4   5   6
Target: 8 (positions 2, 3, 4)

Left Boundary Search:
- When nums[mid] >= 8: Continue left (includes == case)
- Records positions: 3 → 2 (final answer: leftmost)

Right Boundary Search:  
- When nums[mid] <= 8: Continue right (includes == case)
- Records positions: 3 → 4 (final answer: rightmost)
```

## ☀️ Coding Walkthrough Script

"I need to find the range of a target in a sorted array with O(log n) complexity.
Since the array can have duplicates, I can't just use standard binary search which stops at any occurrence. I need to find the leftmost and rightmost positions specifically.
My approach is to use two modified binary searches:
For the left boundary, I'll use a condition `nums[mid] >= target`. This means even when I find the target, I continue searching left to see if there's an earlier occurrence. I record each target I find, so the final recorded position will be the leftmost.
For the right boundary, I'll use `nums[mid] <= target`. This means even when I find the target, I continue searching right for later occurrences. Again, the final recorded position will be the rightmost.
The key insight is that when `nums[mid] < target` or `nums[mid] > target`, the logic is identical to standard binary search. The special handling only applies when we find the target.
This gives me two O(log n) searches, so overall O(log n) complexity."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Linear Search | O(n) | O(1) | Scan from both ends | Simple but doesn't meet requirement |
| Two Binary Searches | O(log n) | O(1) | Separate boundary searches | **Optimal**; most intuitive |
| Unified Binary Search | O(log n) | O(1) | Single function with parameter | Most elegant; reduces code duplication |
| Expand from center | O(n) worst case | O(1) | Find any, then expand | Poor worst case when all elements are target |

## ☀️ Boundary Search Insights

- **Prerequisites:** Array must be sorted for binary search to work
- **Core insight:** Continue searching beyond finding target to locate boundaries
- **Template difference:** `>=` and `<=` conditions vs `==` in standard binary search
- **Recording strategy:** Track each occurrence, final one is the boundary
- **Comparison with LeetCode 35:** Different from insert position (no duplicates)
- **Boundary guarantee:** Left search finds first, right search finds last occurrence

**Mathematical Guarantee:** Since we continue searching past each found target in the direction of the desired boundary, we will eventually find the extreme occurrence (leftmost or rightmost) in logarithmic time.

**Note:** Solution 1 demonstrates basic understanding but doesn't meet complexity requirements. Solution 2 is the recommended approach for interviews due to its clear logic. Solution 3 shows advanced design skills by eliminating code duplication through parameterization.
