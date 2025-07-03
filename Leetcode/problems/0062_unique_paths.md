# Leetcode 0062 - Unique Paths

## ☀️ UMPIRE
- **Understand**: Given an `m x n` grid, return the number of unique paths from the top-left to the bottom-right. You can only move right or down.
- **Match**: This is a classic grid DP problem. Movement is restricted to right/down only, with no obstacles.
- **Plan**: There are three valid approaches:
  1. 2D bottom-up DP
  2. 1D space-optimized DP
  3. Combinatorics (Math)
- **Implement**: See all 3 methods below
- **Review**: Compare 2D vs 1D vs math in terms of logic, space, and interview usage
- **Evaluate**:
  - Time:
    - DP: O(m * n)
    - Math: O(min(m, n)) in theory, often treated as O(1) due to Python’s optimized comb()
  - Space:
    - 2D DP: O(m * n)
    - 1D DP: O(n)
    - Math: O(1)


## ☀️ Metadata
- **Appears In**: Grind75
- **Pattern**: Dynamic Programming (#8)
- **Data Structure**: Array (1D or 2D)
- **Algorithm**: Grid DP / Combinatorics
- **Tags**: DP, Math, Combinatorics, Grid


## ☀️ Solution Code

### ✅ Method 1: 2D DP
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D grid filled with 1s
        dp = [[1] * n for _ in range(m)]

        # Start from cell (1,1) since row 0 and col 0 are base cases
        for r in range(1, m):
            for c in range(1, n):
                # Total paths = from above + from left
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m - 1][n - 1]
```

### ✅ Method 2: 1D Space-Optimized DP
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize 1D array for current row
        dp = [1] * n

        # Update the dp array row by row
        for i in range(1, m):
            for j in range(1, n):
                # dp[j] = dp[j] (from top) + dp[j - 1] (from left)
                dp[j] = dp[j] + dp[j - 1]

        return dp[-1]
```

### ✅ Method 3: Math / Combinatorics
```python
from math import comb

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Total steps = (m - 1) downs + (n - 1) rights
        # Choose (n - 1) rights from total steps
        return comb(m + n - 2, n - 1)
```

## ☀️ Trace

For m = 3, n = 3:
```
Step-by-step DP table:
[1, 1, 1]
[1, 2, 3]
[1, 3, 6] → return 6

1D DP iteration:
Initial: [1, 1, 1]
i = 1 → [1, 2, 3]
i = 2 → [1, 3, 6]
```

### ☀️ Typing Script - Method 1 (2D DP)
- I initialize the DP table with all 1s since the first row and column have only one way to reach.
- I iterate through each cell starting from (1,1).
- For each cell, I add the number of paths from the cell above and the cell to the left.
- This reflects the idea that I can only move down or right.

### ☀️ Typing Script - Method 2 (1D DP)
- I use a 1D array to simulate the current row.
- For each cell from left to right, I update its value using the previous value in the array.
- This way, I reuse space and only keep one row in memory.

### ☀️ Typing Script - Method 3 (Combinatorics)
- I realize the total path is a fixed sequence of (m - 1) down moves and (n - 1) right moves.
- So I calculate the number of combinations to arrange these moves using C(m + n - 2, n - 1).
- I return the result using Python's math.comb function.


