# Leetcode 0074 - Search a 2D Matrix

## ☀️ UMPIRE

**Understand:** Write an efficient algorithm that searches for a value target in an m x n integer matrix. This matrix has the following properties:
- Integers in each row are sorted from left to right
- The first integer of each row is greater than the last integer of the previous row
- **You must write a solution in O(log(m * n)) time complexity**

**Match:** This is a Modified Binary Search problem. The key insight is that the entire matrix can be treated as a single sorted array when read row by row, allowing us to apply binary search on the "virtual" 1D representation.

**Plan:**
1. Recognize that the matrix is globally sorted when flattened
2. Use binary search on the virtual 1D array (indices 0 to m*n-1)
3. Convert 1D indices to 2D coordinates using mathematical transformation
4. Apply standard binary search logic

**Implement:** See the code section below.

**Review:**
- Ensure we meet the O(log(m*n)) time complexity requirement
- Verify coordinate transformation logic (row = mid // n, col = mid % n)
- Handle edge cases like empty matrix and single element

**Evaluate:**
- Time: O(log(m*n)) - single binary search on entire matrix
- Space: O(1) - only using constant extra space

## ☀️ Why This Is a Modified Binary Search Problem

The matrix has special properties that make it globally sorted:
- **Each row is individually sorted**
- **The last element of each row < first element of next row**
- This creates a **global ordering** when read row by row
- We can treat the 2D structure as a **virtual 1D sorted array**
- Standard binary search can be applied with coordinate transformation

Key insights:
- Don't think row-by-row; think globally sorted
- The 1D index to 2D coordinate conversion is the crucial technique
- This transforms a 2D problem into a familiar 1D binary search

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]], target = 5` | Target exists | `true` |
| `matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]], target = 20` | Target doesn't exist | `false` |
| `matrix = [[1]], target = 1` | Single element, found | `true` |
| `matrix = [[1]], target = 2` | Single element, not found | `false` |
| `matrix = [], target = 1` | Empty matrix | `false` |
| `matrix = [[]], target = 1` | Empty rows | `false` |

These test:
- Normal search scenarios
- Boundary elements (first, last)
- Single element matrices
- Empty input validation
- Non-existent targets

## ☀️ Code

### Solution 1: Row-by-Row Binary Search (Intuitive Approach)
**Time: O(m × log n) → Binary search on each row individually**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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
```

### Solution 2: 1D Binary Search (Optimal Approach)
**Time: O(log(m × n)) → Single binary search on entire matrix**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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
                left = mid + 1  # Search right half
            else:
                right = mid - 1  # Search left half
        
        return False
```

### Alternative: Pythonic Version with divmod
**Time: O(log(m × n)) → Same complexity but more elegant**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Use divmod for coordinate conversion
            row, col = divmod(mid, n)
            mid_value = matrix[row][col]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
```

## ☀️ Notes

**Key Algorithm Components:**
- **Coordinate transformation**: `row = mid // n`, `col = mid % n`
- **Virtual 1D indexing**: Treat matrix as array with indices [0, m*n-1]
- **Standard binary search**: Apply normal binary search logic on virtual array
- **Edge case handling**: Check for null and empty matrices

**Critical Insight:**
The algorithm works because the matrix maintains global ordering when read row by row. The coordinate transformation allows us to map any 1D index to its corresponding 2D position, enabling binary search on the entire matrix as if it were a single sorted array.

## ☀️ Coordinate Transformation Explained

```
Matrix:          Virtual 1D Array:
[1,  4,  7, 11]  [1, 4, 7, 11, 2, 5, 8, 12, 3, 6, 9, 16, 10, 13, 14, 17]
[2,  5,  8, 12]   0  1  2   3  4  5  6   7  8  9 10  11  12  13  14  15
[3,  6,  9, 16]
[10,13, 14, 17]

Index 6 (value 8): row = 6 // 4 = 1, col = 6 % 4 = 2 → matrix[1][2] = 8
Index 13 (value 13): row = 13 // 4 = 3, col = 13 % 4 = 1 → matrix[3][1] = 13
```

## ☀️ Coding Walkthrough Script

I need to search in a 2D matrix with special sorting properties. Let me analyze the constraints first.
The matrix is sorted both within rows and between rows, which means if I read it row by row, I get a completely sorted sequence. This suggests I can treat it as a 1D sorted array and apply binary search.
I'll use binary search on indices from 0 to m*n-1, where m and n are the matrix dimensions. The key is converting 1D indices back to 2D coordinates.
For any 1D index 'mid', I can find the corresponding row and column using integer division: row = mid // n and col = mid % n. This works because each row has exactly n elements.
I'll initialize left=0 and right=m*n-1, then apply standard binary search. At each step, I convert the middle index to 2D coordinates, get the value, and compare with target.
If the middle value equals target, I return true. If it's less than target, I search the right half by setting left=mid+1. Otherwise, I search the left half by setting right=mid-1.
This approach gives me O(log(m*n)) time complexity, which meets the problem requirement.

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Row-by-Row Search | O(m × log n) | O(1) | Binary search each row | Simple but doesn't meet requirement |
| 1D Binary Search | O(log(m×n)) | O(1) | Treat as virtual 1D array | **Optimal**; meets requirement |
| Linear Search | O(m × n) | O(1) | Check every element | Too slow for large matrices |

## ☀️ 1D Binary Search Insights

- **Prerequisites:** Matrix sorted within rows and between rows
- **Core insight:** Global ordering enables virtual 1D representation
- **Coordinate mapping:** Mathematical transformation between 1D and 2D indices
- **Standard binary search:** Apply familiar algorithm on transformed space
- **Efficiency gain:** Single search vs multiple row searches
- **Requirement satisfaction:** Meets O(log(m×n)) constraint

**Mathematical Guarantee:** Since the matrix maintains global ordering when flattened, binary search on the virtual 1D array will correctly locate any existing element or determine its absence in logarithmic time.

**Note:** Solution 1 demonstrates basic understanding but doesn't meet the time complexity requirement. Solution 2 is the optimal approach that fully utilizes the matrix's ordering properties. The coordinate transformation technique is widely applicable in 2D matrix problems.
