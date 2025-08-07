## ☀️ Leetcode 3. Longest Substring Without Repeating Characters

### Problem

Given a string `s`, find the length of the longest substring without repeating characters.

---

### ☀️ Brute Force

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_len = max(max_len, j - i + 1)

        return max_len
```

**Time Complexity:** O(n^2)**Space Complexity:** O(min(n, m)) — m is the character set size

---

### ☀️ Optimized Sliding Window

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len
```

**Time Complexity:** O(n)**Space Complexity:** O(min(n, m)) — m is the character set size

---

### ☀️ Tags

- HashMap
- Sliding Window
- Two Pointers
- Strings

---

### ☀️ Script

I use a sliding window to expand from the left to the right.
If I encounter a repeating character, I move the left pointer just after the previous index of that character.
I update the max length every time I expand the window.
A hashmap helps me quickly check and update character positions.
