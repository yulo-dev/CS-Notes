class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # answer stores the final count of valid subarrays
        answer = 0
        # leftBound is the index of the most recent invalid element
        # (element < minK or element > maxK). Any subarray starting
        # before or at leftBound is invalid.
        leftBound = -1
        # minPos stores the index of the most recent occurrence of minK
        minPos = -1
        # maxPos stores the index of the most recent occurrence of maxK
        maxPos = -1

        # Iterate through the array
        for i, num in enumerate(nums):
            # If num is outside [minK, maxK], update leftBound
            if num < minK or num > maxK:
                leftBound = i
            
            # Update positions of minK and maxK when found
            if num == minK:
                minPos = i
            if num == maxK:
                maxPos = i

            # The earliest position where both minK and maxK appear
            # after the last invalid value is min(minPos, maxPos)
            # All valid subarrays ending at index i start after leftBound
            # and before or at min(minPos, maxPos)
          
            validCount = max(0, min(minPos, maxPos) - leftBound)
            answer += validCount

        return answer
