# solution 1: Brute Force (Double Loop)
# Time: O(n²) – double loop
# Space: O(1) – no extra data structure
# Issue: Too slow for large input (not acceptable in real interview, but good as a baseline)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       # Compare every pair
       for i in range(len(nums)):
          for j in range(i + 1, len(nums)):
             if nums[i] == nums[j]:
                return nums[i]
       return -1  # should not happen because duplicate guaranteed  


# solution 2: Hash Set
# Time: O(n) – single pass
# Space: O(n) – hash set to store seen numbers
# Issue: Extra memory is not allowed by the problem

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       seen = set()  # store numbers we've already encountered
       for num in nums:
          if num in seen:
             return num  # duplicate found
          seen.add(num)
       return -1  # should not happen because duplicate guaranteed


# solution 3: Slow and Fast Pointers (Cycle Detection)
# Time: O(n) – each pointer visits at most n steps
# Space: O(1) – only two pointers
# Best choice when interviewer mentions O(1) space & O(n) time

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Use Floyd's Tortoise and Hare algorithm to detect a cycle.
        # Treat array as a linked list:
        # - index = node position
        # - nums[index] = pointer to next node
        
        slow = 0
        fast = 0
        
        # Find the intersection point inside the cycle
        while True:
            slow = nums[slow]            # move slow pointer by 1 step
            fast = nums[nums[fast]]      # move fast pointer by 2 steps
            if slow == fast:
                break                    # pointers meet → cycle detected
        
        # Phase 2: Find the entrance of the cycle
        # Reset one pointer to the start (index 0)
        slow = 0
        while slow != fast:
            slow = nums[slow]            # move both pointers one step
            fast = nums[fast]
        
        # When they meet again, it's the cycle entrance → duplicate number
        return slow
