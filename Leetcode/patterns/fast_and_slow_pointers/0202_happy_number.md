# 202. Happy Number

**Difficulty:** Easy  
**Tags:** Math, Hash Table, HashSet, Two Pointers, Cycle Detection

---

## Problem
A **happy number** is defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
- Return `true` if `n` is a happy number, and `false` if not.

**Example 1**  
```
Input: n = 19
Output: true
Explanation:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1
```

**Example 2**  
```
Input: n = 2
Output: false
```

---

## Approach 1: HashSet (Detect Cycle by Memory)

### Idea
- Use a HashSet to store numbers we have already seen.
- If we see a number again, it means we are in a cycle (return False).
- If we reach 1, the number is happy (return True).

### Code
```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(num):
            total = 0
            while num > 0:
                num, digit = divmod(num, 10)  # extract last digit
                total += digit * digit        # add square of digit
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)          # record current number
            n = get_sum(n)       # move to next number

        return n == 1
```

### Complexity
- **Time:** O(log n) (numbers quickly reduce to <243 states)
Time Complexity:
Each iteration computes the sum of squares of digits, which takes O(log n) time because the number of digits is proportional to log n.
However, numbers quickly shrink to a fixed range (< 243 for 32‑bit integers), so the total number of iterations is constant.
Effectively, for this problem the runtime is O(1).

- **Space:** O(log n) for storing seen numbers

---

## Approach 2: Fast & Slow Pointers (Floyd's Cycle Detection)

### Idea
- Use two pointers (like linked list cycle detection):
  - Slow pointer moves one step at a time.
  - Fast pointer moves two steps at a time.
- If there is a cycle (not including 1), they will eventually meet.
- If `fast` reaches 1, then n is happy.

### Code
```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(num):
            total = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total += digit * digit
            return total

        slow = n
        fast = get_sum(n)

        while fast != 1 and slow != fast:
            slow = get_sum(slow)
            fast = get_sum(get_sum(fast))

        return fast == 1
```

### Complexity
- **Time:** O(log n)
Time Complexity:
Each iteration computes the sum of squares of digits, which takes O(log n) time because the number of digits is proportional to log n.
However, numbers quickly shrink to a fixed range (< 243 for 32‑bit integers), so the total number of iterations is constant.
Effectively, for this problem the runtime is O(1).

- **Space:** O(1)

---

## Why Fast & Slow Works
- The sequence of numbers either:
  1. Reaches 1 (fixed point) → happy number
  2. Falls into a cycle not including 1 → not happy
- Using two pointers with different speeds guarantees:
  - If there is a cycle, `fast` will eventually meet `slow`.
  - If no cycle (i.e., we reach 1), then `fast == 1` and the loop stops.

---

## Common Mistakes
1. Using `for i in range(num)` in `get_sum()`:
   - This runs `num` times, not `digit-count` times. Should use `while num > 0`.
2. Updating pointers incorrectly:
   - Must update based on current `slow` and `fast`, not always from initial `n`.

---

## Script (Fast & Slow Pointer version)
We need to check if repeatedly replacing a number with the sum of the squares of its digits will eventually reach 1, or fall into a cycle.  
First, we define a helper function `get_sum()` that computes the sum of the squares of all digits of a given number. It uses `divmod(num, 10)` to extract the last digit and sum up its square.  
We then initialize two pointers: `slow`, starting at n and moving one step at a time, and `fast`, starting at `get_sum(n)` and moving two steps at a time.  
In the loop, as long as `fast` is not 1 and `slow` is not equal to `fast`, we keep updating them. This uses the same principle as detecting a cycle in a linked list: if there is a cycle, eventually the two pointers meet; if there is no cycle, the fast pointer reaches 1.  
Finally, if `fast == 1`, it means the number is happy and we return True; otherwise, it is stuck in a cycle, and we return False.
