# Method 1: Recursive + Memo 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}  # Dictionary to store the minimum coins needed for each amount

        def dp(n):
            # Base case: If the amount is 0, no coins are needed
            if n == 0:
                return 0
            
            # If the amount is negative, this path is invalid
            if n < 0:
                return float('inf')
            
            # If we already computed dp(n), return the cached result
            if n in memo:
                return memo[n]
            
            # Initialize the minimum coins needed to infinity
            min_coins = float('inf')

            # Try every coin and see which leads to the minimum coins
            for coin in coins:
                res = dp(n - coin)  # Ask: how many coins to make up (n - coin)?
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)  # Add this coin (+1)
            
            # Save the result in the memo dictionary before returning
            memo[n] = min_coins
            return memo[n]

        result = dp(amount)

        # If result is infinite, it means we cannot form the amount
        return result if result != float('inf') else -1
      
# Method 2: Bottom-up Dynamic Programming (recommend)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the dp array. dp[i] = min coins needed for amount i.
        dp = [float('inf')] * (amount + 1)

        # Base case: zero coins needed to make amount 0
        dp[0] = 0

        # For each coin, update the dp table from coin value up to amount
        for coin in coins:
            for i in range(coin, amount + 1):
                # If we can make i - coin, then try using this coin
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still inf, it means amount cannot be formed
        return dp[amount] if dp[amount] != float('inf') else -1
