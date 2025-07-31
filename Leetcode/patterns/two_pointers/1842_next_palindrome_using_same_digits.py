class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        half_n = n // 2

        # Take the left half as a list for easier manipulation
        left = list(num[:half_n])
        # Middle character if odd length
        mid = "" if n % 2 == 0 else num[half_n]

        # Standard next_permutation algorithm
        def next_permutation(arr):
            # 1. Find the first decreasing index from the right
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            if i < 0:
                return False

            # 2. Find the element just larger than arr[i]
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1

            # 3. Swap and reverse
            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = reversed(arr[i + 1:])
            return True

        # If no next permutation of the left part exists
        if not next_permutation(left):
            return ""

        # Build the palindrome using updated left
        new_left = ''.join(left)
        return new_left + mid + new_left[::-1]
