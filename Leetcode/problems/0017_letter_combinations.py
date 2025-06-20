class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Result list to store all valid combinations
        res = []

        # Mapping of digits to corresponding letters on a phone keypad
        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

         # Edge case: if input is empty, return empty result
        if not digits:
            return []

        # Recursive backtracking function
        def backtrack(index, path):
            # Base case: if the path length equals the input length, add to result
            if index == len(digits):
                res.append(path)
                return

            # Get the letters that the current digit can represent
            for letter in phone[digits[index]]:
                # Append the letter to path and move to the next digit
                backtrack(index + 1, path + letter)

        # Start the recursion from index 0 with empty path
        backtrack(0, "")
        return res
