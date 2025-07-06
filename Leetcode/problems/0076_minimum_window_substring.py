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
