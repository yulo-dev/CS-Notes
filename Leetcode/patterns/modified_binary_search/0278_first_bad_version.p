Solution 1: Binary Search (Lower Bound Template)
Time: O(log n) → We eliminate half of the search space in each iteration
Space: O(1) → Only using constant extra space for pointers

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # First bad version is at mid or before mid
                right = mid
            else:
                # First bad version is after mid
                left = mid + 1
        
        # When left == right, we found the first bad version
        return left


Solution 2: Binary Search with Record and Continue (Alternative Approach)
Time: O(log n) → Same time complexity but may require more iterations
Space: O(1) → Only using constant extra space for pointers

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Find the first bad version using binary search with an 'ans' variable.
        - Keep a candidate 'ans' whenever we see a bad version.
        - Then continue searching on the left side to ensure it's the first bad.
        
        Time Complexity:  O(log n)
        Space Complexity: O(1)
        """
        left, right = 1, n
        ans = n  # Problem guarantees there is at least one bad version.

        while left <= right:
            # Middle index; avoids overflow in languages with fixed int width
            mid = left + (right - left) // 2

            # Call the API exactly once per loop and store the result
            bad = isBadVersion(mid)

            if bad:
                # mid is a bad version; it could be the first bad
                ans = mid
                # Exclude mid and everything to its right; continue searching left
                right = mid - 1
            else:
                # mid is good; the first bad must be to the right
                left = mid + 1

        return ans


# Note: Solution 1 is the most recommended approach using the while left < right template, which is optimal for finding "the first position that satisfies a condition". 
Solution 2 demonstrates a "record and continue" strategy but typically requires more iterations. Use Solution 1 in interviews for better efficiency.
