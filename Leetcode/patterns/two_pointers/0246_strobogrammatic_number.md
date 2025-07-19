# Leetcode 0246 - Strobogrammatic Number

## ☀️ UMPIRE

- **Understand**:

  - Input: A string `num` containing digits.
  - Output: Return `True` if the number is **strobogrammatic** — looks the same when rotated 180 degrees.
  - Constraints:
    - Only digits 0–9.
    - Valid mirror pairs: `0 <-> 0`, `1 <-> 1`, `6 <-> 9`, `8 <-> 8`, `9 <-> 6`
    - Digits like 2, 3, 4, 5, and 7 are invalid for strobogrammatic.

- **Match**:

  - This is a two-pointer pattern.
  - Similar to palindrome checking, but using a rotation mapping.

- **Plan**:

  - Use a `mapping` dictionary to define valid strobogrammatic pairs.
  - Initialize `left = 0`, `right = len(num) - 1`.
  - While `left <= right`:
    - Check if `num[left]` and `num[right]` exist in mapping.
    - Confirm if `mapping[num[left]] == num[right]`
    - Move pointers inward.

- **Implement**: See Two Pointers solution below.

- **Review**:

  - Check the mapping exists for both ends.
  - Correctly compare rotation mapping.
  - Cover edge cases like single digits and empty string (though Leetcode guarantees valid input).

- **Evaluate**:

  - Time: O(n), where n is the length of `num`
  - Space: O(1), since only a fixed-size dictionary is used

---

## ☀️ Code (Two Pointers)

```python
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        left, right = 0, len(num) - 1

        while left <= right:
            # Check if both digits are valid
            if num[left] not in mapping or num[right] not in mapping:
                return False
            # Check for strobogrammatic match
            if mapping[num[left]] != num[right]:
                return False
            left += 1
            right -= 1

        return True
```

---

## ☀️ Code (Rebuild and Reverse Method)

```python
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated = ''
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        for digit in reversed(num):
            if digit not in mapping:
                return False
            rotated += mapping[digit]

        return rotated == num
```

---

## ☀️ Complexity Comparison

| Approach          | Time | Space | Notes                            |
| ----------------- | ---- | ----- | -------------------------------- |
| Two Pointers      | O(n) | O(1)  | Clean, in-place comparison       |
| Reverse & Rebuild | O(n) | O(n)  | Less optimal due to extra string |

Two Pointers approach is recommended: it's clear, efficient, and shows algorithmic thinking.
