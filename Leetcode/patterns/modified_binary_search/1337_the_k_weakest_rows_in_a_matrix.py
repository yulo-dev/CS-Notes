# LeetCode 1337: The K Weakest Rows in a Matrix
# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). 
# The soldiers are positioned in front of the civilians in each row.
# A row i is weaker than a row j if one of the following is true:
# - The number of soldiers in row i is less than the number of soldiers in row j.
# - Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

# Solution 1: Count + Sort
# Time: O(m * n + m * log m) → Count soldiers in each row + sort by strength
# Space: O(m) → Store strength info for each row
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Count soldiers in each row and store with row index
        rows_strength = []
        
        for i in range(len(mat)):
            soldier_count = sum(mat[i])  # Count 1's in the row
            rows_strength.append((soldier_count, i))
        
        # Sort by soldier count first, then by row index
        # This automatically handles the tie-breaking rule
        rows_strength.sort()
        
        # Extract the first k row indices
        return [row_index for _, row_index in rows_strength[:k]]

# Solution 2: Binary Search + Heap
# Time: O(m * log n + k * log m) → Binary search for each row + heap operations
# Space: O(m) → Store in heap
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def count_soldiers(row):
            # Use binary search to find the first 0 (end of soldiers)
            left, right = 0, len(row)
            while left < right:
                mid = left + (right - left) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        # Use min heap to store (soldier_count, row_index)
        heap = []
        
        for i in range(len(mat)):
            soldier_count = count_soldiers(mat[i])
            heapq.heappush(heap, (soldier_count, i))
        
        # Extract k weakest rows
        result = []
        for _ in range(k):
            _, row_index = heapq.heappop(heap)
            result.append(row_index)
        
        return result

# Solution 3: Optimized with Max Heap (Space Efficient)
# Time: O(m * log n + m * log k) → Binary search + maintain heap of size k
# Space: O(k) → Only store k elements in heap
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def count_soldiers(row):
            # Binary search to count soldiers efficiently
            left, right = 0, len(row)
            while left < right:
                mid = left + (right - left) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        # Use max heap to keep only k weakest rows
        # Store as (-soldier_count, -row_index) for max heap behavior
        max_heap = []
        
        for i in range(len(mat)):
            soldier_count = count_soldiers(mat[i])
            
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-soldier_count, -i))
            else:
                # If current row is weaker than the strongest in heap
                if (-soldier_count, -i) > max_heap[0]:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-soldier_count, -i))
        
        # Extract results and reverse to get weakest to strongest order
        result = []
        while max_heap:
            soldier_count, row_index = heapq.heappop(max_heap)
            result.append(-row_index)
        
        return result[::-1]  # Reverse to get correct order

# Note: 
# Solution 1 is the most straightforward and easy to understand.
# Solution 2 uses binary search for counting but still processes all rows.
# Solution 3 is most space-efficient when k << m, maintaining only k elements in memory.
# The binary search optimization in Solutions 2&3 is particularly useful when rows are long,
# as it reduces the counting step from O(n) to O(log n) per row.
