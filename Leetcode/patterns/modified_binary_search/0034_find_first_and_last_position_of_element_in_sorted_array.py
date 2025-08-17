# LeetCode 34: Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""
Problem Statement:
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""

from typing import List

# Solution 1: Naive Approach - Linear Search (Not optimal)
# Time: O(n) → May need to scan entire array
# Space: O(1) → Only using constant extra space
class Solution1:
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


# Solution 2: Two Binary Searches (Optimal Approach)
# Time: O(log n) → Two separate binary searches
# Space: O(1) → Only using constant extra space
class Solution2:
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
      

# Solution 3: Single Pass with Boundary Search (Most Elegant)
# Time: O(log n) → Two separate binary searches
# Space: O(1) → Only using constant extra space
class Solution3:
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

"""
Key Insights and Takeaways:

1. Problem Classification:
   - This is a boundary search problem, not a simple binary search
   - Requires finding first and last occurrence of a target in sorted array

2. Core Technique - Modified Binary Search:
   - Left boundary: When nums[mid] >= target, continue searching left
   - Right boundary: When nums[mid] <= target, continue searching right
   - The key is to "greedily" continue searching even after finding target

3. Why This Works:
   - Left search: >= condition ensures we find the leftmost target
   - Right search: <= condition ensures we find the rightmost target
   - Each found target is recorded, with the final one being the boundary

4. Template Recognition:
   - This is different from LeetCode 35 (Search Insert Position)
   - LeetCode 35 has no duplicates, so standard binary search works
   - LeetCode 34 has duplicates, requiring boundary search template

6. Common Mistakes to Avoid:
   - Don't expand linearly from found position (makes it O(n))
   - Remember to handle edge cases (empty array, target not found)
   - Use >= and <= conditions correctly for boundary search

7. Related Problems:
   - LeetCode 278: First Bad Version
   - LeetCode 35: Search Insert Position  
   - LeetCode 69: Sqrt(x)
   - LeetCode 875: Koko Eating Bananas
"""
