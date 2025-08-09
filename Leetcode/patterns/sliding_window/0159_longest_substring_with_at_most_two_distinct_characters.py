# solution 1: brute force
# time: O(n³)
# space: O(n)

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


# solution 2: Sliding Window + Last Index Map
# time: O(n)
# space: O(1)

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Sliding window using a last-index map (char -> last occurrence index in window).
        Keep updating last positions as we expand. If we exceed 2 distinct chars,
        drop the char whose LAST occurrence is farthest to the left, and jump left past it.

        Key idea:
        - We don't need per-char counts; we only need to know WHICH char to drop,
          and by how much to move `left`. The char to drop is the one with the
          smallest "last occurrence index" in the window.

        Time:  O(n) — we do O(1) work per step; taking min over <=3 keys is O(1)
        Space: O(1) — at most 3 keys before we drop back to 2
        """
        last_idx = {}  # char -> last index inside the current window
        left = 0
        best = 0

        for right, ch in enumerate(s):
            # 1) update last seen index of current char
            last_idx[ch] = right

            # 2) if invalid (>2 distinct), drop the leftmost-last-occurring char
            if len(last_idx) > 2:
                # choose the char whose last index is the smallest
                drop_char = min(last_idx, key=last_idx.get)
                # move left just past that char's last occurrence
                left = last_idx[drop_char] + 1
                # remove it from our map
                del last_idx[drop_char]

            # 3) window [left..right] is valid
            best = max(best, right - left + 1)

        return best
