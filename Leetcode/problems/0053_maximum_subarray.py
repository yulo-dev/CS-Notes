class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize both current sum and max sum to the first element
        current_sum = max_sum = nums[0]

        # Iterate through the array starting from index 1
        for i in range(1, len(nums)):
            # Decide whether to extend the previous subarray or start a new one
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update the global maximum if needed
            max_sum = max(max_sum, current_sum)

        # Return the largest sum of any contiguous subarray
        return max_sum
