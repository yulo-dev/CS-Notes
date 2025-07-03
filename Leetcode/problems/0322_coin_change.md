# Leetcode 0322 - Coin Change

## ☀️ UMPIRE  
- **Understand**: Given coins of different denominations and a total amount, return the minimum number of coins needed to make up that amount. Return -1 if it cannot be done.  
- **Match**: This is a classic DP problem. We need to explore all combinations of coin values that add up to the target.  
- **Plan**: Use either top-down recursion with memoization or bottom-up DP to find the fewest number of coins to reach each amount.  
- **Implement**: See below  
- **Review**: Ensure subproblem dependencies are handled correctly (dp[i - coin]), and edge cases like amount = 0 return 0.  
- **Evaluate**: Time O(amount × len(coins)), Space O(amount)


## ☀️ Metadata  
- **Appears In**: Grind75  
- **Pattern**: Dynamic Programming  
- **Data Structure**: Array, Dictionary  
- **Algorithm**: DP (Top-down & Bottom-up)  
- **Tags**: DP, Complete Knapsack, Recursion, Memoization

## ☀️ Solution 1: Top-down Recursion + Memoization

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(n):
            if n == 0:
                return 0
            if n < 0:
                return float('inf')
            if n in memo:
                return memo[n]

            min_coins = float('inf')
            for coin in coins:
                res = dp(n - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)

            memo[n] = min_coins
            return memo[n]

        result = dp(amount)
        return result if result != float('inf') else -1
```

## ☀️ Solution 2: Bottom-up Dynamic Programming

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
```

## ☀️ Trace Example (Bottom-up, coins = [1, 2, 5], amount = 6)

```
Initial: dp = [0, inf, inf, inf, inf, inf, inf]

coin = 1:
  dp[1] = 1
  dp[2] = 2
  dp[3] = 3
  dp[4] = 4
  dp[5] = 5
  dp[6] = 6

coin = 2:
  dp[2] = 1
  dp[3] = 2
  dp[4] = 2
  dp[5] = 3
  dp[6] = 3

coin = 5:
  dp[5] = 1
  dp[6] = 2

Final dp = [0, 1, 1, 2, 2, 1, 2]
→ dp[6] = 2
```

## ☀️ Line-by-line Typing Script (for Bottom-up version)

- I’m defining the `coinChange` function, which returns the minimum number of coins needed to make up the given amount.
- I initialize a `dp` array of length `amount + 1`, and set all values to infinity to represent “not reachable”.
- I set `dp[0] = 0`, because we need 0 coins to make up 0 amount.
- Then I loop through each coin in the coins list.
- For each coin, I iterate from `coin` to `amount`, because we can only use this coin to build amounts equal or greater than its value.
- For each `i`, I update `dp[i]` by comparing the current value with `dp[i - coin] + 1`, which represents using one more coin to build `i`.
- After finishing all updates, if `dp[amount]` is still infinity, that means we cannot form the target amount, so return -1.
- Otherwise, return `dp[amount]` as the final answer.
