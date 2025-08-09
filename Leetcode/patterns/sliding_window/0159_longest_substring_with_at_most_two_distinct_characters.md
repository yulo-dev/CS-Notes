# Leetcode 159 — Longest Substring with At Most Two Distinct Characters

## ☀️ Problem
Given a string `s`, return the length of the longest substring that contains **at most two distinct characters**.

---

## ☀️ UMPIRE

### Understand
- **Input/Output:** Input: string `s`. Output: an integer = max length of a substring with ≤ 2 distinct characters.
- **Constraint:** 1 ≤ |s| ≤ 10^5 (typical). Characters can be arbitrary ASCII/Unicode.
- **Edge cases:** Empty string → 0; string length 1 → 1; if the whole string already has ≤2 distinct chars → answer is |s|.

### Match
- **Pattern:** Sliding Window / Two Pointers over a string.
- **Similar problems:** LC 904 (Fruit Into Baskets), LC 340 (At Most K Distinct), LC 3 (Longest Substring Without Repeating Characters).
- **Data structure:** Hash map to track either (a) frequency or (b) last index.

### Plan
Two standard approaches (both O(n)):
1) **Frequency Map (Beginner):** maintain `count[ch]` inside the window; shrink while `len(count) > 2` by decrementing `count[s[left]]`.
2) **Last Index Map (Advanced):** maintain `last_idx[ch] = last position of ch in window`; if `len(last_idx) > 2`, drop the char whose last index is the smallest and jump `left` to `last_idx[drop] + 1`.

### Implement
See code sections below (Beginner & Advanced).

### Review
- **Why sliding window?** The validity predicate (“≤ 2 distinct”) is monotonic when extending/shrinking a contiguous range; each character enters/leaves the window at most once → linear pass.
- **Why last-index works?** When >2 distinct, the only char we should remove is the one whose **last occurrence** is leftmost; removing it allows `left` to jump directly to a valid position.

### Evaluate
- **Time:** O(n) for either approach (single pass; O(1) operations per step).
- **Space:** O(1) extra (at most 3 keys live briefly; we cap at 2 distinct).

---

## ☀️ Tags / Data Structure / Algorithm
- **Tags:** Sliding Window, Two Pointers, String
- **Data Structure:** Hash Map / Dictionary (frequency map or last-index map)
- **Algorithm:** Sliding Window with (a) Count Map **or** (b) Last Index Map

---

## ☀️ Solution 1 — Brute Force (Educational, O(n^3))

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        True brute force:
        - Enumerate all substrings s[i:j+1]
        - For each substring, count distinct characters from scratch
        Time:  O(n^3)  (O(n^2) substrings * O(n) to count distinct)
        Space: O(n)    (set to count distinct in worst case)
        """
        n = len(s)
        best = 0

        for i in range(n):
            for j in range(i, n):
                # count distinct characters in s[i:j+1]
                distinct = len(set(s[i:j+1]))
                if distinct <= 2:
                    best = max(best, j - i + 1)

        return best
```

---

## ☀️ Solution 2 — Sliding Window + Frequency Map, O(n)

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Sliding window with a frequency map (char -> count).
        Expand right; if we have > 2 distinct chars, shrink left by
        decrementing counts until the window becomes valid again.
        Time:  O(n)
        Space: O(1)  (at most 3 distinct temporarily; we cap at 2)
        """
        from collections import defaultdict

        left = 0
        count = defaultdict(int)  # current window char -> frequency
        best = 0

        for right, ch in enumerate(s):
            count[ch] += 1

            while len(count) > 2:
                left_ch = s[left]
                count[left_ch] -= 1
                if count[left_ch] == 0:
                    del count[left_ch]
                left += 1

            best = max(best, right - left + 1)

        return best
```

---

## ☀️ Solution 3 — Advanced (Sliding Window + Last Index Map, O(n))

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Sliding window using a last-index map (char -> last occurrence index in window).
        Update last positions as we expand. If we exceed 2 distinct chars,
        drop the char whose LAST occurrence is farthest to the left, and jump left past it.
        Time:  O(n) — O(1) work per step; min over <=3 keys is O(1)
        Space: O(1) — at most 3 keys before we drop back to 2
        """
        last_idx = {}  # char -> last index in the current window
        left = 0
        best = 0

        for right, ch in enumerate(s):
            last_idx[ch] = right

            if len(last_idx) > 2:
                drop = min(last_idx, key=last_idx.get)  # char with smallest last index
                left = last_idx[drop] + 1               # jump left just past it
                del last_idx[drop]

            best = max(best, right - left + 1)

        return best
```

---

## ☀️ Complexity Comparison

| Solution | Method                                  | Time      | Space |
|---------:|-----------------------------------------|-----------|-------|
| 1        | Brute Force                             | O(n^3)    | O(n)  |
| 2        | Sliding Window + Frequency Map (Beginner) | O(n)      | O(1)  |
| 3        | Sliding Window + Last Index Map (Advanced) | O(n)      | O(1)  |

---

## ☀️ Script
I’ll use a **sliding window** and keep a small **map** to track the window’s state.
At any time the window must have **at most two distinct characters**.
With a **frequency map**, if we exceed two, I’ll **shrink from the left** by decrementing counts until we’re valid.
Alternatively, with a **last-index map**, if we exceed two, I **drop the char** whose last occurrence is **leftmost** and **jump `left`** just past it.  
This yields **O(n)** time and **O(1)** extra space.
