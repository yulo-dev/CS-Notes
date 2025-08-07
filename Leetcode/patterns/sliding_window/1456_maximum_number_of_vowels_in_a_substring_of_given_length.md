# ☀️ Leetcode 1456 - Maximum Number of Vowels in a Substring of Given Length

## ☀️ Problem Summary

Given a string `s` and an integer `k`, return the maximum number of vowels in any substring of length `k`.

---

## ☀️ Brute Force Version (O(n * k))

```python
# Check all substrings of length k and count vowels one by one

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_count = 0

        # Loop through all possible substrings of length k
        for i in range(len(s) - k + 1):
            count = 0
            for j in range(i, i + k):
                if s[j] in vowels:
                    count += 1
            max_count = max(max_count, count)

        return max_count
```

- Time: O(n * k)
- Space: O(1)
- Checks every substring of length k and counts vowels each time

---

## ☀️ Sliding Window Version (Optimized, O(n))

```python
# Maintain a window of size k and update the vowel count incrementally

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")  # Use set for O(1) vowel lookup
        count = 0  # Current number of vowels in the window
        max_count = 0  # Maximum vowels found so far

        # Step 1: Initialize the first window of size k
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count

        # Step 2: Slide the window forward one character at a time
        for right in range(k, len(s)):
            if s[right] in vowels:
                count += 1  # Add new right-end character
            if s[right - k] in vowels:
                count -= 1  # Remove left-end character that is sliding out
            max_count = max(max_count, count)

        return max_count
```

- Time: O(n)
- Space: O(1)
- Only adds/removes one character at a time while maintaining count of vowels

---

## Explanation
First, I create a set of vowels for fast lookup. Then I initialize the count of vowels and max_count."
Then, I build the first window of size k and count the vowels. After that, I slide the window one character at a time.
At each step, I add the new character to the window if it's a vowel.
I also remove the character that falls out of the window, only if it's a vowel.
Finally, I update max_count based on the current vowel count.

---

## Clarifications

- The `right` pointer represents the **new character** entering the window.
- `right - k` points to the character that is now outside the window (left boundary).
- Even if `count` doesn't change (e.g., character removed isn't a vowel), the window **has moved**.
- You don't need an explicit `left` pointer — `right - k` already implies the left end.
- The window is always size `k` by definition of the loop and how entries/exits are tracked.
- `set("aeiou")` works like `set(['a','e','i','o','u'])` — because strings are iterable.
