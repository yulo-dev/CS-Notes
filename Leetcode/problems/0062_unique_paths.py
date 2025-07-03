# method 1 (time complexity: O(mn); time complexity: O(mn))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D dp grid with all values set to 1
        # dp[i][j] represents the number of unique paths to reach cell (i, j)
        # First row and first column are all 1s because there's only one way to reach them
        dp = [[1] * n for _ in range(m)]

        # Start filling the dp table from cell (1,1) since first row and column are base cases
        for r in range(1, m):
            for c in range(1, n):
                # Number of ways to reach (r, c) is the sum of:
                # - ways to reach the cell above (r-1, c)
                # - ways to reach the cell to the left (r, c-1)
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        # Return the number of unique paths to reach the bottom-right corner
        return dp[m - 1][n - 1]


# method 2 (time complexity: O(mn); time complexity: O(n))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 1D DP array with all values set to 1
        # dp[j] represents the number of unique paths to column j in the current row
        dp = [1] * n

        # Start from row 1, since row 0 (dp) is already initialized as base case
        for i in range(1, m):
            for j in range(1, n):
                # Update dp[j] by adding the value from the left (dp[j - 1])
                # dp[j] already holds the value from the row above (previous dp[j])
                dp[j] = dp[j] + dp[j - 1]

        # The last element holds the number of unique paths to the bottom-right corner
        return dp[-1]


# method 3 (time complexity: O(1); time complexity: O(1))
from math import comb

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # To reach the bottom-right corner, we must take (m - 1) down moves and (n - 1) right moves
        # In total, we take (m + n - 2) steps
        # The number of unique paths equals the number of ways to choose (n - 1) right moves
        # from (m + n - 2) total steps → which is C(m + n - 2, n - 1)
        return comb(m + n - 2, n - 1)
