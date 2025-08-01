class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper function to check if a substring is a palindrome
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        # Two pointers from both ends of the string
        left, right = 0, len(s) - 1

        # Check characters from outside to inside
        while left < right:
            if s[left] != s[right]:
                # If mismatch occurs, try skipping either left or right character
                # Case 1: skip the left character
                # Case 2: skip the right character
                # If either skipping left or skipping right leads to a palindrome, return True
                return is_palindrome(s[left + 1:right + 1]) or is_palindrome(s[left:right])
            # Move pointers inward if characters match
            left += 1
            right -= 1

        # If no mismatch found or fixed by one deletion, it is a palindrome
        return True
