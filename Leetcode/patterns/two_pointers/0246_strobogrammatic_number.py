# version 1: Two pointers

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # Define the valid strobogrammatic digit mappings
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        # Initialize two pointers at both ends of the string
        left, right = 0, len(num) - 1

        # Use two pointers to compare mirrored digits
        while left <= right:
            # Check if both digits are in the valid mapping
            if num[left] not in mapping or num[right] not in mapping:
                return False
            
            # The rotated version of left digit must match the right digit
            if mapping[num[left]] != num[right]:
                return False

            # Move pointers inward
            left += 1
            right -= 1

        # If all pairs are valid, it's strobogrammatic
        return True


# version 2: Build the rotated string then compare

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # Mapping for each strobogrammatic digit
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        rotated = []

        # Traverse the original string in reverse
        for ch in reversed(num):
            if ch not in mapping:
                return False  # Invalid digit
            rotated.append(mapping[ch])

        # Join and compare with the original
        return ''.join(rotated) == num
