# Leetcode 1337 - The K Weakest Rows in a Matrix

## ☀️ UMPIRE

**Understand:** You are given an `m x n` binary matrix `mat` of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians in each row. A row i is weaker than a row j if one of the following is true: (1) The number of soldiers in row i is less than the number of soldiers in row j, or (2) Both rows have the same number of soldiers and i < j. Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

**Match:** This is a sorting/heap problem with optimization opportunities. We can use counting + sorting, binary search + heap, or maintain a fixed-size heap for space efficiency. The key insight is leveraging the binary nature of rows (soldiers followed by civilians) for efficient counting.

**Plan:**
1. Count soldiers in each row (can optimize with binary search)
2. Sort rows by strength (soldier count, then by index)
3. Return first k row indices
4. Alternative: Use heap-based approaches for better space complexity when k << m

**Implement:** See the code section below.

**Review:**
- Ensure proper tie-breaking (lower index wins when soldier counts are equal)
- Verify binary search correctly finds the boundary between 1's and 0's
- Handle edge cases like all 1's or all 0's in rows

**Evaluate:**
- Time: O(m * n + m log m) for basic approach, O(m * log n + k log m) with binary search
- Space: O(m) for basic approach, O(k) for heap-optimized version

## ☀️ Why This Is a Counting and Sorting Problem

The problem requires ranking rows by "weakness" which naturally leads to sorting:
- **Counting phase:** Determine each row's strength (number of soldiers)
- **Ranking phase:** Sort by strength with tie-breaking rules
- **Selection phase:** Extract the k weakest rows

Key insights:
- Binary matrix structure allows binary search optimization for counting
- Tie-breaking rule (lower index wins) is naturally handled by stable sorting
- Heap can optimize space complexity when k is much smaller than m
- The "weakness" metric creates a total ordering of rows

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], k = 3` | Standard case | `[2,0,3]` |
| `mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], k = 2` | Multiple rows with same strength | `[0,2]` (index tie-breaking) |
| `mat = [[1,1,1],[1,1,1],[1,1,1]], k = 1` | All rows have same strength | `[0]` (first row wins) |
| `mat = [[0,0,0],[0,0,0],[0,0,0]], k = 2` | No soldiers in any row | `[0,1]` (index order) |
| `mat = [[1],[0]], k = 1` | Minimal matrix | `[1]` (0 soldiers < 1 soldier) |
| `mat = [[1,1,1,1,1]], k = 1` | Single row | `[0]` |

These test:
- Standard ranking scenarios
- Tie-breaking with identical soldier counts
- Extreme cases (all same, no soldiers)
- Minimal input sizes
- Single row edge case

## ☀️ Code

### Solution 1: Count + Sort (Standard Approach)
**Time: O(m * n + m * log m) → Count soldiers in each row + sort by strength**  
**Space: O(m) → Store strength info for each row**

```python
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
```

### Solution 2: Binary Search + Min Heap (Optimized Counting)
**Time: O(m * log n + k * log m) → Binary search for each row + heap operations**  
**Space: O(m) → Store in heap**

```python
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
```

### Solution 3: Binary Search + Max Heap (Space Optimized)
**Time: O(m * log n + m * log k) → Binary search + maintain heap of size k**  
**Space: O(k) → Only store k elements in heap**

```python
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
```

## ☀️ Notes

**Key Algorithm Components:**
- `sum(mat[i])` provides O(n) counting for each row
- Binary search reduces counting to O(log n) by finding first 0
- Tuple sorting `(soldier_count, row_index)` naturally handles tie-breaking
- Max heap with size k maintains space efficiency when k << m

**Critical Insight:**
The binary structure of rows (1's followed by 0's) allows binary search optimization. The tie-breaking rule aligns perfectly with lexicographic tuple ordering.

## ☀️ Coding Walkthrough Script

I'll solve this by counting soldiers and ranking rows by weakness.
First, I need to count soldiers in each row. Since soldiers come before civilians, I can either sum the 1's or use binary search to find where 1's end.
For each row, I'll store both the soldier count and row index as a tuple. This is crucial for tie-breaking - when soldier counts are equal, the lower index should win.
I sort these tuples, which naturally sorts by soldier count first, then by index. This gives me the weakness ranking.
Finally, I extract the first k row indices from the sorted list.
For optimization, I can use binary search to count soldiers in O(log n) instead of O(n), especially beneficial when columns are numerous.
For space optimization when k is small, I can maintain a max heap of size k, keeping only the k weakest rows discovered so far."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Linear Count + Sort | O(m * n + m log m) | O(m) | Count all soldiers, sort all rows | Simple and intuitive |
| Binary Search + Sort | O(m * log n + m log m) | O(m) | Binary search for counting | Better when n is large |
| Binary Search + Min Heap | O(m * log n + k log m) | O(m) | Heap for k smallest | Good for extracting top-k |
| Binary Search + Max Heap | O(m * log n + m log k) | O(k) | **Recommended**; Space optimal when k << m |

## ☀️ Binary Search Counting Insights

- **Prerequisite:** Soldiers (1's) come before civilians (0's) in each row
- **Core insight:** Find the boundary between 1's and 0's using binary search
- **Search target:** First position where value is 0
- **Termination:** When left == right, left points to first 0 (or end if all 1's)
- **Count formula:** The boundary position equals the soldier count
- **Edge cases:** All soldiers (boundary at end) or no soldiers (boundary at start)

**Mathematical Guarantee:** Binary search on the monotonic 1,1,1...1,0,0,0...0 pattern will find the transition point in O(log n) time, giving us the soldier count directly.

**Note:** Solution 1 is the most straightforward for understanding the core algorithm. 
Solution 2 optimizes counting with binary search, useful for wide matrices. 
Solution 3 provides space optimization crucial when k is much smaller than m, making it the recommended approach for large-scale problems.
