## ☀️ Leetcode 219. Contains Duplicate II

### Problem

Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` in the array such that:

- `nums[i] == nums[j]`, and
- `abs(i - j) <= k`

---

### ☀️ UMPIRE

**U - Understand**

- What does "nearby" mean? → Distance between indices `i` and `j` is at most `k`
- Can elements repeat more than once? → Yes
- Are `i` and `j` allowed to be equal? → No, must be distinct
- Edge case: empty array or `k = 0`? → Return `False`

**M - Match**

- Data structure: Array, Set
- Pattern: Sliding Window, Hashing

**P - Plan**

- Use a `HashSet` to store the current window of size `k`
- Traverse array with index `right`
  - If `nums[right] in seen`: return `True`
  - Add `nums[right]` to `seen`
  - If window size > `k`, remove `nums[left]` and increment `left`
- If no duplicate found: return `False`

**I - Implement**

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        left = 0
        for right in range(len(nums)):
            if nums[right] in seen:
                return True

            seen.add(nums[right])

            if right - left >= k:
                seen.remove(nums[left])
                left += 1

        return False
```

**R - Review**

- The key part is `right - left >= k`, which ensures we keep a window of at most size `k`
- Window is [right - k, right - 1] (exclusive of current `right`)
- Use HashSet for O(1) lookups

**E - Evaluate**

- Time: O(n), each element added/removed once
- Space: O(k), max size of HashSet

---

### ☀️ Brute Force Version

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, min(i + k + 1, n)):
                if nums[i] == nums[j]:
                    return True
        return False
```

**Time:** O(n \* k) in worst case\
**Space:** O(1)

---

### ☀️ Sliding Window Insight

- You can dynamically maintain a set of the last `k` seen elements
- At each index `right`, you're checking if `nums[right]` was seen in the last `k` steps
- Shrink the window when it exceeds size `k`

---

### ☀️ Template: Sliding Window with Set

```python
seen = set()
left = 0
for right in range(len(nums)):
    # check duplicate
    if nums[right] in seen:
        return True
    # add to window
    seen.add(nums[right])
    # shrink if needed
    if right - left >= k:
        seen.remove(nums[left])
        left += 1
return False
```

---

### ☀️ Tags

- Sliding Window
- Hashing
- Two Pointers (implicit)

---

### ☀️ Script

I’ll use a set to track the last `k` elements in a sliding window.
For each index `right`, I’ll check if it’s already in the set. If so, return True.
Otherwise, I’ll add it to the set.
If the size of the window exceeds `k`, remove the element at the left.
Increment left accordingly.
If no duplicates are found within the allowed distance, return False.

---

### ☀️ Summary

- Use `set` for O(1) lookups
- Maintain window size of `k`
- Efficient and clean solution for nearby duplicate detection

