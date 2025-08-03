# Leetcode 287. Find the Duplicate Number
Tags: Array, Two Pointers, Binary Search, Cycle Detection

---

## ☀️ UMPIRE

### U — Understand
**Problem**:  
Given an array `nums` containing `n + 1` integers where each integer is in `[1, n]`.  
There is only one repeated number, but it can be repeated multiple times.  
Return the duplicate number **without modifying the array** and using only **O(1) extra space**.

**Constraints**:
- `len(nums) = n + 1`, numbers in `[1, n]`.
- Exactly one duplicate, but may appear more than twice.
- Cannot modify the input array.

**Clarifying Questions**:
- Is there always exactly one duplicate? → Yes.
- Can duplicate appear more than twice? → Yes, still return that duplicate value.
- Can we use extra data structures? → No, must be O(1) space.

---

### M — Match
**Patterns**:
1. **Brute force check pairs** → O(n²)
2. **HashSet** → O(n) time, O(n) space
3. **Sorting** → O(n log n), modifies input (not allowed)
4. **Cycle detection (Floyd’s Tortoise & Hare)** → O(n) time, O(1) space (optimal)

**Why Cycle Detection?**
- Because values are in `[1, n]` and array length is `n+1`,  
  we can treat each index as a node and `nums[i]` as a pointer to next node:
  ```
  i -> nums[i]
  ```
- Duplicate numbers create a **cycle** in this "pointer graph".
- The duplicate number is exactly the **entry point of the cycle**.

---

### P — Plan

#### Approach 1: Hash Set (Basic)
1. Initialize empty set.
2. Iterate through `nums`:
   - If `num` already in set → return it.
   - Else add to set.

#### Approach 2: Sorting (If modifying allowed)
1. Sort `nums`.
2. Scan for consecutive duplicate elements.

#### Approach 3: Floyd’s Cycle Detection (Optimal)
1. Phase 1: Use two pointers:
   - slow = nums[slow]
   - fast = nums[nums[fast]]
   - Stop when slow == fast (guaranteed inside cycle).
2. Phase 2: Reset one pointer to index 0:
   - Move both pointers one step each.
   - Next meeting point = cycle entrance = duplicate number.

---

### I — Implement

#### Approach 1: Hash Set
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
```

#### Approach 2: Sorting
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()  # Not allowed in problem but good to mention
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
```

#### Approach 3: Floyd’s Cycle Detection (Optimal)
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: detect intersection
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]            # move one step
            fast = nums[nums[fast]]      # move two steps
            if slow == fast:
                break

        # Phase 2: find cycle entrance
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
```

---

### R — Review

#### Time Complexity
- HashSet → O(n)
- Sorting → O(n log n)
- Floyd → O(n)

#### Space Complexity
- HashSet → O(n)
- Sorting → O(1) extra but modifies input
- Floyd → O(1)

**Why Floyd is optimal?**
- Satisfies problem constraints (no extra space, no array modification).
- Runs in linear time.

---

### E — Evaluate
- **Correctness**: Works for arrays with multiple duplicates but only one unique duplicate value.
- **Why two phases?**:
  - Phase 1 ensures pointers are inside the cycle.
  - Phase 2 finds the cycle entry, which equals the duplicate number.
- **Common mistakes**:
  - Mixing index and value concepts.
  - Forgetting to reset one pointer in phase 2.
  - Assuming first meeting is directly the answer.
