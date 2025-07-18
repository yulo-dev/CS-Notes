class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the beginning and end of the string
        left = 0
        right = len(s) - 1

        # Traverse toward the center
        while left < right:
            # Move the left pointer forward if it's pointing to a non-alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move the right pointer backward if it's pointing to a non-alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare lowercase characters; if they differ, it's not a palindrome
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers toward the center
            left += 1
            right -= 1

        # All characters matched; the string is a valid palindrome
        return True
