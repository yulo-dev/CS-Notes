"""
Problem Statement:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in 
the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the array nums after the possible rotation, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0

Example 3:
Input: nums = [11,13,15,17]
Output: 11

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times.
"""

from typing import List

# Solution 1: Linear Search (Naive Approach)
# Time: O(n) → May need to scan entire array
# Space: O(1) → Only using constant extra space
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        """
        Approach: Linear search to find minimum element
        
        This approach is straightforward but doesn't meet the O(log n) requirement.
        Simply iterate through the array to find the minimum value.
        Used here to demonstrate the basic idea before optimization.
        """
        min_val = nums[0]
        
        for num in nums:
            if num < min_val:
                min_val = num
        
        return min_val


# Solution 2: Binary Search with Position Convergence (Optimal)
# Time: O(log n) → Binary search eliminates half search space each iteration
# Space: O(1) → Only using constant extra space
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        """
        Approach: Binary search to find the rotation point (minimum element)
        
        Key Insight:
        - The minimum element is at the rotation point
        - Compare nums[mid] with nums[right] to determine which side contains the rotation
        - If nums[mid] > nums[right]: rotation point is on the right side
        - If nums[mid] <= nums[right]: left side is sorted or mid is the minimum
        
        We use while left < right for position convergence, similar to peak finding.
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # Right side contains the rotation point (minimum)
                # The minimum must be in (mid, right]
                left = mid + 1
            else:
                # Left side is sorted, or mid is the minimum
                # The minimum is in [left, mid]
                right = mid
        
        # When left == right, we found the minimum element
        return nums[left]


"""
Key Insights and Takeaways:

1. Problem Classification:
   - Modified binary search on rotated sorted array
   - Finding rotation point which contains the minimum element
   - Guaranteed to have exactly one minimum (no duplicates)

2. Core Technique - Rotation Point Binary Search:
   - Compare nums[mid] with nums[right] (not nums[left])
   - If nums[mid] > nums[right]: minimum on right side
   - If nums[mid] <= nums[right]: minimum on left side or at mid
   - Use position convergence approach

3. Template Choice:
   - Use while left < right for position convergence
   - Similar to LeetCode 162 (peak finding)
   - Guaranteed answer exists, so converge to position

4. Why This Works:
   - Rotated sorted array has at most one rotation point
   - Minimum element is always at the rotation point
   - Comparing with right endpoint gives monotonic decision

6. Common Mistakes to Avoid:
   - Don't compare nums[mid] with nums[left] (ambiguous cases)
   - Remember this assumes no duplicates (LeetCode 154 handles duplicates)
   - Use while left < right, not while left <= right
   - Use right = mid, not right = mid - 1 (preserve potential answer)

7. Related Problems:
   - LeetCode 154: Find Minimum in Rotated Sorted Array II (with duplicates)
   - LeetCode 33: Search in Rotated Sorted Array
   - LeetCode 81: Search in Rotated Sorted Array II
   - LeetCode 162: Find Peak Element (similar template)

8. Template Pattern:
   - Position convergence problems use while left < right
   - When answer is guaranteed to exist
   - When we want boundaries to meet at the answer
"""
