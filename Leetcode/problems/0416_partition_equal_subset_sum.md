# Leetcode 0416 - Partition Equal Subset Sum

## ☀️ UMPIRE
- **Understand**: Given an array of positive integers, determine if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
- **Match**: This is a classic 0/1 Knapsack problem → suitable for dynamic programming
- **Plan**: 
    1. If total sum is odd → return False
    2. Target = total // 2
    3. Use dp[i] = True if a subset sum of i is possible
    4. Traverse nums and update dp from target → num (reverse)
- **Implement**: See below
- **Review**: Key logic lies in using dp[i] = dp[i] or dp[i - num] while iterating backward
- **Evaluate**: Time O(n × target), where target = sum(nums) // 2, Space O(target); optimized with 1D dp and reverse loop to avoid reuse

## ☀️ Metadata
- **Appears In**: Grind75
- **Pattern**: Dynamic Programming (#12)
- **Data Structure**: 1D Array (Boolean)
- **Algorithm**: 0/1 Knapsack, Bottom-up DP
- **Tags**: DP, Knapsack, Subset Sum, Partition, Optimization


## ☀️ Solution Code

```python
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
```

## ☀️ Trace

```
Input: nums = [1, 5, 11, 5], target = 11
Initial dp: [True, False, ..., False]  (length 12)

Processing num = 1:
  dp[1] = dp[1] or dp[0] → True

Processing num = 5:
  dp[6] = dp[6] or dp[1] → True
  dp[5] = dp[5] or dp[0] → True

Processing num = 11:
  dp[11] = dp[11] or dp[0] → True

Processing num = 5 (again):
  dp[10] = dp[10] or dp[5] → True

Final dp: [..., True, ..., dp[11]=True]
→ Can partition: True
```


## ☀️ Line-by-line Typing Script 

- I’m defining the `canPartition` function, which determines if the list can be split into two equal subsets.
- I compute the total sum of the array. If it’s odd, we return False immediately.
- I calculate the target subset sum by dividing the total sum by 2.
- I initialize a boolean dp array where dp[i] means "can I form sum i with some subset of nums".
- I set dp[0] = True since we can always make 0 with an empty subset.
- For each number in nums, I iterate backward from target down to num.
- This ensures we only use each number once (0/1 knapsack).
- For each i, I check if dp[i - num] is True, then dp[i] becomes True.
- Finally, I return dp[target], which tells us if target sum is achievable.
