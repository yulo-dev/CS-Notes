# solution 1: brute force
# time: O(n²) 
# space: O(1)

from typing import List

class Solution:
    def longestOnes_bruteforce(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = 0

        for start in range(n):
            zeros = 0
            for end in range(start, n):
                if nums[end] == 0:
                    zeros += 1
                if zeros <= k:
                    best = max(best, end - start + 1)
                else:
                    # Can't extend further from this start since zeros only increase
                    break

        return best




# solution 2: Zeros-count Sliding Window
# time: O(n) 
# space: O(1)

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Sliding window counting zeros.
        Window is valid iff the number of zeros inside it is <= k.
        Whenever invalid (zeros > k), shrink from the left until valid again.
        """
        left = 0           # left boundary of the current window
        zeros = 0          # number of zeros inside window [left, right]
        best = 0           # answer: max valid window length seen so far

        for right, x in enumerate(nums):     # expand the window by moving 'right'
            if x == 0:
                zeros += 1                   # new zero enters the window

            # If the window is invalid, shrink it from the left
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1               # a zero leaves the window
                left += 1                    # always move left to shrink

            # Now window [left, right] is valid -> update best length
            best = max(best, right - left + 1)

        return best




# solution 3: general method just like 424
# time: O(n) 
# space: O(1)

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Sliding window using the 424-style formula:
        replacements_needed = window_len - max_count <= k
        Here we treat '1' as the majority element we want to keep.
        """
        left = 0
        count = [0, 0]     # count[0] = zeros in window, count[1] = ones in window
        max_count = 0      # the highest frequency of a single value (here, of 1s)
        best = 0

        for right, x in enumerate(nums):
            count[x] += 1
            # Track the highest count of the target value (1s) in current window
            max_count = max(max_count, count[x])

            # replacements_needed = window_len - max_count
            # If we need to flip more than k, shrink from the left
            while (right - left + 1) - max_count > k:
                count[nums[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
