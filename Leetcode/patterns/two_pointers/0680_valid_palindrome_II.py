# method 1: space complexity O(n) 

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

# method 2: space complexity O(1) 

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper function: check if s[l:r] is palindrome (inclusive)
        def is_palindrome_range(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Skip left or skip right, check directly without slicing
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left += 1
            right -= 1

        return True
