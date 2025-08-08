# solution 1: Sliding Window with Recompute Max
# time: O(n)
# space: O(1)

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Sliding window with a frequency map (dict).
        At each step, we recompute the max frequency in the window.
        This is simpler to reason about (beginner-friendly).
        """
        freq = defaultdict(int)   # char -> count in the current window
        left = 0                  # left boundary of the window
        best = 0                  # answer (longest valid window length)

        for right, ch in enumerate(s):
            # expand right
            freq[ch] += 1

            # current window size
            window_len = right - left + 1

            # the most frequent character count inside the window
            # (recomputed each time; still O(1) since at most 26 uppercase letters)
            max_count = max(freq.values())

            # If we need to replace more than k chars to make the window uniform,
            # shrink from the left.
            # #replacements needed = window_len - max_count
            while window_len - max_count > k:
                freq[s[left]] -= 1
                left += 1
                window_len = right - left + 1
                # (Optionally recompute max_count here; not necessary if alphabet is fixed 26,
                # but doing it keeps the logic explicit and beginner-friendly.)
                max_count = max(freq.values())

            # update answer
            best = max(best, window_len)

        return best



# solution 2: Optimized Sliding Window with Static Max Count
# time: O(n)
# space: O(1)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Optimized sliding window with a fixed-size array for A..Z
        and a monotonic non-decreasing max_count.
        Time: O(n), Space: O(1)
        """
        count = [0] * 26          # frequency for 'A'..'Z' in the current window
        left = 0                  # left boundary of the window
        max_count = 0             # highest single-char frequency seen in the window so far
        best = 0                  # answer (longest valid window length)

        for right in range(len(s)):
            # map current char to [0..25]
            idx = ord(s[right]) - ord('A')
            count[idx] += 1

            # update the best (max) frequency in the current window
            # NOTE: we only increase max_count; we do NOT decrease it when shrinking.
            # This is fine because an overestimated max_count only makes the window
            # shrink a little later, but the validity check (while loop) still enforces correctness.
            max_count = max(max_count, count[idx])

            # window length
            window_len = right - left + 1

            # If we need to replace more than k characters to make the window uniform,
            # shrink from the left until valid again.
            # replacements needed = window_len - max_count
            while window_len - max_count > k:
                left_idx = ord(s[left]) - ord('A')
                count[left_idx] -= 1
                left += 1
                window_len = right - left + 1

            # update best answer
            best = max(best, window_len)

        return best
