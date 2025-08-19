# LeetCode 658: Find K Closest Elements
# Given a sorted integer array arr, two integers k and x, 
# return the k closest integers to x in the array. 
# The result should also be sorted in ascending order.
# If there is a tie, the smaller elements are always preferred.

# Solution 1: Sort by Distance (Brute Force)
# Time: O(n log n) → Sort entire array by distance
# Space: O(1) → Only using constant extra space (excluding output)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sort by distance to x first, then by value for tie-breaking
        arr.sort(key=lambda num: (abs(num - x), num))
        
        # Take first k elements and sort them in ascending order
        return sorted(arr[:k])

# Solution 2: Binary Search + Two Pointers (Expand from Center)
# Time: O(log n + k) → Binary search to find insertion point + expand k times
# Space: O(1) → Only using constant extra space
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Find the insertion position for x
        left = bisect.bisect_left(arr, x)
        right = left
        
        # Expand from center to find k closest elements
        for _ in range(k):
            if left == 0:
                # Can only expand right
                right += 1
            elif right == len(arr):
                # Can only expand left
                left -= 1
            elif x - arr[left - 1] <= arr[right] - x:
                # Left element is closer or equal (prefer smaller)
                left -= 1
            else:
                # Right element is closer
                right += 1
        
        return arr[left:right]

# Solution 3: Binary Search for Sliding Window Start (Optimal)
# Time: O(log(n - k)) → Binary search on possible window starting positions
# Space: O(1) → Only using constant extra space
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Compare distances from window boundaries to x
            # If left boundary is farther than right boundary, move window right
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left + k]


# Note: Solution 1 is straightforward but inefficient for large arrays.
# Solution 2 leverages the sorted property with expansion from optimal insertion point.
# Solution 3 is the most efficient, using binary search to find optimal sliding window.
