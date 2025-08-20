# Binary Search — Patterns Summary

This guide consolidates common **Binary Search** patterns you'll see across LeetCode. It teaches you **when to use which pattern**, **how to recognize** the right approach, core **tips/pitfalls**, a short **template**, and **example problems** you've solved.

---

## Pattern 1 — Standard Binary Search (Find Target Value)

### When to Use
- You're given a **sorted array** and need to find a **specific target value**.
- Classic "search for exact match" scenario.

### How to Recognize
- Input is a sorted array.
- Looking for exact target value or checking if target exists.
- Return index of target or -1 if not found.

### Tips / Pitfalls
- Use `while left <= right` (includes equality).
- Always eliminate `mid` in each iteration (`left = mid + 1` or `right = mid - 1`).
- Handle not found case by returning -1.

### Template
```python
def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # not found
```

### Problems
- **0704 – Binary Search**

---

## Pattern 2 — Search Insert Position (Find Left Boundary)

### When to Use
- Find the **first position** where target should be inserted to maintain sorted order.
- Looking for "first position >= target".

### How to Recognize
- Need to find insertion point.
- Return position even if target doesn't exist.
- Looking for leftmost valid position.

### Tips / Pitfalls
- Use `while left < right` (no equality).
- When condition met: `right = mid` (keep mid as potential answer).
- When condition not met: `left = mid + 1` (exclude mid).
- Final answer is always `left`.

### Template
```python
def searchInsert(nums, target):
    left, right = 0, len(nums)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    
    return left
```

### Problems
- **0035 – Search Insert Position**

---

## Pattern 3 — Rotated Array Search (Pattern Disruption)

### When to Use
- Searching in a **rotated sorted array**.
- Array was originally sorted but rotated at some unknown pivot.

### How to Recognize
- Array description mentions "rotated" or "shifted".
- Still need O(log n) solution despite rotation.
- Need to identify which half is properly sorted.

### Tips / Pitfalls
- Check which half is sorted using `nums[left] <= nums[mid]`.
- Only make range comparisons on the sorted half.
- Use elimination principle: if target not in sorted half, must be in other half.

### Template
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

### Problems
- **0033 – Search in Rotated Sorted Array**
- **0081 – Search in Rotated Sorted Array II** (with duplicates)

---

## Pattern 4 — Find First and Last Position (Boundary Search)

### When to Use
- Find the **range** of positions where target appears.
- Need both leftmost and rightmost occurrence of target.

### How to Recognize
- Asked for "first and last position" or "range" of target.
- Target may appear multiple times.
- Return `[-1, -1]` if target doesn't exist.

### Tips / Pitfalls
- Use two separate binary searches: one for left boundary, one for right boundary.
- Left boundary: find first position >= target.
- Right boundary: find first position > target, then subtract 1.

### Template
```python
def searchRange(nums, target):
    def findLeft(nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
    
    def findRight(nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left - 1
    
    left_idx = findLeft(nums, target)
    if left_idx >= len(nums) or nums[left_idx] != target:
        return [-1, -1]
    
    right_idx = findRight(nums, target)
    return [left_idx, right_idx]
```

### Problems
- **0034 – Find First and Last Position of Element in Sorted Array**

---

## Pattern 5 — 2D Matrix Search (Coordinate Transformation)

### When to Use
- Searching in a **2D matrix** with sorted properties.
- Matrix is sorted row-wise and column-wise, or can be treated as 1D sorted array.

### How to Recognize
- 2D matrix input with sorting guarantees.
- Need O(log(m*n)) or O(log(min(m,n))) solution.
- Can treat matrix as flattened sorted array.

### Tips / Pitfalls
- Convert 2D coordinates to 1D index: `index = row * cols + col`.
- Convert 1D index back to 2D: `row = index // cols`, `col = index % cols`.
- Choose search space carefully (top-right or bottom-left for staircase search).

### Template
```python
# Approach 1: Treat as 1D array
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        mid_val = matrix[mid // n][mid % n]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False
```

### Problems
- **0074 – Search a 2D Matrix**

---

## Pattern 6 — Pattern Disruption Analysis (Find Anomaly)

### When to Use
- Array has a **repeating pattern** that gets disrupted at one point.
- Need to find where the pattern breaks.

### How to Recognize
- Array has pairs or patterns that are consistent except for one disruption.
- Usually involves **parity analysis** or **index relationships**.
- Looking for the "odd one out" or disruption point.

### Tips / Pitfalls
- Analyze the pattern before and after the disruption.
- Use index parity (even/odd) to guide search direction.
- Make sure to adjust `mid` to maintain pattern consistency.

### Template
```python
def singleNonDuplicate(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # Ensure mid is even for consistent pattern checking
        if mid % 2 == 1:
            mid -= 1
        
        # Check if pair at even index is complete
        if nums[mid] == nums[mid + 1]:
            # Pattern intact, single element on right
            left = mid + 2
        else:
            # Pattern broken, single element on left
            right = mid
    
    return nums[left]
```

### Problems
- **0540 – Single Element in a Sorted Array**

---

