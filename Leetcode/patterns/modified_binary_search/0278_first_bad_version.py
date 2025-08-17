# LeetCode 278: First Bad Version
# https://leetcode.com/problems/first-bad-version/

"""
Problem Statement:
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
- 1 <= bad <= n <= 2^31 - 1
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Solution 1: Linear Search (Naive Approach)
# Time: O(n) → May need to check every version
# Space: O(1) → Only using constant extra space
class Solution1:
    def firstBadVersion(self, n: int) -> int:
        """
        Approach: Linear search from version 1 to n
        
        This approach is straightforward but inefficient.
        It doesn't utilize the sorted property of the problem.
        Used here to demonstrate the basic idea before optimization.
        """
        for version in range(1, n + 1):
            if isBadVersion(version):
                return version
        
        # This should never happen given problem constraints
        return n


# Solution 2: Binary Search with Left Boundary Template (Optimal)
# Time: O(log n) → Binary search eliminates half search space each iteration
# Space: O(1) → Only using constant extra space
class Solution2:
    def firstBadVersion(self, n: int) -> int:
        """
        Approach: Binary search to find the first bad version
        
        Key Insight:
        - This is a left boundary search problem
        - We want to find the leftmost (first) bad version
        - Use the same template as LeetCode 34 (Find First and Last Position)
        - When we find a bad version, continue searching left for earlier bad versions
        """
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2  # Prevent overflow
            
            if isBadVersion(mid):
                # Found a bad version, but search left for the first one
                right = mid - 1
            else:
                # Current version is good, first bad version is to the right
                left = mid + 1
        
        # When loop ends, left points to the first bad version
        return left


# Solution 3: Alternative Binary Search Template
# Time: O(log n) → Binary search eliminates half search space each iteration  
# Space: O(1) → Only using constant extra space
class Solution3:
    def firstBadVersion(self, n: int) -> int:
        """
        Alternative binary search template using while left < right
        
        Note: This template requires different boundary handling
        """
        left, right = 1, n
        
        while left < right:  # No equal sign
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # mid might be the first bad version, so don't exclude it
                right = mid  # Not mid - 1
            else:
                # mid is definitely not the first bad version
                left = mid + 1
        
        # When loop ends, left == right, pointing to first bad version
        return left


# Solution 4: Binary Search with Recording (Consistent with LeetCode 34 style)
# Time: O(log n) → Binary search eliminates half search space each iteration
# Space: O(1) → Only using constant extra space  
class Solution4:
    def firstBadVersion(self, n: int) -> int:
        """
        Binary search with explicit recording of found bad versions
        This style is consistent with LeetCode 34 approach
        """
        left, right = 1, n
        first_bad = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                first_bad = mid  # Record this bad version
                right = mid - 1  # Continue searching left for earlier ones
            else:
                left = mid + 1   # Search right for bad versions
        
        return first_bad


"""
Key Insights and Takeaways:

1. Problem Classification:
   - This is a left boundary search problem
   - Similar to finding the first occurrence in LeetCode 34
   - Requires binary search for optimal O(log n) solution

2. Core Technique - Left Boundary Binary Search:
   - When isBadVersion(mid) is True: search left (right = mid - 1)
   - When isBadVersion(mid) is False: search right (left = mid + 1)
   - The pattern is: find the transition point from good to bad

3. Template Consistency:
   - Recommended to use same template as LeetCode 34 boundary search
   - while left <= right provides consistent logic
   - return left at the end (points to first bad version)

4. Why This Works:
   - Array is conceptually: [good, good, ..., good, bad, bad, ..., bad]
   - We're finding the first position where condition becomes true
   - Binary search efficiently narrows down to the boundary

5. Interview Strategy:
   - Start with Solution 1 to show understanding
   - Mention API call minimization requirement
   - Implement Solution 2 as optimal approach
   - Explain the boundary search logic clearly

6. Common Mistakes to Avoid:
   - Don't use different templates inconsistently
   - Remember to handle integer overflow with (right - left) // 2
   - Don't confuse this with standard binary search (we're finding boundary)

7. Related Problems:
   - LeetCode 34: Find First and Last Position (boundary search)
   - LeetCode 35: Search Insert Position (insertion point)
   - LeetCode 69: Sqrt(x) (finding boundary of valid values)
   - LeetCode 875: Koko Eating Bananas (binary search on answer space)

8. Template Choice:
   - Solution 2 (while left <= right) is recommended for consistency
   - Works well with other boundary search problems
   - Clear logic: continue searching even after finding a bad version
"""
