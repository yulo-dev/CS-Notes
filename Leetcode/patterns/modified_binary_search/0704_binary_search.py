
# Solution 1: Iterative Binary Search
# Time: O(log n) → We eliminate half of the search space in each iteration
# Space: O(1) → Only using constant extra space for pointers

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers
        left, right = 0, len(nums) - 1
        
        # Continue searching while search space is valid
        while left <= right:
            # Calculate middle index to avoid overflow
            mid = left + (right - left) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            # Target is in the right half
            elif nums[mid] < target:
                left = mid + 1
            # Target is in the left half
            else:
                right = mid - 1
        
        # Target not found in the array
        return -1


# Solution 2: Recursive Binary Search
# Time: O(log n) → Each recursive call eliminates half of the search space
# Space: O(log n) → Recursion stack depth is log n

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            # Base case: search space is invalid
            if left > right:
                return -1
            
            # Calculate middle index
            mid = left + (right - left) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            # Search in the right half
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            # Search in the left half
            else:
                return binary_search(left, mid - 1)
        
        # Start the recursive search
        return binary_search(0, len(nums) - 1)


Note: Solution 1 (Iterative) is generally preferred due to O(1) space complexity, 
while Solution 2 (Recursive) is more intuitive but uses O(log n) space due to recursion stack.
