
# Brute Force Approach
# Time: O(n^2), Space: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            seen = set()
            current_len = 0

            for j in range(i, len(s)):
                if s[j] in seen:
                    break  # stop at duplicate
                seen.add(s[j])
                current_len += 1

            max_len = max(max_len, current_len)

        return max_len


# Optimized Sliding Window using HashSet
# Time: O(n), Space: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()  # Store characters in current window
        left = 0      # Left pointer
        max_len = 0   # Length of longest valid substring

        for right in range(len(s)):  # Scan string with right pointer
            while s[right] in seen:  # If duplicate character found
                seen.remove(s[left])  # Remove left character
                left += 1             # Move left pointer

            seen.add(s[right])        # Add current character
            max_len = max(max_len, right - left + 1)  # Update max length

        return max_len  # Return result
