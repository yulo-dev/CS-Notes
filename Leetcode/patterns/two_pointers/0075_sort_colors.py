class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the input list in-place so that all 0s come first,
        followed by 1s, then 2s — solving the Dutch National Flag problem.
        """

        # Initialize three pointers:
        # low: points to the next position for 0
        # mid: current element being evaluated
        # high: points to the next position for 2
        low = 0
        mid = 0
        high = len(nums) - 1

        # Traverse the array while mid pointer is within bounds
        while mid <= high:
            if nums[mid] == 0:
                # Swap the 0 to the front (low)
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Just move on if it's 1 — already in the middle
                mid += 1
            else:
                # nums[mid] == 2
                # Swap the 2 to the back (high)
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
