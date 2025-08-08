# Leetcode 424 — Longest Repeating Character Replacement

## UMPIRE Note (Interview-Ready)

### U — Understand (Clarify the problem)
**Goal:** Longest substring that can become all the same character after at most `k` replacements.  
**Constraints & Clarifications**
- Input: `s` is uppercase A–Z only; `k >= 0`.
- We replace characters *within a contiguous substring*.
- Return the *length* only, not the substring.
- If `k >= len(s)`, answer is `len(s)` (we can convert the whole string).

**Key Insight Question (to self/interviewer):**
> If in a window we know the count of the most frequent character is `max_count`, how many replacements are needed to make the whole window uniform?  
**Answer:** `window_len - max_count`. The window is valid if `window_len - max_count <= k`.

---

### M — Match (Identify patterns)
- **Sliding Window** (two pointers).
- **Frequency Counting** inside the window.
- Maintain a running `max_count` of a single character within the window.
- Validity check drives left-shrinking: `(right - left + 1) - max_count <= k`.

Related patterns/problems to recall:
- LC 3 (Longest Substring Without Repeating Characters) — sliding window + positions map.
- LC 1004 (Max Consecutive Ones III) — flip at most `k` zeros; same validity style.
- LC 567 (Permutation in String) — window + frequency matching.

---

### P — Plan (High-level algorithm)
1. Use `left` and `right` as window boundaries.
2. Keep an array `count[26]` for frequencies of `A..Z`.
3. For each `right`, increment `count[s[right]]`; update `max_count` (only increase).
4. If window invalid: while `(window_len - max_count) > k`, move `left` forward and decrement `count[s[left]]`.
5. Track the best window length seen.
6. Return the best length.

Why `max_count` only increases?
- Overestimating `max_count` might delay shrinking, but the while-loop **guarantees** we never keep an invalid window as the answer. It preserves correctness and avoids recomputing `max()` each step, keeping the algorithm `O(n)`.

---

### I — Implement (Clean code with comments)

#### Version 1 — Beginner Sliding Window with Recompute Max (dict)
```python
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)   # char -> frequency in current window
        left = 0
        best = 0

        for right, ch in enumerate(s):
            # expand window by including s[right]
            freq[ch] += 1

            window_len = right - left + 1
            # explicit recomputation: still O(1) since alphabet size is 26
            max_count = max(freq.values())

            # shrink while invalid: replacements needed > k
            while window_len - max_count > k:
                freq[s[left]] -= 1
                left += 1
                window_len = right - left + 1
                max_count = max(freq.values())  # keep logic explicit for clarity

            best = max(best, window_len)

        return best
```

#### Version 2 — Optimized Sliding Window with Static Max Count (array)
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26          # frequencies for 'A'..'Z'
        left = 0
        max_count = 0             # highest single-char frequency seen in window
        best = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            # only increase; do not decrease when shrinking
            max_count = max(max_count, count[idx])

            # current window length
            window_len = right - left + 1

            # if invalid, shrink from the left until valid
            while window_len - max_count > k:
                left_idx = ord(s[left]) - ord('A')
                count[left_idx] -= 1
                left += 1
                window_len = right - left + 1

            # record best valid window
            best = max(best, window_len)

        return best
```

**Complexity**
- Time: `O(n)` — each index enters/leaves the window at most once.
- Space: `O(1)` — fixed 26-length array (or O(1) for dict with A–Z).

---

### R — Review (Reason about correctness & pitfalls)
- **Correctness invariant:** While loop enforces `(window_len - max_count) <= k`.  
- **Why static `max_count` is safe:** An overestimated `max_count` causes a window to *seem* more valid, not less. The while-loop still checks validity; no invalid window can be taken as answer because we compute `best` only after enforcing the condition.
- **Pitfalls:**
  - Mixing fullwidth `'Ａ'` vs ASCII `'A'` in `ord()`.
  - Using `right` vs `i` inconsistently in `(right - left + 1)`.
  - Accidentally resetting/decreasing `max_count` on shrink (not needed).
  - Off-by-one errors in window length.

**Dry Run (s = "AABABBA", k = 1)**
| step | left | right | char | count(A,B) | max_count | window_len | need = len - max | action | best |
|-----:|-----:|------:|------|------------|-----------|------------|------------------|--------|------|
| 0 | 0 | 0 | A | A=1,B=0 | 1 | 1 | 0 | keep | 1 |
| 1 | 0 | 1 | A | A=2,B=0 | 2 | 2 | 0 | keep | 2 |
| 2 | 0 | 2 | B | A=2,B=1 | 2 | 3 | 1 | keep | 3 |
| 3 | 0 | 3 | A | A=3,B=1 | 3 | 4 | 1 | keep | 4 |
| 4 | 0 | 4 | B | A=3,B=2 | 3 | 5 | 2 | shrink left→1 | 4 |
| 5 | 1 | 5 | B | A=2,B=3 | 3 | 5 | 2 | shrink left→2 | 4 |
| 6 | 2 | 6 | A | A=3,B=3 | 3 | 5 | 2 | shrink left→3 | 4 |

Final `best = 4`.

---

### E — Evaluate (Edge cases & tests)
- `s = ""` → `0`
- `k = 0` → longest run of the same character
- `k >= len(s)` → `len(s)`
- All same chars (e.g., `"AAAA"`, any `k`) → `len(s)`
- Alternating chars (e.g., `"ABABAB"`, various `k`) → check formula

**Quick tests:**
```python
assert Solution().characterReplacement("ABAB", 2) == 4
assert Solution().characterReplacement("AABABBA", 1) == 4
assert Solution().characterReplacement("AAAA", 0) == 4
assert Solution().characterReplacement("ABC", 0) == 1
assert Solution().characterReplacement("ABC", 2) == 3
```

---

## Script
I'll solve this with a sliding window. The idea is to keep a window where I can make all characters the same with at most `k` replacements.  
Inside the window, if the most frequent character appears `max_count` times, then the number of changes needed is `window_len - max_count`. As long as that is `<= k`, the window is valid.  
I’ll expand the window to the right, update the frequency of the new character, and track a non-decreasing `max_count`. If the window becomes invalid, I’ll move the left pointer forward and decrement the left character’s count until it’s valid again. Throughout, I’ll track the longest valid window length.


1. *Initialize frequency array `count[26]`, `left = 0`, `max_count = 0`, `best = 0`.*  
2. *Iterate `right` over indices of `s`.*  
3. *Map `s[right]` to an index `idx = ord(s[right]) - ord('A')` and increment `count[idx]`.*  
4. *Update `max_count = max(max_count, count[idx])`.*  
5. *Compute `window_len = right - left + 1`. If `window_len - max_count > k`, the window is invalid, so shrink from the left: decrement `count` for `s[left]` and advance `left` until valid.*  
6. *Update `best = max(best, window_len)` and continue.*  
7. *Return `best` as the result.*

**One-liner summary at the end:**  
> The check `(window_len - max_count) <= k` ensures we can convert the whole window to one character using at most `k` replacements, and sliding/shrinking maintains the longest valid window in `O(n)` time.

---
