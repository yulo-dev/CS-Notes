
"""
Problem Statement:
Write an efficient algorithm that searches for a value target in an m x n integer matrix.
This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

You must write a solution in O(log(m * n)) time complexity.

Example:
Input: matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]], target = 5
Output: true

Input: matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]], target = 20
Output: false
"""

from typing import List

# Solution 1: Row-by-Row Binary Search (Intuitive but not optimal)
# Time: O(m * log n) → Search each row with binary search
# Space: O(1) → Only using constant extra space
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Binary search on each row individually
        
        Intuition:
        - Since each row is sorted, we can apply binary search on each row
        - This is a straightforward approach but doesn't fully utilize the global ordering
        
        Note: This solution doesn't meet the O(log(m*n)) requirement
        """
        if not matrix or not matrix[0]:
            return False
        
        # Search each row using binary search
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[0]) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    left = mid + 1  # Target is in right half
                else:
                    right = mid - 1  # Target is in left half
        
        return False


# Solution 2: Treat 2D Matrix as 1D Array (Optimal)
# Time: O(log(m * n)) → Single binary search on entire matrix
# Space: O(1) → Only using constant extra space
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Treat the 2D matrix as a sorted 1D array
        
        Key Insight:
        - The matrix is globally sorted when read row by row
        - We can perform binary search on the "virtual" 1D array
        - Convert 1D index to 2D coordinates using: row = mid // n, col = mid % n
        
        This approach meets the O(log(m*n)) time complexity requirement
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Convert 1D index to 2D coordinates
            row = mid // n
            col = mid % n
            mid_value = matrix[row][col]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1  # Search right half of virtual 1D array
            else:
                right = mid - 1  # Search left half of virtual 1D array
        
        return False


# Alternative Solution 2 (using divmod for more Pythonic code)
class Solution2_Pythonic:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Same approach as Solution2 but using divmod for coordinate conversion
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Use divmod for more Pythonic coordinate conversion
            row, col = divmod(mid, n)
            mid_value = matrix[row][col]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


# Most concise version
class Solution2_Concise:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Most concise version - direct indexing without intermediate variables
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = matrix[mid // n][mid % n]  # Direct coordinate conversion
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
