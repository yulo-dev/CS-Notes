# Leetcode 0076 - Minimum Window Substring

## ☀️ UMPIRE

- **Understand**: Return the smallest substring of `s` that contains all characters in `t`, including duplicates. If no such substring exists, return an empty string.
- **Match**: Input includes two strings `s` and `t` → best solved with sliding window technique.
- **Plan**: Use two pointers (`l`, `r`) to define a window. Expand `r` to include valid characters, then shrink from `l` to minimize. Use Counter for `t`, and a `window` dict to track current counts.
- **Implement**: See below.
- **Review**: Ensure shrinking window maintains the condition that all required characters (with correct counts) are present.
- **Evaluate**: Time O(n), Space O(k), where `n` is length of `s` and `k` is the number of unique characters in `t`.


## ☀️ Metadata

- **Appears In**: Grind75
- **Pattern**: Sliding Window (#12)
- **Data Structure**: Hash Map (dict)
- **Algorithm**: Sliding Window, Greedy Shrinking
- **Tags**: Sliding Window, Hash Map, Two Pointers, String


## ☀️ Solution Code

```python
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Count the frequency of each character in t
        t_count = Counter(t)

        # Initialize a dictionary to store character counts in the current window
        window = {}

        # 'have' is how many unique characters in t are satisfied in the window
        # 'need' is the number of unique characters required from t
        have, need = 0, len(t_count)

        # Result variables to store the smallest valid window's position and length
        res = [-1, -1]
        res_len = float("inf")

        # Left pointer of the sliding window
        l = 0

        # Expand the window by moving the right pointer
        for r in range(len(s)):
            char = s[r]
            # Add the current character to the window count
            window[char] = window.get(char, 0) + 1

            # If the current character's count matches the required count in t, increment 'have'
            if char in t_count and window[char] == t_count[char]:
                have += 1

            # Try to shrink the window from the left while it satisfies all conditions
            while have == need:
                # Update the result if this window is smaller
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Remove the leftmost character from the window
                window[s[l]] -= 1
                # If that character is needed and removing it breaks the requirement, decrement 'have'
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1

                # Move the left pointer to the right to shrink the window
                l += 1

        # Extract the smallest window from the original string using recorded indices
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
```


## ☀️ Trace

```
s = "ADOBECODEBANC", t = "ABC"
Step-by-step:
- r=0 to r=5 → window contains A, D, O, B, E, C → valid
- Start shrinking: remove A → now A is gone → invalid
- Expand r=6~9 → C, O, D, E → still invalid
- r=10 → B → valid again
- Shrink to "BANC" → this is the shortest valid window
```


## ☀️ Line-by-line Typing Script

- I start by checking if either string is empty — return "" if so.
- I count the frequency of each character in `t` using Counter.
- I initialize an empty window dictionary and variables `have`, `need`.
- `res` stores the best window so far as [start, end], and `res_len` tracks the shortest length.
- The left pointer `l` starts at 0.
- For each index `r` in `s`, I add `s[r]` to the window count.
- If this char matches the count in `t`, I increment `have`.
- While `have == need`, I try shrinking the window:
  - If current window is smaller, I update `res` and `res_len`
  - I shrink the left side by decrementing `window[s[l]]`
  - If removing that char makes it unsatisfied, I decrement `have`
  - Move left pointer `l` right
- After processing all `r`, I return the best window slice if found, else ""

