
# solution 1: Brute Force Version 
# Time: O(n * k)
# Space: O(1)
# Checks every substring of length k and counts vowels each time

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


# solution 2: Sliding Window Version
# Time: O(n)
# Space: O(1)
# Only adds/removes one character at a time while maintaining count of vowels

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
