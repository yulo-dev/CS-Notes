# LeetCode 35: Search Insert Position
# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# Solution 1: Linear Search 
# Time: O(n) → Need to scan through array in worst case
# Space: O(1) → Only using constant extra space
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Scan from left to right
        for i in range(len(nums)):
            # If we find target or a number larger than target
            if nums[i] >= target:
                return i
        
        # If target is larger than all elements, insert at end
        return len(nums)

# Solution 2: Binary Search 
# Time: O(log n) → We eliminate half of the search space in each iteration
# Space: O(1) → Only using constant extra space for pointers
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target is in the right half
                left = mid + 1
            else:
                # Target is in the left half
                right = mid - 1
        
        # When loop ends, left is the insertion position
        # This works because:
        # - If target > all elements, left will be len(nums)
        # - If target < all elements, left will be 0
        # - Otherwise, left points to the first element > target
        return left

# Note: Solution 1 is straightforward but inefficient for large arrays.
# Solution 2 leverages the sorted property with binary search for optimal performance.
# The key insight in Solution 2 is that when the loop terminates, 'left' naturally 
# points to the correct insertion position.
