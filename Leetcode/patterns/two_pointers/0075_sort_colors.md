# Leetcode 0075 - Sort Colors

## ☀️ UMPIRE

- **Understand**: Given an array `nums` with values only 0, 1, and 2, sort them in-place so that all 0s come first, followed by 1s, then 2s.

- **Match**: This is a classic **Dutch National Flag** problem. Since we’re sorting three fixed values, we can use **Two (or Three) Pointers** to solve it efficiently.

- **Plan**:

  - Use three pointers: `low`, `mid`, and `high`.
  - `low` marks the boundary for 0s, `mid` traverses the array, and `high` marks the boundary for 2s.
  - Iterate through the list with `mid`:
    - If `nums[mid] == 0`, swap with `nums[low]`, increment both `mid` and `low`.
    - If `nums[mid] == 1`, just move `mid`.
    - If `nums[mid] == 2`, swap with `nums[high]`, decrement `high` only (don’t move `mid` yet).

- **Implement**: See code section below

- **Review**:

  - Why `mid <= high`? Because even when you swap a `2`, you must recheck the swapped-in value.
  - Ensure all swaps are in-place and pointers are correctly managed.

- **Evaluate**:

  - Time: O(n) — Each element is looked at most once.
  - Space: O(1) — No extra space, in-place sorting.

---

## ☀️ Code with English Comments

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Initialize pointers
        low = 0       # Next position for 0
        mid = 0       # Current index being checked
        high = len(nums) - 1  # Next position for 2

        # Process elements until mid passes high
        while mid <= high:
            if nums[mid] == 0:
                # Swap current element with the front (low)
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                # 1 is in correct position, just move mid
                mid += 1

            else:  # nums[mid] == 2
                # Swap with the back (high) but don’t move mid yet
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

---

## ☀️ Coding Walkthrough Script 

- We use three pointers to divide the array into sections for 0s, 1s, and 2s.
- The `mid` pointer scans the array, while `low` and `high` define the boundaries.
- When we see a 0, we swap it with `low`, when we see a 2, we swap it with `high`.
- 1s are left in place since they belong in the middle.

---

## ☀️ Complexity Comparison

| Method            | Time Complexity | Space Complexity | Notes                                       |
| ----------------- | --------------- | ---------------- | ------------------------------------------- |
| Brute Force       | O(n)            | O(1)             | Count 0s, 1s, 2s, then overwrite array      |
| 3-Pointer Optimal | O(n)            | O(1)             | One-pass, in-place Dutch National Flag sort |

The 3-pointer method is better because it finishes sorting in a single pass, uses no extra space, and avoids rewriting the array, making it ideal for in-place problems.

---

## ☀️ Why It's Called Dutch National Flag

The term comes from the Dutch flag's three colors (red, white, blue), and the goal is to partition the array into three regions just like the flag.

---

## ☀️ Tip

Since we only have three possible values, we can treat it like a partitioning problem and place each value in its region using in-place swaps and two moving boundaries.

---

## ☀️ Edge Cases

According to the problem statement:

- Input will only contain 0s, 1s, and 2s → no need to handle other values.
- Although the constraint guarantees at least one element, it's still good practice to ask whether empty input like [] should be handled.
- “Are inputs guaranteed to only include 0, 1, and 2? Should I consider invalid inputs or just focus on sorting the valid ones?”
- Valid edge cases to discuss:
  - `[]` → Should handle without error. 
  - `[0]`, `[1]`, `[2]` → One-element lists.
  - `[2, 0, 1]` → Smallest complete unsorted example.
