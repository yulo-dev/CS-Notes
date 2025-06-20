class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # This will store all the subsets

        def backtrack(start, path):
            # Add the current path (subset) to the result
            res.append(path[:])  # Use path[:] to make a copy

            # Iterate from the current index to the end of the list
            for i in range(start, len(nums)):
                # Choose: add nums[i] to the current subset
                path.append(nums[i])

                # Explore: move to the next index (only choose from remaining elements)
                backtrack(i + 1, path)

                # Un-choose: backtrack by removing the last element
                path.pop()

        # Start the backtracking from index 0 with an empty path
        backtrack(0, [])
        return res
