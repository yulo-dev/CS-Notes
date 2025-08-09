# Leetcode 340 – Longest Substring with At Most K Distinct Characters

## ☀️ UMPIRE

### Understand
We need the **length of the longest substring** that contains **at most `K` distinct characters**.

**Constraints**:
- `1 <= s.length <= 10^5`
- `0 <= k <= 50`
- Characters are from standard ASCII (English letters, digits, symbols, etc.)
- We only count *distinct* characters, not frequency.
- Output is an integer (length).

**Key clarifications**:
- If `k = 0`, the answer is always 0.
- If `k >= len(s)`, the answer is `len(s)`.
- We need *continuous* substrings, not subsequences.

### Match
- This is a **variable-size sliding window** problem.
- Similar to:
  - LC 159 (k = 2 fixed)
  - LC 3 (Longest substring without repeating characters)
- Tools: HashMap / Counter to track chars in the window.

### Plan
We can solve with **Sliding Window**:
1. Expand `right` pointer to include new chars.
2. Track the count or last index of each char.
3. If distinct chars exceed `k`, shrink from `left` until valid again.
4. Track the max window length.

### Implement
We will show 3 versions:
1. **Brute Force** (O(n³))
2. **Sliding Window + Last Index Map** (Optimized jump shrink)
3. **Sliding Window + Counter** (Generic shrink)

### Review
Check with examples:
- s = "eceba", k = 2 → Output = 3 ("ece")
- s = "aa", k = 1 → Output = 2 ("aa")
- s = "a", k = 5 → Output = 1 ("a")

### Evaluate
- Brute Force: O(n³), too slow for n = 10^5
- Sliding Window: O(n) time, O(k) space → acceptable for constraints.

---

## ☀️ Solution 1 – Brute Force

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        Brute force:
        - Enumerate all substrings s[i:j+1]
        - Count distinct chars each time
        Time:  O(n^3) → too slow for n=1e5
        Space: O(n)   → set to hold distinct chars
        """
        n = len(s)
        best = 0

        for i in range(n):
            for j in range(i, n):
                distinct = len(set(s[i:j+1]))
                if distinct <= k:
                    best = max(best, j - i + 1)

        return best
```

---

## ☀️ Solution 2 – Sliding Window + Last Index Map

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        Optimized Sliding Window:
        - Map char → last seen index
        - When > k distinct chars, drop the char whose last index is smallest (farthest left)
          and jump `left` to that index + 1
        - Works best when k is small (like k=2 in LC 159)

        Time:  O(n)  (min over <= k+1 keys is O(1) if k small)
        Space: O(k)
        """
        if k == 0:
            return 0

        last_idx = {}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            last_idx[ch] = right

            if len(last_idx) > k:
                drop_char = min(last_idx, key=last_idx.get)
                left = last_idx[drop_char] + 1
                del last_idx[drop_char]

            best = max(best, right - left + 1)

        return best
```

---

## ☀️ Solution 3 – Sliding Window + Counter

```python
from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        Generic Sliding Window with Counter:
        - Count each char frequency in window
        - When > k distinct chars, shrink from left until valid
        - More general and stable for large k (up to 50 here)

        Time:  O(n)
        Space: O(k)
        """
        if k == 0:
            return 0

        count = Counter()
        left = 0
        best = 0

        for right, ch in enumerate(s):
            count[ch] += 1

            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            best = max(best, right - left + 1)

        return best
```

---

## ☀️ Why Sliding Window?
- Brute force checks **all substrings** → too slow for n=10^5.
- Sliding Window ensures:
  - Each character is added/removed at most once → O(n) time.
  - Space O(k), where k ≤ 50 (small).

---

## ☀️ Script
We want the longest substring with at most K distinct characters.  
The natural approach is a sliding window: expand the right boundary to include characters, track counts or last indices, and shrink the left boundary when we exceed K distinct chars.  
> In Python, I can use a Counter for general k, or a last-index map for small k to jump left more efficiently."

---

## ☀️ Tags / Data Structure / Algorithm
- **Tags**: Sliding Window, HashMap, Two Pointers
- **Data Structures**: HashMap / Counter
- **Algorithm**: Variable-size Sliding Window

---
