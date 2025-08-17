"""
Problem Statement:
You are given a sorted array consisting of only integers where every element appears 
exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,7,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
- nums.length is odd
- Every element appears exactly twice except for one element which appears exactly once
"""

from typing import List

# Solution 1: Linear Search (Naive Approach)
# Time: O(n) → May need to scan entire array
# Space: O(1) → Only using constant extra space
class Solution1:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Approach: Linear search to find the single element
        
        This approach is straightforward but doesn't meet the O(log n) requirement.
        Simply iterate through the array to find the element that appears only once.
        """
        # XOR approach - all paired elements cancel out
        result = 0
        for num in nums:
            result ^= num
        return result


# Solution 2: Binary Search with Index Parity Analysis (Optimal)
# Time: O(log n) → Binary search eliminates half search space each iteration
# Space: O(1) → Only using constant extra space
class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Approach: Binary search using index parity pattern
        
        Key Insight:
        - Before single element: pairs start at even indices [0,1], [2,3], [4,5]...
        - After single element: pairs start at odd indices [1,2], [3,4], [5,6]...
        - By checking if nums[even] == nums[even+1], we can determine search direction
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Ensure mid is even for consistent pattern checking
            if mid % 2 == 1:
                mid -= 1
            
            # Check if the pair starting at even index mid is complete
            if nums[mid] == nums[mid + 1]:
                # Pair is complete, single element must be on the right
                left = mid + 2
            else:
                # Pair is broken, single element is on the left (including mid)
                right = mid
        
        return nums[left]


# Solution 3: my Original Approach (Fixed) ---> just for backup, not recommend, please use the second one
# Time: O(log n) → Binary search eliminates half search space each iteration
# Space: O(1) → Only using constant extra space
class Solution3:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Your approach: Count remaining elements to determine search direction
        
        Logic: If one side has odd number of remaining elements, 
        the single element must be on that side.
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Check if mid is the single element (different from both neighbors)
            is_single = True
            if mid > 0 and nums[mid - 1] == nums[mid]:
                is_single = False
            if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                is_single = False
            
            if is_single:
                return nums[mid]
            
            # Check which neighbor mid matches
            if mid > 0 and nums[mid - 1] == nums[mid]:
                # mid matches left neighbor
                left_count = mid - 1  # Number of elements before the pair
                if left_count % 2 == 1:
                    # Odd number on left, single element is on left
                    right = mid - 1
                else:
                    # Even number on left, single element is on right
                    left = mid + 1
            else:
                # mid matches right neighbor (nums[mid] == nums[mid + 1])
                right_count = len(nums) - 1 - (mid + 1)  # Elements after the pair
                if right_count % 2 == 1:
                    # Odd number on right, single element is on right
                    left = mid + 2
                else:
                    # Even number on right, single element is on left
                    right = mid - 1
        
        return nums[left]


# Solution 4: XOR with Index Technique
# Time: O(log n) → Binary search eliminates half search space each iteration
# Space: O(1) → Only using constant extra space
class Solution4:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Elegant approach: Use XOR to find pair partner
        
        For any index i:
        - If i is even: partner is at i+1
        - If i is odd: partner is at i-1
        This can be computed as i^1 (XOR with 1)
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Find partner index using XOR trick
            partner = mid ^ 1
            
            if nums[mid] == nums[partner]:
                # Pair is complete, single element is on the right
                left = mid + 1
            else:
                # Pair is broken, single element is on the left (including mid)
                right = mid
        
        return nums[left]

"""
Key Insights and Takeaways:

1. Problem Classification:
   - Modified binary search with parity analysis
   - Finding disruption in paired element pattern
   - Guaranteed exactly one single element

2. Core Technique - Index Parity Analysis:
   - Before single element: pairs start at even indices
   - After single element: pairs start at odd indices
   - Check nums[even] == nums[even+1] to determine search direction

3. Multiple Valid Approaches:
   - Solution 2: Standard index parity method (most common)
   - Solution 3: Your counting approach (equally valid)
   - Solution 4: XOR index technique (most elegant)

4. Template Recognition:
   - This is a "parity analysis" template
   - Used when array has repeating patterns that get disrupted
   - Key: identify the pattern, find the disruption

5. Why This Works:
   - Single element disrupts the pairing pattern
   - Parity analysis gives monotonic decision for binary search
   - Each comparison eliminates exactly half the search space

6. Interview Strategy:
   - Start with Solution 1 to show understanding
   - Mention O(log n) requirement
   - Implement Solution 2 or your approach (Solution 3)
   - Explain the parity pattern clearly

7. Common Mistakes to Avoid:
   - Boundary checking when accessing nums[mid±1]
   - Understanding that both approaches use same mathematical principle
   - Remember to use while left < right for position convergence

8. Related Problems:
   - Problems with repeating patterns that get disrupted
   - Any problem requiring parity analysis
   - Finding anomalies in structured arrays

9. Template Value:
   - Parity analysis is a distinct binary search template
   - Useful for pattern disruption problems
   - Combines mathematical insight with binary search efficiency
"""
