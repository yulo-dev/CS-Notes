class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Step 1: Calculate the total sum of all elements
        total = sum(nums)

        # If the sum is odd, it can't be split into two equal subsets
        if total % 2 == 1:
            return False

        # Step 2: Define the target sum we need to find (half of total)
        target = total // 2

        # Step 3: Initialize DP array
        # dp[i] will be True if a subset with sum i is achievable
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: zero sum is always achievable (empty subset)

        # Step 4: 0/1 Knapsack DP loop
        for num in nums:
            # Traverse dp array backwards to ensure each num is used only once
            for i in range(target, num - 1, -1):
                # If we can make i - num, then we can also make i by adding num
                dp[i] = dp[i] or dp[i - num]

        # Step 5: Final result
        return dp[target]  # True if target sum is achievable
