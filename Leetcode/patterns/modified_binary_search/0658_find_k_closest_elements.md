# Leetcode 658 - Find K Closest Elements

**Tags:** `Array`, `Binary Search`, `Sorting`, `Two Pointers`, `Sliding Window`

**Data Structures:** `Array`, `Sliding Window`

**Algorithms:** `Binary Search`, `Two Pointers`, `Custom Sorting`

## ☀️ UMPIRE

**Understand:** Given a sorted integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

**Match:** This is a modified binary search problem with sliding window optimization. The key insight is that the result must be a contiguous subarray since the input is sorted. We can either sort by distance, expand from insertion point, or binary search for optimal window position.

**Plan:**
1. Brute force: Sort by distance to x, take first k elements
2. Smart expansion: Find insertion point, expand k times toward closer elements  
3. Optimal search: Binary search for best sliding window start position
4. All approaches ensure tie-breaking favors smaller elements

**Implement:** See the code section below.

**Review:**
- Ensure tie-breaking logic (smaller elements preferred when distances are equal)
- Verify binary search correctly finds insertion point and window boundaries
- Handle edge cases like k equals array length or x outside array range

**Evaluate:**
- Time: O(n log n) for sorting, O(log n + k) for expansion, O(log(n-k)) for window search
- Space: O(1) for in-place operations (excluding output array)

## ☀️ Why This Is a Sliding Window + Binary Search Problem

The sorted array property creates crucial opportunities for optimization:
- **Contiguous result:** The k closest elements must form a contiguous subarray
- **Binary search applications:** Find insertion point or optimal window start efficiently
- **Distance comparison shortcuts:** Only need to compare window boundaries instead of all elements
- **Sliding window concept:** The optimal solution is a fixed-size window at the best position

Key insights:
- Sorting by distance works but ignores the pre-sorted structure
- Expansion from center leverages insertion point to grow optimally
- Window-based search compares only boundary elements for maximum efficiency
- All approaches must handle tie-breaking consistently

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `arr = [1,2,3,4,5], k = 4, x = 3` | Standard case | `[1,2,3,4]` |
| `arr = [1,2,3,4,5], k = 4, x = -1` | x smaller than all elements | `[1,2,3,4]` |
| `arr = [1,2,3,4,5], k = 4, x = 6` | x larger than all elements | `[2,3,4,5]` |
| `arr = [1,4,6,10,20], k = 3, x = 8` | x not in array, between elements | `[4,6,10]` |
| `arr = [0,1,2,2,2,3,4], k = 3, x = 2` | Multiple equal elements, x in array | `[1,2,2]` or `[2,2,2]` |
| `arr = [1], k = 1, x = 1` | Single element array | `[1]` |
| `arr = [1,3], k = 1, x = 2` | Tie-breaking scenario | `[1]` (smaller element) |

These test:
- Standard distance-based selection
- Boundary conditions (x outside array range)
- Tie-breaking with equal distances
- Arrays with duplicate elements
- Minimal input sizes

## ☀️ Code

### Solution 1: Sort by Distance (Brute Force Approach)
**Time: O(n log n) → Sort entire array by distance**  
**Space: O(1) → Only using constant extra space (excluding output)**

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sort by distance to x first, then by value for tie-breaking
        arr.sort(key=lambda num: (abs(num - x), num))
        
        # Take first k elements and sort them in ascending order
        return sorted(arr[:k])
```

### Solution 2: Binary Search + Two Pointers (Recommended for Interview)
**Time: O(log n + k) → Binary search to find insertion point + expand k times**  
**Space: O(1) → Only using constant extra space**

```python
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
```

### Solution 3: Binary Search for Sliding Window Start (Optimal)
**Time: O(log(n - k)) → Binary search on possible window starting positions**  
**Space: O(1) → Only using constant extra space**

```python
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
```

## ☀️ Notes

**Key Algorithm Components:**
- `(abs(num - x), num)` tuple sorting naturally handles distance and tie-breaking
- `bisect_left()` finds optimal insertion point in O(log n) time
- Two-pointer expansion considers boundary cases and distance comparisons
- Sliding window binary search compares only boundary elements for efficiency

**Critical Insight:**
The k closest elements must form a contiguous subarray in the sorted input. This transforms the problem from individual element selection to optimal subarray positioning.

## ☀️ Coding Walkthrough Script

I'll solve this by recognizing that the k closest elements must be contiguous in the sorted array.
My recommended approach is to first find where x would be inserted using binary search. This gives me the optimal starting point.
Then I'll expand outward k times, each time choosing the direction that gives me a closer element. I need to handle three cases: can only go left, can only go right, or compare both sides.
When comparing distances, if they're equal, I prefer the smaller element for tie-breaking.
For the most optimal solution, I can binary search for the best window starting position by comparing only the window boundaries, since adjacent windows differ by only one element at each end.

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Interview Notes |
|--------|----------------|------------------|--------------|-----------------|
| Sort by Distance | O(n log n) | O(1) | Custom sorting with tie-breaking | Quick to implement but inefficient |
| Binary Search + Expand | O(log n + k) | O(1) | **Recommended**; Find center, expand optimally | Best balance of clarity and efficiency |
| Sliding Window Search | O(log(n-k)) | O(1) | Advanced; Binary search for window position | Most optimal but complex to explain |

## ☀️ Binary Search + Expansion Insights

- **Prerequisite:** Array is sorted, allowing efficient insertion point location
- **Core insight:** Optimal region surrounds the insertion point for x
- **Expansion strategy:** Always choose the closer element, with tie-breaking toward smaller values
- **Boundary handling:** Gracefully handle cases where expansion hits array limits
- **Termination:** Stop when exactly k elements are selected

**Mathematical Guarantee:** Since elements are sorted and we start from the optimal insertion point, expanding toward closer elements ensures we collect the globally closest k elements.

## ☀️ Sliding Window Binary Search Insights

- **Prerequisite:** The optimal k elements form a contiguous subarray
- **Core insight:** Compare window boundaries to determine optimal shift direction
- **Decision making:** If left boundary is farther from x than right boundary, shift window right
- **Elimination principle:** Each comparison eliminates half the possible starting positions
- **Convergence:** Binary search finds the unique optimal window position

**Mathematical Guarantee:** The boundary comparison `x - arr[mid] > arr[mid + k] - x` correctly identifies when shifting the window right reduces total distance, ensuring convergence to the global optimum.

**Note:** Solution 1 provides a simple baseline but doesn't leverage the sorted property. 
Solution 2 is recommended for interviews due to its clear logic and good efficiency. 
Solution 3 achieves optimal time complexity and demonstrates advanced binary search applications.
