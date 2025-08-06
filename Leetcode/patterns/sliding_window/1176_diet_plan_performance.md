## ☀️ Leetcode 1176. Diet Plan Performance

### Problem

You are given:

- `calories`: a list of integers where `calories[i]` is the number of calories on the i-th day
- `k`: the length of each performance period (number of days)
- `lower`: the lower bound of acceptable calories
- `upper`: the upper bound of acceptable calories

You need to calculate the overall performance score by evaluating each `k`-day period:

- If the total calories < lower, subtract 1 point
- If the total calories > upper, add 1 point
- Otherwise, 0 points

Return the total score after evaluating all such `k`-day periods.

---

### ☀️ UMPIRE

**U - Understand**

- Contiguous subarrays only
- Subarray size is always `k`
- Multiple scoring intervals

**M - Match**

- Data Structure: Array
- Pattern: Sliding Window (Fixed-size)

**P - Plan**

1. Calculate the sum of the first `k` elements
2. Check whether it's < lower, > upper, or in-between
3. Slide the window by removing one from the left and adding one on the right
4. Accumulate the score accordingly

**I - Implement**

### ☀️ Brute Force

```python
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        score = 0
        for i in range(len(calories) - k + 1):
            window_sum = sum(calories[i:i + k])  # O(k) operation
            if window_sum < lower:
                score -= 1
            elif window_sum > upper:
                score += 1
        return score
```

**Time Complexity:** O(n \* k)

**Space Complexity:** O(1)

---

### ☀️ Optimized Sliding Window

```python
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # Step 1: Compute initial sum
        window_sum = sum(calories[:k])
        score = 0

        # Step 2: Evaluate the first window
        if window_sum < lower:
            score -= 1
        elif window_sum > upper:
            score += 1

        # Step 3: Slide the window
        for i in range(k, len(calories)):
            window_sum += calories[i] - calories[i - k]  # Add new, remove old
            if window_sum < lower:
                score -= 1
            elif window_sum > upper:
                score += 1

        return score
```

**Time Complexity:** O(n)

**Space Complexity:** O(1)

---

### ☀️ Sliding Window Template (Fixed Size)

```python
window_sum = sum(arr[:k])
# evaluate first window
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]
    # evaluate
```

---

### ☀️ Tags

- Sliding Window
- Arrays
- Prefix Sum (minor)

---

### ☀️ Script

I’ll start by calculating the initial sum of the first `k` days.
I’ll check if this sum is below `lower`, above `upper`, or in-between.
Then I’ll slide the window one day at a time.
Update the sum by removing the leftmost day and adding the new rightmost day.
Adjust the score based on the new sum.

