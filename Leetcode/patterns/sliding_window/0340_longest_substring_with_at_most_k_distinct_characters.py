# solution 1: brute force
# time: O(n³)
# space: O(n)

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        Enumerate all substrings and check the number of distinct characters.
        Time Complexity:  O(n^3)  -> O(n^2) substrings * O(n) to count distinct
        Space Complexity: O(n)    -> temporary set for distinct count
        """
        if k == 0 or not s:
            return 0

        n = len(s)
        best = 0

        for i in range(n):
            for j in range(i, n):
                # Count distinct chars in s[i:j+1]
                distinct = len(set(s[i:j+1]))
                if distinct <= k:
                    best = max(best, j - i + 1)

        return best


# solution 2: Sliding Window + Last Index Map 
# time: O(n·k)
# space: O(k)

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        Sliding window with a dictionary storing the last index of each character.
        Key idea:
        - Expand window by moving right pointer.
        - If distinct count exceeds k, remove the char whose last occurrence is leftmost.
        - Move left pointer past the last occurrence of that char.
        
        Time Complexity:  O(n·k)  -> finding min over <= k+1 chars each time
        Space Complexity: O(k)    -> store up to k distinct chars
        """
        if k == 0 or not s:
            return 0

        left = 0
        seen = {}  # char -> last index in current window
        best = 0

        for right, ch in enumerate(s):
            seen[ch] = right

            if len(seen) > k:
                # Find char with smallest last occurrence index
                drop_char = min(seen, key=seen.get)
                left = seen[drop_char] + 1
                del seen[drop_char]

            best = max(best, right - left + 1)

        return best



# solution 3: Sliding Window + Counter (Optimized)
# time: O(n)
# space: O(k)

from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        Sliding window with a Counter to track character counts.
        Key idea:
        - Expand window to the right, adding char counts.
        - If distinct chars exceed k, shrink from left until valid.
        - This avoids O(k) min() calls, making it strictly O(n).
        
        Time Complexity:  O(n)   -> each char enters and leaves the window once
        Space Complexity: O(k)   -> store up to k distinct chars
        """
        if k == 0 or not s:
            return 0

        left = 0
        count = Counter()
        best = 0

        for right, ch in enumerate(s):
            count[ch] += 1

            # Shrink window until we have at most k distinct chars
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            best = max(best, right - left + 1)

        return best
