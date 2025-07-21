class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)  # Convert string to a list so we can swap characters
        res = 0
        left, right = 0, len(s) - 1

        while left < right:
            i = right
            # Move pointer i leftward to find a match for s[left]
            while i > left and s[i] != s[left]:
                i -= 1

            if i == left:
                # No match found → s[left] must be the lone odd-count char
                # Push it one step toward center
                s[left], s[left + 1] = s[left + 1], s[left]
                res += 1
            else:
                # Match found at index i → move s[i] to the right end
                # Do this by swapping s[i] with s[i+1], ..., until it reaches s[right]
                for j in range(i, right):
                    s[j], s[j + 1] = s[j + 1], s[j]
                    res += 1
                left += 1
                right -= 1

        return res
