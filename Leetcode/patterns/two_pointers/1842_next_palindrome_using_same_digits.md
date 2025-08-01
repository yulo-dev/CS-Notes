
# Leetcode 1842 - Next Palindrome Using Same Digits

---

## ☀️ UMPIRE

### Understand
**Q:** What is the problem asking?  
**A:** Given a numeric string `num` that is already a palindrome, find the smallest palindrome larger than `num` that can be formed by rearranging its digits. If no such palindrome exists, return an empty string `""`.

**Constraints:**
- `num` length can be very large (treat as string, not integer).
- Input is guaranteed to be a palindrome.
- Output must also be a palindrome and **larger** than input.
- If impossible, return `""`.

**Goal:** Return the lexicographically smallest palindrome greater than the original using the same digits.

---

### Match
- **Pattern:** Next Permutation (applied to half of the palindrome)
- **Data Structure:** String → List for modification
- **Algorithm:** Next Permutation + String Reconstruction
- **Tags:** String, Permutation, Palindrome

---

### Plan
1. Split the palindrome into:
   - `left` = first half of digits
   - `mid` = middle digit (if length is odd)
2. Apply **Next Permutation** algorithm on `left`:
   - Find the first decreasing index `i` from the right.
   - Find index `j` where `arr[j] > arr[i]`.
   - Swap `arr[i], arr[j]` and reverse suffix.
3. If no next permutation exists, return `""`.
4. Reconstruct palindrome:
   - `new_left + mid + reversed(new_left)`.
5. Return the result.

---

### Implement
```python
class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        half_len = n // 2

        # Take left half as list for easy modification
        left = list(num[:half_len])
        mid = '' if n % 2 == 0 else num[half_len]

        # Standard Next Permutation on left half
        def next_permutation(arr):
            # 1. Find first decreasing index from right
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            if i < 0:
                return False

            # 2. Find the element just larger than arr[i]
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1

            # 3. Swap and reverse suffix
            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = reversed(arr[i + 1:])
            return True

        # If no larger permutation exists
        if not next_permutation(left):
            return ""

        new_left = ''.join(left)
        return new_left + mid + new_left[::-1]
```

---

### Review
- **Index pitfalls:**  
  - `i = len(arr) - 2` because we compare arr[i] with arr[i+1].
  - `j = len(arr) - 1` to find the rightmost greater element.
- **In-place modification:** `next_permutation` modifies `left` directly.
- **Palindrome reconstruction:** Must reverse the updated left half and mirror it correctly.
- **Return condition:** If left half has no next permutation → return `""`.

---

### Evaluate
- **Time Complexity:** O(n) (next permutation + string building)
- **Space Complexity:** O(n) (string conversion and result building)

---

## ☀️ Approaches Comparison

### Approach 1: Brute Force (Generate All Permutations)
- Generate all permutations of the string digits.
- Filter palindromes.
- Sort and pick the next greater one.
- **Time Complexity:** O(n! * n)
- **Space Complexity:** O(n)
- **Notes:** Completely infeasible for even moderate n.

### Approach 2: Next Permutation on Half (Chosen)
- Only permute the left half of the palindrome.
- Reconstruct a new palindrome by mirroring.
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Notes:** Optimal and clean.

---

## ☀️ Complexity Comparison
| Approach                  | Time        | Space | Notes                           |
|---------------------------|-------------|-------|--------------------------------|
| Brute Force (all perms)   | O(n! * n)   | O(n)  | Generate and check palindromes |
| Next Permutation (chosen) | O(n)        | O(n)  | Optimal approach               |

---

## ☀️ Trace Simulation
### Example: `num = "1221"`
- left = ['1','2'], mid = ''  
- next_permutation → ['2','1']  
- new_left = "21"  
- result = "21" + "" + "12" = "2112"

---

## ☀️ Tags
- **Data Structure:** String
- **Algorithm:** Next Permutation, Palindrome Reconstruction
- **Pattern:** Next Permutation
- **Difficulty:** Medium
