
# Leetcode 680 - Valid Palindrome II

---

## ☀️ UMPIRE

### Understand
**Q:** Given a string `s`, you are allowed to delete at most one character. Determine if it can become a palindrome.  
**Constraints:**
- 1 <= s.length <= 10^5
- Consists of only lowercase English letters.

**Goal:** Return True if after deleting at most one character `s` can become a palindrome, otherwise return False.

---

### Match
- **Pattern:** Two Pointers
- **Data Structure:** String (immutable input, optional list conversion if needed)
- **Algorithm:** Greedy two-pointer approach with one allowed skip.
- **Tags:** String, Two Pointers, Palindrome

---

### Plan
1. Use two pointers: one from the left (`left`), one from the right (`right`).
2. While `left < right`:
   - If `s[left] == s[right]`, move both pointers inward.
   - If they mismatch:
     - Try skipping the left character (`s[left+1:right+1]`).
     - Try skipping the right character (`s[left:right]`).
     - If either substring is a palindrome, return True.
3. If the loop finishes without issues, return True.

---

### Implement
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper function to check if a substring is a palindrome
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        # Two pointers from both ends of the string
        left, right = 0, len(s) - 1

        # Check characters from outside to inside
        while left < right:
            if s[left] != s[right]:
                # If mismatch occurs, try skipping either left or right character
                skip_left = s[left + 1:right + 1]   # skip left character
                skip_right = s[left:right]          # skip right character
                # If either skipping left or skipping right leads to a palindrome, return True
                return is_palindrome(skip_left) or is_palindrome(skip_right)
            # Move pointers inward if characters match
            left += 1
            right -= 1

        # If no mismatch found or fixed by one deletion, it is a palindrome
        return True
```

---

### Review
- **Key Idea:** Allow one mismatch to be skipped, then check if the remaining string is palindrome.
- **Skip logic:** Use slicing to create substrings with one character removed.
- **Edge cases:** Strings that are already palindromes, single-character strings, or need one deletion at ends.

---

### Evaluate
- **Time Complexity:** O(n) → One full scan + at most one extra palindrome check of size n-1.
- **Space Complexity:** O(n) → Due to Python slicing (creates copies). Can be optimized to O(1) by pointer-based palindrome check without slicing.

---

## ☀️ Metadata
- **Difficulty:** Easy/Medium (depends on perspective)
- **Data Structure:** String
- **Algorithm:** Two Pointers, Conditional Skip
- **Tags:** String, Two Pointers, Palindrome

---

## ☀️ Complexity Comparison
| Approach              | Time   | Space | Notes                           |
|-----------------------|--------|-------|--------------------------------|
| Brute Force (delete each char) | O(n²) | O(n) | Check each deletion case separately |
| Two Pointer Skip (chosen)     | O(n)  | O(n) | Uses slicing to skip one char |
| Two Pointer Skip (optimized)  | O(n)  | O(1) | Uses indices, no slicing      |

---

## ☀️ Trace Example
### Input: `"abca"`
1. left=0, right=3 → `s[left]=='a'`, `s[right]=='a'` → move inward.
2. left=1, right=2 → `s[left]=='b'`, `s[right]=='c'` → mismatch.
3. Check skip left → `"aca"` → palindrome → return True.

---

## ☀️ Tags
- **Data Structure:** String
- **Algorithm:** Two Pointers
- **Pattern:** Conditional Skip
- **Difficulty:** Easy/Medium
