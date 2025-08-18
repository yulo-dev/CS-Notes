"""
LeetCode 81 - Search in Rotated Sorted Array II

Problem Statement:
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at some pivot index k (0 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,4,4,5,6,7] might be rotated at pivot index 5 and become [4,5,6,7,0,1,2,4,4].

Given the array nums after the possible rotation and an integer target, 
return true if target is in nums, or false otherwise.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Example 3:
Input: nums = [1,0,1,1,1], target = 0
Output: true

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- nums is guaranteed to be rotated at some pivot.
- -10^4 <= target <= 10^4

Follow up: This problem is similar to Search in Rotated Sorted Array, 
where nums may contain duplicates. Would this affect the run-time complexity? How and why?
"""

from typing import List

# Solution 1: Linear Search (Naive Approach)
# Time: O(n) → Must scan entire array in worst case
# Space: O(1) → Only using constant extra space
class Solution1:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Approach: Linear search through the array
        
        This approach is straightforward but doesn't take advantage of the sorted nature.
        Simply iterate through the array to find the target.
        """
        return target in nums
        
        # Alternative explicit implementation:
        # for num in nums:
        #     if num == target:
        #         return True
        # return False


# Solution 2: Binary Search with Duplicate Handling (Optimal)
# Time: O(log n) average, O(n) worst case → Binary search with duplicate elimination
# Space: O(1) → Only using constant extra space
class Solution2:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Approach: Modified binary search for rotated array with duplicates
        
        Key Insights:
        1. Array is rotated, so one half is always sorted
        2. Duplicates can make it ambiguous which half is sorted
        3. When nums[left] == nums[mid] == nums[right], we can't determine rotation
        4. In ambiguous cases, eliminate duplicates from boundaries
        
        Strategy:
        - If we can identify the sorted half, check if target is in that range
        - If target is in sorted half, search there; otherwise search other half
        - When duplicates create ambiguity, shrink boundaries to eliminate duplicates
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Found target
            if nums[mid] == target:
                return True
            
            # Handle duplicates: when left, mid, right are all equal
            # We can't determine which half is sorted, so eliminate boundaries
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                # Check if target is in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left half
                else:
                    left = mid + 1   # Search right half
            else:  # Right half is sorted (nums[mid] < nums[right])
                # Check if target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Search right half
                else:
                    right = mid - 1  # Search left half
        
        return False


# Solution 3: Binary Search with Optimized Duplicate Elimination
# Time: O(log n) average, O(n) worst case → Binary search with smarter duplicate handling
# Space: O(1) → Only using constant extra space
class Solution3:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Optimized approach: More aggressive duplicate elimination
        
        Instead of eliminating one element at a time, we can eliminate
        all duplicates from boundaries more efficiently.
        """
        left, right = 0, len(nums) - 1
        
        # Remove duplicates from left boundary
        while left < right and nums[left] == nums[left + 1]:
            left += 1
        
        # Remove duplicates from right boundary  
        while left < right and nums[right] == nums[right - 1]:
            right -= 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            
            # Handle remaining duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            
            # Standard rotated array binary search logic
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False


# Solution 4: Recursive Binary Search (Alternative Implementation)
# Time: O(log n) average, O(n) worst case → Binary search with recursion
# Space: O(log n) → Recursion stack space
class Solution4:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Recursive approach for educational purposes
        
        Same logic as iterative version but implemented recursively.
        """
        def binary_search(left: int, right: int) -> bool:
            if left > right:
                return False
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            
            # Handle duplicates
            if nums[left] == nums[mid] == nums[right]:
                return binary_search(left + 1, right - 1)
            
            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return binary_search(left, mid - 1)
                else:
                    return binary_search(mid + 1, right)
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    return binary_search(mid + 1, right)
                else:
                    return binary_search(left, mid - 1)
        
        return binary_search(0, len(nums) - 1)


"""
Key Insights and Analysis:

1. Problem Classification:
   - Modified binary search with duplicates
   - Rotated sorted array search variant
   - Ambiguity resolution in binary search

2. Core Challenge - Duplicate Handling:
   - Duplicates can make it impossible to determine which half is sorted
   - When nums[left] == nums[mid] == nums[right], both halves could be valid
   - Solution: Eliminate boundary duplicates to restore determinism

3. Time Complexity Analysis:
   - Best case: O(log n) when no duplicates interfere
   - Average case: O(log n) for most practical inputs
   - Worst case: O(n) when array is mostly duplicates (e.g., [1,1,1,1,1,0,1])

4. Comparison with LeetCode 33 (without duplicates):
   - LC 33: Always O(log n) because no ambiguity
   - LC 81: O(n) worst case due to duplicate-induced ambiguity
   - Same core logic, additional duplicate handling needed

5. Why Duplicates Affect Complexity:
   - In worst case, we might need to eliminate n/2 duplicates
   - Each elimination is O(1), but n/2 eliminations = O(n)
   - Example: [1,1,1,1,1,0,1] searching for 0

6. Optimization Strategies:
   - Pre-eliminate boundary duplicates (Solution 3)
   - Early termination on target found
   - Minimize duplicate elimination operations

7. Interview Discussion Points:
   - Explain why duplicates create ambiguity
   - Discuss trade-off between worst-case and average-case performance
   - Compare with non-duplicate version (LC 33)
   - Mention that linear search might be acceptable for small arrays

8. Edge Cases to Consider:
   - All elements are the same
   - Target at rotation point
   - Array with length 1
   - Target not in array
   - Multiple occurrences of target

9. Alternative Approaches:
   - Could use two-pass: find rotation point, then binary search
   - For very small arrays, linear search might be faster due to constants
   - Advanced: use randomization to avoid worst-case (not typically expected)

Solution Recommendation:
- Solution 2 is the standard and most interview-appropriate
- Solution 3 shows optimization thinking
- Mention that worst-case O(n) is unavoidable due to duplicates
"""
