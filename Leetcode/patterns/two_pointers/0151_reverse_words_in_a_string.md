# Leetcode 0151 - Reverse Words in a String

## ☀️ UMPIRE

- **Understand**:

  - Input: A string `s` that may contain leading/trailing/multiple spaces between words.
  - Output: Return a new string where the words are reversed and separated by **a single space**.

- **Match**: String manipulation problem with constraints on space and word order → **Two Pointers**, reverse traversal, or split/rebuild logic.

- **Plan**:

  - Use a **reverse traversal** with two pointers (`i`, `j`) to locate each word from the end.
  - For each word found, append it to the result list.
  - Join the result list with a single space.

- **Implement**: See Method 2 below (Two Pointers Reverse Traverse).

- **Review**:

  - Are we trimming excessive spaces?
  - Are we correctly slicing each word?
  - Are we avoiding trailing/leading whitespace in the final result?

- **Evaluate**:

  - Time: O(n) — Each character is visited once.
  - Space: O(n) — For the result list and output string.

---

## ☀️ Code (Method 2: Reverse Traverse with Two Pointers)

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        i = len(s) - 1  # Start from the end

        while i >= 0:
            # Skip trailing spaces
            while i >= 0 and s[i] == ' ':
                i -= 1

            if i < 0:
                break

            j = i  # j marks the end of the word

            # Move i to the start of the word
            while i >= 0 and s[i] != ' ':
                i -= 1

            # Append the word from i+1 to j (inclusive)
            result.append(s[i+1 : j+1])

        return ' '.join(result)
```

---

## ☀️ Coding Walkthrough Script 

- We use two pointers to scan the string from the end.
- First, we skip any spaces. Then we mark the end of the word with `j`.
- Next, we walk back to the start of the word with `i`, and slice out that word.
- We repeat this until all words are found, then join them with a single space.

---

## ☀️ Complexity Comparison

| Method               | Time Complexity | Space Complexity | Notes                                          |
| -------------------- | --------------- | ---------------- | ---------------------------------------------- |
| Python Built-in      | O(n)            | O(n)             | Uses `split()` and `join()`                    |
| Method 2 (Two Ptrs)  | O(n)            | O(n)             | Manual trimming + slicing in reverse traversal |
| Method 3 (Full Rev.) | O(n)            | O(n)             | Extra reversing logic; more verbose            |

Method 2 is preferred in interviews because it’s simple, efficient, and avoids extra abstraction.

---

## ☀️ Edge Cases

- One word, no spaces: `"hello"` → Should return `"hello"`
- One word, many spaces: `"   world   "` → Should return `"world"`
- Multiple spaces between words: `"a   b   c"` → Should return `"c b a"`
