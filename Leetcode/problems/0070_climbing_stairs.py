# method 1: space complexity O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
            # Handle base cases directly
            # If there are 1 or 2 steps, the number of ways is equal to n
            if n <= 2:
                return n

            # Initialize the number of ways to reach step 1 and step 2
            first = 1      # dp[1]: 1 way to climb 1 step
            second = 2     # dp[2]: 2 ways to climb 2 steps (1+1, 2)

            # Use a bottom-up dynamic programming approach from step 3 to n
            for i in range(3, n + 1):
                third = first + second  # Total ways to reach step i
                first = second          # Slide the window: first becomes previous second
                second = third          # second becomes current result

            # After the loop, 'second' holds the total ways to reach step n
            return second


# method 2: top-down + memo: space complexity O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(i):
            if i <= 2:
                return i
            if i in memo:
                return memo[i]
            memo[i] = dfs(i - 1) + dfs(i - 2)
            return memo[i]

        return dfs(n)

# method 3: bottom-up + array: space complexity O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
