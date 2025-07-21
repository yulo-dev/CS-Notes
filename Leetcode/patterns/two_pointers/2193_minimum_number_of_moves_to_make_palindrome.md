# Leetcode 2193 - Minimum Number of Moves to Make Palindrome

## ☀️ UMPIRE
- **Understand**: Given a string `s`, you can move any character to any position. Find the minimum number of moves to make the string a palindrome.
- **Match**: String manipulation + Greedy + Two Pointers
- **Plan**:
    - Use two pointers from left and right.
    - Try to match s[left] with a character from the right.
    - If matched, move the match to right via adjacent swaps (each counts as 1 move).
    - If no match, this is the unpaired (odd) character → push it step-by-step to the center.
- **Implement**: See below.
- **Review**: Ensure pointer updates are correct and swaps are counted accurately.
- **Evaluate**: Time O(n^2) worst-case, Space O(n) due to list conversion.

---

## ☀️ Metadata
- **Difficulty**: Hard (Simulation + Greedy + Loop Control)
- **Data Structure**: List (for mutable string)
- **Algorithm**: Greedy pairing via swaps
- **Tags**: Greedy, Two Pointers, String, Simulation

---

## ☀️ Solution Code
```python
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)  # convert to list so we can swap
        res = 0
        left, right = 0, len(s) - 1

        while left < right:
            i = right
            # Move pointer i leftward to find a match for s[left]
            while i > left and s[i] != s[left]:
                i -= 1

            if i == left:
                # No match found — s[left] is the lone unpaired char → push toward center
                s[left], s[left+1] = s[left+1], s[left]
                res += 1
            else:
                # Found a matching char → move it to right by swapping
                for j in range(i, right):
                    s[j], s[j+1] = s[j+1], s[j]
                    res += 1
                left += 1
                right -= 1

        return res
```

---

## ☀️ Review Notes

### Why Not Use `while i == left:`
- Although the unpaired character is pushed one step at a time, the **outer loop** re-evaluates `s[left]` each round.
- So we don't need a nested while — the control flow is driven by `while left < right`.

### When Do We Enter the Else Block?
- Only if:
  - `i != left` and `s[i] == s[left]`
  - Meaning: we found a matching character to `s[left]`, not at the same position

### Why We Don't Count Pointer Search as a Move
- `while i > left and s[i] != s[left]: i -= 1` is only pointer movement — no actual char is moved
- Only swaps (actual moves) should be counted in `res`

---

## ☀️ Valid Input Assumption
- Input string is guaranteed to be rearrangeable into a palindrome.
- This means:
  - At most **1** character occurs an **odd** number of times (for the center).
  - All other characters can form pairs.
- So:
  - Either you find a matching character for `s[left]`, or it's the one unpaired char
  - The algorithm never fails to match unless it's the intended odd char
- This assumption is the key to why the while-if-else logic is valid

---

## ☀️ Difficulty Note
- This problem is less about applying a standard algorithm
- It tests:
  - Careful simulation of string mutation
  - Swap-based cost modeling
  - Multi-layer loop + pointer logic
  - Understanding structural guarantees of valid palindromes
- It often feels more like **systems-level logic reasoning** than pure algorithm
- Feeling confused is normal — solving this helps develop robust coding control flow thinking

---

## ☀️ Additional Intuition Notes
- The core of the solution relies on the **guarantee that the string can become a palindrome**.
- Therefore, there are only two types of situations:
  1. **One unpaired (odd-count) character** in the center (if string length is odd)
  2. All characters can be perfectly matched in pairs (if string length is even)
- With this guarantee:
  - `if i == left:` always targets the unpaired character
  - `else:` handles the characters that have a matching pair (to be swapped into place)
  - The inner `while i > left and s[i] != s[left]` uses a pointer `i` to **search** for a match to `s[left]`, but does **not move any characters**, hence no `res += 1` here
- The program design is tight and feels implicit, but it works only because the palindrome guarantee ensures the search will always converge

---

## ☀️ Full Trace with Example `s = "caabb"`

| Round | left | right | i   | Action / Observation                     | Swaps        | res |
|-------|------|--------|-----|------------------------------------------|--------------|-----|
| 1     | 0    | 4      | 0   | No match for `'c'` → push right          | (0↔1)        | 1   |
| 2     | 0    | 4      | 2   | Match `'a'` at i=2 → move to right end   | (2↔3↔4)      | 3   |
| 3     | 1    | 3      | 1   | No match for `'b'` → push right          | (1↔2)        | 4   |
| 4     | 1    | 3      | 3   | Match `'b'` at i=3 → already at right    | none         | 4   |
| 5     | 2    | 2      | —   | left == right → Done                     |              |     |

- Final state: `['a', 'b', 'c', 'b', 'a']`
- Total moves: `res = 4`
