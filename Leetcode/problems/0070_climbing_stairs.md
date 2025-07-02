## ☀️ UMPIRE

- **Understand**: You are at the bottom of a staircase with `n` steps. Each time, you can climb 1 or 2 steps. How many distinct ways can you reach the top?
- **Match**: This is a classic Fibonacci-like problem → Suitable for bottom-up DP
- **Plan**: Use two rolling variables to simulate the Fibonacci sequence (dp[i] = dp[i-1] + dp[i-2])
- **Implement**: Initialize first=1, second=2; loop from step 3 to n, update both variables
- **Review**: Ensure base cases (n = 1, 2) are handled properly; check variable shift logic
- **Evaluate**: Time O(n) for single loop; Space O(1) using only constant vars


## ☀️ Metadata

- **Appears In**: Grind75, NeetCode 150
- **Pattern**: Dynamic Programming (#8)
- **Data Structure**: Integers only
- **Algorithm**: DP (bottom-up), Fibonacci recurrence
- **Tags**: Dynamic Programming, Math, Fibonacci


## ☀️ Solution Code

```python
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
```

## ☀️ Trace

```
n = 5

first = 1   # dp[1]
second = 2  # dp[2]

→ i=3: third = 1+2=3 → dp[3]=3
    first = 2, second = 3

→ i=4: third = 2+3=5 → dp[4]=5
    first = 3, second = 5

→ i=5: third = 3+5=8 → dp[5]=8
    first = 5, second = 8

Return second = 8
```

## ☀️ Line-by-line Typing Script

- I’m defining a function that returns the number of ways to climb `n` stairs.
- First, I handle the base cases. If `n` is 1 or 2, we simply return `n` since the number of ways equals the step count.
- Then I initialize two variables: `first` for dp[1], and `second` for dp[2].
- These represent the number of ways to reach the 1st and 2nd steps.
- Now I enter a for loop starting from step 3 up to `n`.
- For each step `i`, I calculate `third` as the sum of the previous two values — this is the number of ways to reach step `i`.
- Then I slide the window forward: `first` becomes the old `second`, and `second` becomes the new `third`.
- After the loop finishes, `second` holds the number of ways to reach step `n`, so I return it as the final result.
