# Leetcode 0053 - Maximum Subarray

## ☀️ UMPIRE
- **Understand**: Given an integer array `nums`, return the **largest sum** of any contiguous subarray.
- **Match**: Input is a 1D array of integers (may include negatives) → suitable for linear scan / dynamic programming
- **Plan**: Use Kadane’s Algorithm to track the maximum subarray sum ending at each index
- **Implement**: See below
- **Review**: Check transition logic: whether to extend previous sum or start a new subarray
- **Evaluate**: Time O(n), Space O(1) — linear scan using only two variables


## ☀️ Metadata
- **Appears In**: Grind75, NeetCode 150
- **Pattern**: Dynamic Programming (#3)
- **Data Structure**: Array
- **Algorithm**: Kadane’s Algorithm
- **Tags**: Dynamic Programming, Greedy, Subarray, Prefix Sum


## ☀️ Solution Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current and max sum with the first element
        current_sum = max_sum = nums[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Decide whether to start a new subarray or extend the existing one
            current_sum = max(nums[i], current_sum + nums[i])
            # Update global maximum sum if current is higher
            max_sum = max(max_sum, current_sum)

        return max_sum
```


## ☀️ Trace

```
Input: [-2,1,-3,4,-1,2,1,-5,4]

Step-by-step trace:
i=0 → current_sum = -2, max_sum = -2
i=1 → current_sum = max(1, -2+1) = 1 → max_sum = max(-2, 1) = 1
i=2 → current_sum = max(-3, 1-3) = -2 → max_sum = 1
i=3 → current_sum = max(4, -2+4) = 4 → max_sum = 4
i=4 → current_sum = max(-1, 4-1) = 3 → max_sum = 4
i=5 → current_sum = max(2, 3+2) = 5 → max_sum = 5
i=6 → current_sum = max(1, 5+1) = 6 → max_sum = 6
i=7 → current_sum = max(-5, 6-5) = 1 → max_sum = 6
i=8 → current_sum = max(4, 1+4) = 5 → max_sum = 6

Final Result: 6
```


## ☀️ Line-by-line Typing Script

- I’m defining the `maxSubArray` function which receives a list of integers.
- I initialize both `current_sum` and `max_sum` with the first element of the array.
- This is because we must include at least one number in the subarray.
- Then I iterate from index 1 to the end of the array.
- For each number, I compute the max of:
  - starting a new subarray at this number,
  - or extending the previous subarray with this number.
- I assign that result to `current_sum`.
- Then I update `max_sum` if the current sum is greater than what we had so far.
- Finally, I return the global max which holds the largest sum of any contiguous subarray.
