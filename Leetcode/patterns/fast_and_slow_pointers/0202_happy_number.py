# solution 1: Hash Set (Straightforward Approach)
# time complexity: O(log n) (number quickly shrinks to < 243 → finite states)
# space complexity:

class Solution:
    def isHappy(self, n: int) -> bool:
        # Helper function to calculate the sum of squares of digits
        def get_sum(num):
            total = 0
            while num > 0:
                num, digit = divmod(num, 10)  # Extract last digit
                total += digit * digit        # Add square of digit to total
            return total

        seen = set()  # Store numbers we have seen to detect loops

        # Repeat until we reach 1 (happy number) or detect a cycle
        while n != 1 and n not in seen:
            seen.add(n)        # Mark current number as seen
            n = get_sum(n)     # Move to next number

        return n == 1          # True if happy number, False if cycle detected

      
# solution 2: Fast & Slow Pointers (Floyd’s Cycle Detection)
# time complexity: O(log n) (same shrinking property)
# space complexity: O(1) (no extra memory for seen numbers)

class Solution:
    def isHappy(self, n: int) -> bool:
        # Helper function to calculate the sum of squares of digits
        def get_sum(num):
            total = 0
            while num > 0:
                num, digit = divmod(num, 10)  # Extract last digit
                total += digit * digit        # Add square of digit to total
            return total

        slow = n              # Slow pointer moves one step
        fast = get_sum(n)     # Fast pointer moves two steps

        # Loop until fast reaches 1 (happy number) or pointers meet (cycle detected)
        while fast != 1 and slow != fast:
            slow = get_sum(slow)               # Move one step
            fast = get_sum(get_sum(fast))      # Move two steps

        return fast == 1      # True if happy number, False if cycle detected