## Pattern 7 — Binary Search on Answer (BSOA)

### When to Use
- **Optimization problems** where you need to find maximum/minimum value satisfying constraints.
- Can easily check if a given value is feasible, but direct calculation is hard.

### How to Recognize
- Asks for "maximum/minimum value" subject to constraints.
- Has **monotonic property**: if x works, then x+1/x-1 might also work.
- Easier to verify feasibility than to calculate directly.

### Tips / Pitfalls
- Define answer search space clearly.
- Write efficient feasibility check function.
- Choose correct boundary template: upper bound for maximum, lower bound for minimum.
- Upper bound search needs `mid = left + (right - left + 1) // 2` to avoid infinite loop.

### Template
```python
# Template for finding maximum feasible value
def binarySearchOnAnswer(constraints):
    def isFeasible(candidate):
        # Check if candidate value satisfies all constraints
        pass
    
    left, right = min_possible, max_possible
    
    while left < right:
        mid = left + (right - left + 1) // 2  # Upper bound template
        
        if isFeasible(mid):
            left = mid  # Try larger values
        else:
            right = mid - 1  # Must be smaller
    
    return left
```

### Problems
- **0875 – Koko Eating Bananas**
- **1802 – Maximum Value at a Given Index in a Bounded Array**

---

## Pattern 8 — Weighted Random Selection (Prefix Sum + Binary Search)

### When to Use
- **Weighted random sampling** where different elements have different selection probabilities.
- Need to map uniform random numbers to weighted distribution.

### How to Recognize
- Problem involves "random selection" with "weights" or "probabilities".
- Need to implement `pickIndex()` or similar random selection method.
- Probability of selection proportional to element weight.

### Tips / Pitfalls
- Build prefix sum array for cumulative weight ranges.
- Random number range should be `[1, total_weight]`, not `[0, total_weight-1]`.
- Use "find first >= target" binary search template.
- Binary search is on array indices, but comparison is with prefix sum values.

### Template
```python
class Solution:
    def __init__(self, w):
        self.prefix_sum = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)
    
    def pickIndex(self):
        target = random.randint(1, self.prefix_sum[-1])
        left, right = 0, len(self.prefix_sum) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            if self.prefix_sum[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        return left
```

### Problems
- **0528 – Random Pick with Weight**

---

## Pattern 9 — Find Closest Elements (Range Selection)

### When to Use
- Find k elements **closest** to a target value.
- Result should be a contiguous subarray due to sorting property.

### How to Recognize
- Asked for "k closest elements" to a target.
- Input array is sorted.
- Need to return k elements, not just find one element.

### Tips / Pitfalls
- Since array is sorted, k closest elements form a contiguous subarray.
- Binary search for optimal starting position of the sliding window.
- Compare boundary elements to determine window shift direction.

### Template
```python
def findClosestElements(arr, k, x):
    left, right = 0, len(arr) - k
    
    while left < right:
        mid = left + (right - left) // 2
        
        # Compare window boundaries
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1  # Right boundary closer
        else:
            right = mid     # Left boundary closer
    
    return arr[left:left + k]
```

### Problems
- **0658 – Find K Closest Elements**

---

## Quick Recognition Guide

- **"Find exact target in sorted array"** → Pattern 1 (Standard Binary Search)
- **"Insert position / first position >= target"** → Pattern 2 (Left Boundary)
- **"Search in rotated sorted array"** → Pattern 3 (Pattern Disruption)
- **"Find first and last occurrence"** → Pattern 4 (Boundary Search)
- **"Search in 2D sorted matrix"** → Pattern 5 (Coordinate Transformation)
- **"Find anomaly in patterned array"** → Pattern 6 (Pattern Disruption Analysis)
- **"Find maximum/minimum value satisfying constraints"** → Pattern 7 (BSOA)
- **"Weighted random selection"** → Pattern 8 (Prefix Sum + Binary Search)
- **"Find k closest elements"** → Pattern 9 (Range Selection)

---

## General Tips

- **Choose the right loop condition**: `while left <= right` for standard search, `while left < right` for boundary search.
- **Avoid infinite loops**: Use correct mid calculation, especially for upper bound search.
- **Handle edge cases**: Empty array, single element, target not found.
- **Understand the problem's constraints**: Sorted array assumption, duplicate handling, inclusive vs exclusive ranges.
- **Binary search is not just for arrays**: Can be used on answer spaces, time/capacity ranges, etc.

---

## Problems Mapped

- **0033 – Search in Rotated Sorted Array** → Pattern 3
- **0034 – Find First and Last Position** → Pattern 4
- **0035 – Search Insert Position** → Pattern 2
- **0074 – Search a 2D Matrix** → Pattern 5
- **0540 – Single Element in a Sorted Array** → Pattern 6
- **0528 – Random Pick with Weight** → Pattern 8
- **0658 – Find K Closest Elements** → Pattern 9
- **0704 – Binary Search** → Pattern 1
- **0875 – Koko Eating Bananas** → Pattern 7
- **1802 – Maximum Value at a Given Index** → Pattern 7

---
