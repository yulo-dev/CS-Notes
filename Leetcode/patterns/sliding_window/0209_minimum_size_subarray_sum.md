## ☀️ Leetcode 209. Minimum Size Subarray Sum

### Problem

Given an array of positive integers `nums` and an integer `target`, return the minimal length of a contiguous subarray of which the sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

---

### ☀️ UMPIRE

**U - Understand**
- Find the **minimum** length of a subarray whose total sum is **≥ target**
- Only **positive integers**
- Return `0` if no valid subarray exists

**M - Match**
- Data Structure: Array
- Algorithm: Sliding Window (Variable-size), Two Pointers

**P - Plan**
1. Use two pointers `left` and `right` to define the window
2. Add `nums[right]` to a running `total`
3. While `total >= target`, update `min_len` and try shrinking the window from the left
4. Return `min_len` if valid, else 0

**I - Implement**

### ☀️ Brute Force
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total >= target:
                    min_len = min(min_len, j - i + 1)
                    break  # early stop for minimal length

        return min_len if min_len != float('inf') else 0
```
**Time Complexity:** O(n^2)  
**Space Complexity:** O(1)

---

### ☀️ Optimized Sliding Window
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
```
**Time Complexity:** O(n) — Each element is added and removed from the window at most once

**Space Complexity:** O(1)

---

### ☀️ Sliding Window Template (Variable Size)
```python
for right in range(len(nums)):
    total += nums[right]
    while total >= target:
        # update result
        total -= nums[left]
        left += 1
```

---

### ☀️ Tags
- Sliding Window
- Two Pointers
- Arrays

---

### ☀️ Script
I start with two pointers: left and right. As I expand the window by moving right, I add each element to total.
When total is greater than or equal to the target, I try to shrink the window from the left to find the smallest valid window.
Each time total meets the target, I check the length and update the minimum length seen so far.
