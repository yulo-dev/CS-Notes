# solution 1: brute force
# Try all subarrays starting at start and ending at end.
# Sum them one by one and check if they reach or exceed target.
# Stop expanding when valid to minimize unnecessary work.
# Time Complexity: O(n^2)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')

        # Try every possible subarray
        for start in range(n):
            total = 0
            for end in range(start, n):
                total += nums[end]

                # Check if this subarray meets the requirement
                if total >= target:
                    min_len = min(min_len, end - start + 1)
                    break  # no need to expand further
        return 0 if min_len == float('inf') else min_len



# solution 2: Optimized Sliding Window
# Keep a running total of the current window.
# Expand to the right, and whenever the total ≥ target, try to shrink from the left to find the smallest valid window.
# Track and update the min_len.
# Time Complexity: O(n)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        total = 0
        min_len = float('inf')

        # Expand window to the right
        for right in range(n):
            total += nums[right]

            # Shrink from the left while the total is valid
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
