# solution 1: brute force

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

# solution 2: sort + two pointers

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
