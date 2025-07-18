
# Leetcode 0125 - Valid Palindrome

## ☀️ UMPIRE

- **Understand**:  
  Check if the given string is a valid palindrome, considering **only alphanumeric characters** and **ignoring cases**.

- **Match**:  
  This is a classic **Two Pointers** problem because we need to compare characters from both ends moving toward the center, skipping invalid ones.

- **Plan**:  
  - Use two pointers `left` and `right`
  - Move them toward each other
  - Skip any character that is not alphanumeric using `isalnum()`
  - Compare lowercase characters only
  - If all matching pairs are valid, return `True`

- **Implement**:  
  See code below

- **Review**:  
  - Be careful with pointer bounds (e.g., `left < right`)
  - Use `isalnum()` to filter out non-alphanumeric chars
  - Convert both sides to lowercase before comparing

- **Evaluate**:  
  - Brute force: O(N) time + O(N) space  
  - Two Pointers: O(N) time, **O(1) space**

---

## ☀️ Why This Is a Two Pointers Problem

We use two pointers starting from the beginning and end of the string:
- `left` moves forward
- `right` moves backward  
At each step, we compare the characters they point to — after skipping non-alphanumeric characters.

This approach is:
- More efficient than checking all substrings
- Avoids extra space used in filtering or reversing the string
- Ideal when checking **symmetric structure** like palindromes

---

## ☀️ Edge Case Notes

| Input       | Description                                            | Expected |
|-------------|--------------------------------------------------------|----------|
| `"A"`       | Single uppercase letter                                | `True`   |
| `"@#$%%"`   | Only special characters → filters to empty string      | `True`   |
| `""`        | Empty string → no mismatch possible                    | `True`   |
| `"abccbaa"` | Asymmetric string (visually similar but not mirrored) | `False`  |

These are useful for testing whether:
- Your pointer skips are working (`isalnum()`)
- Your lowercasing is working
- You handle trivial or empty input

---

## ☀️ Code (with comments)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the beginning and end of the string
        left = 0
        right = len(s) - 1

        # Traverse toward the center
        while left < right:
            # Move the left pointer forward if it's pointing to a non-alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1

            # Move the right pointer backward if it's pointing to a non-alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters; if they differ, it's not a palindrome
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers toward the center
            left += 1
            right -= 1

        # All characters matched; the string is a valid palindrome
        return True
```

---

## ☀️ Python Notes 

### `isalnum()`  
Built-in method that checks whether a character is alphanumeric (A–Z, a–z, 0–9):

```python
'A'.isalnum()  # True
'9'.isalnum()  # True
```

Used to skip punctuation, spaces, etc.

---

### `lower()`  
Ensures case-insensitive comparison:

```python
'A'.lower() == 'a'  # True
```

Without this, `"A"` and `"a"` would not match.

---

## ☀️ Coding Walkthrough Script 

I start by initializing two pointers: one at the beginning of the string (`left`) and one at the end (`right`).  
As long as `left` is less than `right`, I do the following steps in each loop:

1. If the character at `left` is not alphanumeric, I skip it by moving `left` forward.  
2. If the character at `right` is not alphanumeric, I skip it by moving `right` backward.  
3. Once both `left` and `right` point to valid alphanumeric characters, I convert them to lowercase and compare.  
4. If they are not equal, I return `False` immediately — it’s not a palindrome.  
5. If they match, I move both pointers toward the center and continue the process.  

If the loop finishes without returning `False`, that means all valid character pairs matched — so I return `True`.

---

## ☀️ Brute Force vs Two Pointers 

| Strategy        | Description                                                  | Time    | Space  |
|----------------|--------------------------------------------------------------|---------|--------|
| Brute Force     | Clean the string, reverse it, then compare both             | O(N)    | O(N)   |
| Two Pointers    | Compare characters on the fly without extra string creation | O(N)    | O(1)   |

Two Pointers is more **space efficient**, especially on large inputs.
