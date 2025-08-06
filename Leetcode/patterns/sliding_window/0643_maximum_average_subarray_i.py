# solution 1: brute force
# For each possible subarray of length k, compute its sum and average.
# Update max_avg if the current one is better.
# Time Complexity: O(n * k) because slicing and summing is O(k) per iteration.
# space: O(1)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        
        # Try every subarray of length k
        for i in range(len(nums) - k + 1):
            current_sum = sum(nums[i:i + k])  # Sum the window manually
            current_avg = current_sum / k
            max_avg = max(max_avg, current_avg)
        
        return max_avg



# solution 2: Optimized Sliding Window version 
# Only one full sum is calculated (the first window).
# After that, we only adjust the sum by adding the new rightmost element and subtracting the old leftmost one.
# Time Complexity: O(n) 
# space: O(1)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize the sum of the first window of size k
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window from index k to the end of the array
        for i in range(k, len(nums)):
            # Add the new element and remove the leftmost element of the previous window
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        # Compute the max average from the max sum
        return max_sum / k
