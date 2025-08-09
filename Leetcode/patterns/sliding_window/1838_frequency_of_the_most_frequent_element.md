# Leetcode 1838 — Frequency of the Most Frequent Element

## ☀️ Problem
Given an integer array `nums` and an integer `k`, in one operation you may choose any index and increment its value by 1. Return the **maximum possible frequency** of an element after performing at most `k` operations.

---

## ☀️ UMPIRE

### Understand
- **Input/Output:** Input: array `nums`, integer `k`. Output: the largest frequency of any value achievable after ≤ `k` increments.
- **Operation:** Each operation increases a single element by 1; no decrements allowed.
- **Constraints (typical):** `1 ≤ len(nums) ≤ 1e5`, `1 ≤ nums[i], k ≤ 1e5`.
- **Edge cases:** If `k = 0`, answer is the current max frequency. If all numbers can be made equal within `k`, the answer can be `len(nums)`.

### Match
- **Patterns:** Sorting + Sliding Window, “valid-window with cost” (same family as LC 424 / 1004).
- **Data structures:** Two pointers, running window sum.
- **Key invariant:** After sorting, for any window `[l..r]`, `nums[r]` is the maximum value inside the window.

### Plan
1. **Sort** the array so that the right end of any window is the current maximum.
2. Maintain a window `[l..r]` and its **running sum** `window_sum`.
3. For target `val = nums[r]`, the cost to raise every element in `[l..r]` up to `val` is  
   `cost = val * (r - l + 1) - window_sum`.
4. While `cost > k`, move `l` right (shrink) and subtract the leaving value from `window_sum`.
5. Track the best window length as the answer.

### Implement
See **Solution 2** (Sliding Window) below.

### Review
- **Why target = rightmost value?** Only `+1` operations are allowed. The cheapest way to equalize is to raise everything to the current maximum `nums[r]`; raising beyond `nums[r]` only increases cost.
- **Why must the optimal set be a contiguous block after sorting?** If a chosen set skips a closer element in favor of a farther one, swapping them never increases total cost. Repeating this argument yields a contiguous segment.

### Evaluate
- **Time:** `O(n log n)` for sorting + `O(n)` sliding → `O(n log n)` total.
- **Space:** `O(1)` extra (ignoring sorting’s internal buffers). Works for `n = 1e5`.

---

## ☀️ Why Sliding Window?
- **Brute force** enumerates all subarrays and recomputes sums → `O(n^3)` (or `O(n^2)` with prefix sums).
- After **sorting**, the optimal choice for any target is a **contiguous** segment ending at that target (right end).  
  This makes two pointers ideal: `r` only moves forward; `l` only moves forward to restore validity.  
- Maintaining a **running sum** turns the cost check into `O(1)` per step, giving linear pass after sorting.

---

## ☀️ Key Formula
For sorted `nums` and window `[l..r]` with `val = nums[r]`:
```
cost = val * (r - l + 1) - sum(nums[l..r])
```
Window is **valid** iff `cost ≤ k`.

---

## ☀️ Solution 1 — Brute Force (O(n^3))
Educational baseline; enumerates all windows and recomputes the sum each time.

```python
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        # 1) Sort so the right end is the window max.
        # 2) Enumerate every window [l..r].
        # 3) Compute sum(nums[l:r+1]) from scratch (O(n)).
        # 4) Cost to raise all to nums[r]: val*len - window_sum.
        # 5) If cost <= k, update answer.
        nums.sort()
        n = len(nums)
        best = 1

        for r in range(n):
            val = nums[r]
            for l in range(r + 1):
                length = r - l + 1
                window_sum = sum(nums[l:r+1])  # O(n) per window
                cost = val * length - window_sum
                if cost <= k:
                    best = max(best, length)
        return best
```

**Time:** `O(n^3)` • **Space:** `O(1)`

---

## ☀️ Solution 2 — Sort + Sliding Window (O(n log n))
Practical go-to: maintain a running window sum; shrink while the cost exceeds `k`.

```python
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        # After sorting, nums[r] is the max in the current window.
        # If raising all numbers in [l..r] to nums[r] costs more than k,
        # we shrink from the left until valid.
        nums.sort()
        l = 0
        window_sum = 0
        best = 1

        for r, val in enumerate(nums):
            window_sum += val
            # While invalid, move l right to reduce cost
            while val * (r - l + 1) - window_sum > k:
                window_sum -= nums[l]
                l += 1
            best = max(best, r - l + 1)
        return best
```

**Time:** `O(n log n)` (sort + linear pass) • **Space:** `O(1)` extra

---

## ☀️ Solution 3 — Sort + Prefix Sum + Binary Search (O(n log n))
Same formula, different technique: for each `r`, binary search the smallest feasible `l`.

```python
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        # Precompute prefix sums for O(1) range sums.
        nums.sort()
        n = len(nums)

        prefix = [0] * (n + 1)  # prefix[i] = sum of nums[0..i-1]
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def range_sum(l: int, r: int) -> int:
            return prefix[r + 1] - prefix[l]

        best = 1
        for r in range(n):
            val = nums[r]
            lo, hi = 0, r
            ans_l = r  # at worst, window of size 1
            while lo <= hi:
                mid = (lo + hi) // 2
                length = r - mid + 1
                cost = val * length - range_sum(mid, r)
                if cost <= k:
                    ans_l = mid
                    hi = mid - 1  # try extend further left
                else:
                    lo = mid + 1  # too expensive, move right
            best = max(best, r - ans_l + 1)
        return best
```

**Time:** `O(n log n)` • **Space:** `O(n)` (prefix array)

---

## ☀️ Complexity Comparison

| Solution | Method                           | Time           | Space  | Notes                              |
|---------:|----------------------------------|----------------|--------|------------------------------------|
| 1        | Brute Force                      | O(n^3)         | O(1)   | Pedagogical baseline               |
| 2        | Sort + Sliding Window            | O(n log n)     | O(1)   | Practical and concise              |
| 3        | Sort + Prefix + Binary Search    | O(n log n)     | O(n)   | Clear formula; educational variant |

---

## ☀️ Script 
I’ll **sort** the array so the window’s right end is always the **current maximum**.
Use a **sliding window** `[l..r]` and maintain its **running sum**.
The **cost** to raise all numbers in the window to `nums[r]` is `val * window_len - window_sum`.
While `cost > k`, I **shrink from the left** to restore validity.
I track the **maximum window length** as the answer and return it.
