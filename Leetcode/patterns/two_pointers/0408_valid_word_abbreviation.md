# Leetcode 0408 - Valid Word Abbreviation

## ☀️ UMPIRE

- **Understand**:
  
  - Input: A `word` and an `abbr` string that may contain digits (for abbreviation).
  - Output: Return `True` if `abbr` is a valid abbreviation of `word`, else `False`.

  - Can abbreviation start with zero? No — leading zeros are invalid, and the input might contain them. So we must guard against them explicitly.
  - What characters are allowed? Per constraints, `word` and `abbr` contain only lowercase letters and digits.
  - Do all digits represent a number to skip in `word`? Yes — e.g., "i12iz4n" means: skip 12 characters.

- **Match**: This is a two-pointer traversal problem — one pointer for `word`, one for `abbr`.

- **Plan**:
  
  - Initialize two pointers `i` and `j` to traverse `word` and `abbr`.
  - If `abbr[j]` is a digit, extract the number and advance `i`.
    - If digit starts with `'0'`, return False (invalid abbreviation).
  - If `abbr[j]` is a letter, compare it with `word[i]`. If not equal, return False.
  - At the end, ensure both pointers reach the end of their strings.

- **Implement**: See code below.

- **Review**:
  - Are we correctly skipping letters in `word` based on the number?
  - Are we checking for invalid leading zeros?
  - Are both `i` and `j` at the end when returning True?

- **Evaluate**:
  - Time: O(n + m) where n = len(word), m = len(abbr)
  - Space: O(1), constant extra space

---

## ☀️ Code (Two Pointers)

```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0  # i for word, j for abbr

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False  # leading zero is invalid

                num = 0
                # Build the number to skip
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num  # skip ahead in the word
            else:
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        return i == len(word) and j == len(abbr)
```

---

## ☀️ Complexity Comparison

| Approach        | Time     | Space  | Notes                                        |
|----------------|----------|--------|----------------------------------------------|
| Two Pointers   | O(n + m) | O(1)   | Efficient traversal with number parsing      |
| Brute Force ✖  | N/A      | N/A    | No clean brute-force without full simulation |

Two-pointer is ideal because it efficiently parses numbers and letters in one pass.

---

## ☀️ Why Two Pointers?

- We use one pointer `i` to walk through `word`, and one `j` for `abbr`.
- When we encounter a digit in `abbr`, we build a number and advance `i`.
- When we encounter a letter, we compare `word[i] == abbr[j]`.
- This coordinated movement between the two makes it a **Two Pointers** pattern.

---

## ☀️ Edge Cases (based on constraints)

- Leading zero in abbr (e.g. `"l01e"`) → invalid → return False
- `abbr` skips to the end exactly → valid if `i == len(word)` and `j == len(abbr)`
- Abbreviation has too many or too few skips → return False
- Letter mismatch → return False

Per Leetcode Constraints:
- 1 <= len(word), len(abbr) <= 100
- Input contains only lowercase English letters and digits
- There is **at least one character** in each string
