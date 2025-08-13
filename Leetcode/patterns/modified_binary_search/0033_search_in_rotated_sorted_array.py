# Solution 1: Binary Search with Ordered Side Detection 
# Time: O(log n) → We eliminate half of the search space in each iteration
# Space: O(1) → Only using constant extra space for pointers

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            
            # Determine which side is ordered
            if nums[left] <= nums[mid]:
                # Left side is ordered
                if nums[left] <= target < nums[mid]:
                    # Target is in the ordered left side
                    right = mid - 1
                else:
                    # Target is in the right side (may cross rotation point)
                    left = mid + 1
            else:
                # Right side is ordered
                if nums[mid] < target <= nums[right]:
                    # Target is in the ordered right side
                    left = mid + 1
                else:
                    # Target is in the left side (may cross rotation point)
                    right = mid - 1
        
        # Target not found
        return -1


      
# Solution 2: Binary Search with Rotation Point Analysis (進階解法)
# Time: O(log n) → Same time complexity but more explicit logic
# Space: O(1) → Only using constant extra space for pointers

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            
            # Check if left side has no rotation (is sorted)
            if nums[left] <= nums[mid]:
                # Left side is sorted normally
                if target >= nums[left] and target < nums[mid]:
                    # Target lies within the sorted left portion
                    right = mid - 1
                else:
                    # Target must be in right portion (which may contain rotation)
                    left = mid + 1
            else:
                # Right side is sorted normally (left side contains rotation)
                if target > nums[mid] and target <= nums[right]:
                    # Target lies within the sorted right portion
                    left = mid + 1
                else:
                    # Target must be in left portion (which contains rotation)
                    right = mid - 1
        
        return -1


# Note: Solution 1 is the most recommended approach using clear logical conditions to identify the ordered side. 
# Solution 2 provides more explicit comments about rotation analysis but follows the same core logic. 
# Both solutions efficiently handle the rotation by leveraging the fact that at least one side is always completely sorted.
