class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        # Helper function to calculate next index (handle circular wrapping)
        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:   # Already visited, skip
                continue

            direction = nums[i] > 0   # True if forward, False if backward
            slow = fast = i

            # Floyd's Tortoise and Hare (Cycle Detection)
            while True:
                # Move slow pointer one step
                if (nums[slow] > 0) != direction:   # Direction changed → invalid path
                    break
                slow = next_index(slow)
                if (nums[slow] > 0) != direction:   # Direction changed after move
                    break

                # Move fast pointer two steps
                fast = next_index(fast)
                if (nums[fast] > 0) != direction:
                    break
                fast = next_index(fast)
                if (nums[fast] > 0) != direction:
                    break

                # Check if pointers meet → potential cycle
                if slow == fast:
                    # Check for single-element loop (not allowed)
                    if slow == next_index(slow):
                        break
                    return True   # Found a valid cycle

            # Mark all nodes visited in this path as 0
            marker = i
            while nums[marker] != 0 and (nums[marker] > 0) == direction:
                next_pos = next_index(marker)
                nums[marker] = 0   # Mark as visited
                marker = next_pos

        return False
