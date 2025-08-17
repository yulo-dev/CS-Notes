
"""
Problem Statement:
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always 
considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, 
or index number 5 where the peak element is 6.

Constraints:
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i.
"""

from typing import List

# Solution 1: Linear Search (Naive Approach)
# Time: O(n) → May need to scan entire array
# Space: O(1) → Only using constant extra space
class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Approach: Linear search to find any peak element
        
        This approach is straightforward but doesn't meet the O(log n) requirement.
        Used here to demonstrate the basic idea before optimization.
        """
        n = len(nums)
        
        for i in range(n):
            # Check if current element is a peak
            left_smaller = (i == 0) or (nums[i - 1] < nums[i])
            right_smaller = (i == n - 1) or (nums[i] > nums[i + 1])
            
            if left_smaller and right_smaller:
                return i
        
        # Should never reach here given problem constraints
        return 0


# Solution 2: Binary Search with while left <= right (Boundary Check Approach)
# Time: O(log n) → Binary search eliminates half search space each iteration
# Space: O(1) → Only using constant extra space
class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Approach: Binary search with explicit boundary checking
        
        This approach uses the familiar while left <= right template.
        Key insight: When nums[mid] > nums[mid + 1], peak exists on left side (including mid).
        We use boundary checking to avoid array index out of bounds.
        """
        left, right = 0, len(nums) - 1
        result = 0  # Store potential peak index
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Boundary check to avoid index out of bounds
            if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
                # Peak condition satisfied or at last element
                result = mid  # Record this potential peak
                right = mid - 1  # Continue searching left for other peaks
            else:
                # nums[mid] <= nums[mid + 1], peak must be on right side
                left = mid + 1
        
        return result


# Solution 3: Binary Search with while left < right (Elegant Approach)
# Time: O(log n) → Binary search eliminates half search space each iteration
# Space: O(1) → Only using constant extra space
class Solution3:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Approach: Binary search with natural boundary handling
        
        This approach uses while left < right to naturally avoid boundary issues.
        Key insight: The condition guarantees mid + 1 is always valid.
        When nums[mid] > nums[mid + 1], peak exists on left side including mid.
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[mid + 1]:
                # Peak exists on left side (including mid)
                right = mid  # Keep mid as potential answer
            else:
                # Peak exists on right side (excluding mid)
                left = mid + 1
        
        # When left == right, we found the peak
        return left



"""
Key Insights and Takeaways:

1. Problem Classification:
   - Modified binary search on unsorted array
   - Uses peak properties rather than sorted properties
   - Guaranteed to have at least one peak

2. Core Technique - Peak-Based Binary Search:
   - Compare nums[mid] with nums[mid + 1]
   - If nums[mid] > nums[mid + 1]: peak on left side (including mid)
   - If nums[mid] <= nums[mid + 1]: peak on right side (excluding mid)

3. Template Choice:
   - Solution 2: Familiar while left <= right with boundary checking
   - Solution 3: Elegant while left < right with natural handling
   - Both are correct, choice depends on preference

4. Why This Works:
   - Array conceptually has -∞ at both ends
   - This guarantees at least one peak exists
   - Binary search efficiently narrows down to any peak

5. Interview Strategy:
   - Start with Solution 1 to show understanding
   - Mention O(log n) requirement
   - Implement either Solution 2 or 3 based on comfort
   - Explain the peak property logic clearly

6. Common Mistakes to Avoid:
   - Don't assume array is sorted (it's not!)
   - Remember to handle boundary conditions properly
   - Understand that any peak is valid (don't need specific one)

7. Related Problems:
   - LeetCode 852: Peak Index in a Mountain Array
   - LeetCode 1095: Find in Mountain Array
   - Problems involving local extrema in arrays

8. Template Decision:
   - Use Solution 2 if you prefer consistent while left <= right
   - Use Solution 3 if you want cleaner boundary handling
   - Both approaches are interview-ready
"""
