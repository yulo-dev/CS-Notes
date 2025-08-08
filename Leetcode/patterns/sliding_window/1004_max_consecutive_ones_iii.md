# Leetcode 1004 — Max Consecutive Ones III

## Problem
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`s in the array if you can flip at most `k` `0`s.

## Algorithm (Sliding Window)
1. Maintain a window `[left, right]`.
2. Expand `right`; if a `0` enters, increment `zeros`.
3. While the window is invalid (`zeros > k`), move `left` rightward; if a `0` leaves, decrement `zeros`.
4. When valid, update the best length with `right - left + 1`.

**Time:** O(n) **Space:** O(1)

---

## Solution A — Zeros-count Sliding Window (Recommended)

```python
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        best = 0

        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
```
**Idea:** A window is valid iff it contains at most `k` zeros. We never actually flip; we just ensure such a flip **exists**.

---

## Solution B — 424-style Template (Generalized Form)

```python
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count = [0, 0]  # count[0], count[1] in current window
        max_count = 0   # highest frequency of a single value (treat 1s as target)
        best = 0

        for right, x in enumerate(nums):
            count[x] += 1
            max_count = max(max_count, count[x])

            # replacements_needed = window_len - max_count
            while (right - left + 1) - max_count > k:
                count[nums[left]] -= 1
                left += 1

            best = max(best, right - left + 1)
        return best
```
**Why have this version?** It matches the reusable template from LC424/LC340/LC159:  
`window_len - max_count <= k`

---

## (For comparison) Brute Force — O(n²)

```python
from typing import List

class Solution:
    def longestOnes_bruteforce(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = 0
        for start in range(n):
            zeros = 0
            for end in range(start, n):
                if nums[end] == 0:
                    zeros += 1
                if zeros <= k:
                    best = max(best, end - start + 1)
                else:
                    break
        return best
```
> True O(n³) would be re-counting zeros each time; keeping a running `zeros` makes it O(n²).

---

## Dry Run (Quick Trace)
Example: `nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2`  
- Expand `right` until zeros=3 → invalid → move `left` past the first `0` to make zeros=2.  
- Continue expanding; the best length becomes 6, then later 10.

---

## Pitfalls
- Use **`while zeros > k`**, not `if` — may need to shrink multiple steps.
- Always do `left += 1` when shrinking; decrement `zeros` only if the outgoing element is `0`.
- In the template version, you don’t recompute `max_count` when shrinking.

---

## Script
I’ll use a sliding window. The right pointer expands the window and I count how many zeros are inside. 
While zeros exceed k, I move the left pointer and decrement zeros if I drop a zero. 
Each element enters/exits at most once, so it’s O(n) time and O(1) space. 
Alternatively, I can frame it with the LC424 template: replacements needed equals `window_len - max_count`, 
which is equivalent to `zeros ≤ k` in a binary array."

---

## Complexity Summary
- Sliding Window (zeros): **Time O(n)**, **Space O(1)**
- Sliding Window (424 template): **Time O(n)**, **Space O(1)**
- Brute force (running zeros): **Time O(n²)**, **Space O(1)**
