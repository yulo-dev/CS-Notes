class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to enable the two-pointer approach
        nums.sort()
        answer = []

        # Fix the first number and use two pointers to find the other two
        for i in range(len(nums) - 2):
            # Since the array is sorted, if the current number > 0,
            # all numbers after it will also be > 0 → cannot sum to zero
            if nums[i] > 0:
                break
                
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    # Total too small → move left pointer to get a bigger number
                    l += 1
                elif total > 0:
                    # Total too big → move right pointer to get a smaller number
                    r -= 1
                else:
                    # Found a valid triplet
                    answer.append([nums[i], nums[l], nums[r]])

                    # Skip duplicates: clear out repeated values around left/right
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # Move both pointers to the next new values (next room)
                    l += 1
                    r -= 1

        return answer
