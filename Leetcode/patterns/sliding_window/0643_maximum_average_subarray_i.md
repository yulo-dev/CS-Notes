## ☀️ Leetcode 643. Maximum Average Subarray I

### Problem

Given an array consisting of `n` integers and an integer `k`, find the **maximum average value** of any **contiguous subarray** of length `k`.

Return the answer as a float.

---

### ☀️ UMPIRE

**U - Understand**

- Subarray must be **contiguous**
- Subarray length is exactly `k`
- Can elements be negative? → Yes
- Return type is **float**

**M - Match**

- Data structure: Array
- Pattern: Sliding Window (Fixed-size)

**P - Plan**

1. Use a sliding window of size `k` to track the sum
2. Initialize the sum of the first `k` elements
3. Slide the window: subtract the element leaving the window and add the one entering
4. Track the max average seen so far

**I - Implement**

### ☀️ Brute Force

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        n = len(nums)
        for i in range(n - k + 1):
            window_sum = sum(nums[i:i+k])  # O(k)
            avg = window_sum / k
            max_avg = max(max_avg, avg)
        return max_avg
```

**Time Complexity:** O(n \* k)

**Space Complexity:** O(1)

---

### ☀️ Optimized Sliding Window

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Step 1: Initialize window sum of first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Step 2: Slide the window forward one element at a time
        for i in range(k, len(nums)):
            # Add rightmost new element and remove leftmost old element
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
```

**Time Complexity:** O(n)\
**Space Complexity:** O(1)

---

### ☀️ Sliding Window Insights

- Instead of recalculating the sum for every subarray (brute force), you maintain a **rolling sum**
- `window_sum += nums[i] - nums[i - k]` means:
  - Add the new right element to the window
  - Remove the old left element
- Only one sum operation per element → keeps it **linear time**

---

### ☀️ Template: Fixed-size Sliding Window (Sum or Average)

```python
window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]
    max_sum = max(max_sum, window_sum)

return max_sum / k
```

---

### ☀️ Tags

- Sliding Window
- Arrays

---

### ☀️ Script

I’ll initialize the window sum with the first `k` elements. Then I’ll slide the window across the array, one element at a time.
For each new element, I’ll subtract the one leaving the window and add the one entering.
Track the maximum window sum and return its average.

---

### ☀️ Summary

- Use fixed-size sliding window to avoid repeated summation
- Simple rolling sum logic gives O(n) efficiency
