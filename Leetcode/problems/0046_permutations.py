class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Initialize result list to store all permutations
        res = []
        # Track which elements have been used in the current path
        used = [False] * len(nums)

        # Recursive backtracking function to build permutations
        def backtrack(path):
            # If path contains all elements, it's a complete permutation
            if len(path) == len(nums):
                res.append(path[:])  # Add a copy of the path to results
                return

            # Try each unused element at the current position
            for i in range(len(nums)):
                if not used[i]:
                    # Choose the element
                    used[i] = True
                    path.append(nums[i])

                    # Explore further with the current choice
                    backtrack(path)

                    # Backtrack: remove the last element and mark as unused
                    path.pop()
                    used[i] = False

        # Start backtracking with an empty path
        backtrack([])
        return res