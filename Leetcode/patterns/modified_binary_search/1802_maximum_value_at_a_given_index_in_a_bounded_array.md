# Leetcode 1802 - Maximum Value at a Given Index in a Bounded Array

**Tags:** `Binary Search`, `Math`, `Greedy`, `Array Construction`

**Data Structures:** `Array`, `Mathematical Sequences`

**Algorithms:** `Binary Search on Answer`, `Arithmetic Sequence`, `Greedy Construction`

## ☀️ UMPIRE

**Understand:** You are given three integers `n`, `index` and `maxSum`. You want to construct an array `nums` (0-indexed) that satisfies: `nums.length == n`, all elements are positive integers, `abs(nums[i] - nums[i+1]) <= 1`, and the sum does not exceed `maxSum`. Return the maximum possible value of `nums[index]`.

**Match:** This is a Binary Search on Answer (BSOA) problem combined with mathematical optimization. The key insight is that the optimal array forms a mountain shape with the peak at the given index, and we can calculate the minimum sum using arithmetic sequence formulas.

**Plan:**
1. Binary search on the answer range [1, maxSum] for maximum feasible peak value
2. For each candidate peak, calculate minimum possible array sum using mountain construction
3. Use arithmetic sequence formulas to efficiently compute left and right side sums
4. Apply upper bound binary search template since we want maximum feasible value

**Implement:** See the code section below.

**Review:**
- Ensure binary search template handles edge cases correctly (avoid infinite loops)
- Verify arithmetic sequence formulas for both cases (reaches 1 vs doesn't reach 1)
- Test with edge cases like single element array or peak at boundaries
- Confirm that mountain construction truly minimizes sum

**Evaluate:**
- Time: O(log(maxSum)) - binary search on answer range
- Space: O(1) - only using constant extra space for calculations

## ☀️ Why This Is a Binary Search on Answer Problem

This problem exhibits the classic BSOA pattern with mathematical optimization:
- **Answer space**: The peak value ranges from 1 to maxSum
- **Monotonic property**: Larger peak values require larger minimum sums
- **Feasibility check**: Can calculate minimum sum for any given peak value
- **Optimization goal**: Find maximum peak value that keeps sum ≤ maxSum

Key insights:
- Direct construction is complex, but checking feasibility for a given peak is manageable
- Mountain shape minimizes sum while satisfying adjacency constraints
- Mathematical formulas enable O(1) sum calculation instead of O(n) simulation
- Binary search efficiently navigates the trade-off between peak height and sum constraint

## ☀️ Mountain Construction Logic

```
Example: n=7, index=3, peak=5
Optimal mountain shape:

Position: 0  1  2  3  4  5  6
Value:   [2, 3, 4, 5, 4, 3, 2]
                  ↑
                peak

Left side: decreases from peak-1 down to minimum 1
Right side: decreases from peak-1 down to minimum 1
Total sum: minimized while satisfying all constraints
```

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `n = 4, index = 2, maxSum = 6` | Standard mountain case | `2` |
| `n = 6, index = 1, maxSum = 10` | Peak near left boundary | `3` |
| `n = 1, index = 0, maxSum = 1` | Single element array | `1` |
| `n = 1, index = 0, maxSum = 100` | Single element, large sum | `100` |
| `n = 3, index = 0, maxSum = 4` | Peak at left boundary | `2` |
| `n = 3, index = 2, maxSum = 4` | Peak at right boundary | `2` |
| `n = 5, index = 2, maxSum = 5` | Minimal sum constraint | `1` |
| `n = 10, index = 5, maxSum = 50` | Large array, centered peak | `9` |

These test:
- Peak at different positions (center, boundaries)
- Minimal and maximal sum constraints
- Single element edge case
- Various array sizes and index positions

## ☀️ Code

### Solution 1: Brute Force (Demonstration Only)
**Time: O(maxSum) → Try every possible peak value**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        Approach: Try every possible peak value from maxSum down to 1
        
        This approach demonstrates problem understanding but is too slow.
        Used to show the brute force baseline before optimization.
        """
        def calculate_min_sum(peak):
            total = peak
            
            # Left side construction
            current = peak - 1
            for i in range(index - 1, -1, -1):
                total += max(1, current)
                current -= 1
            
            # Right side construction
            current = peak - 1
            for i in range(index + 1, n):
                total += max(1, current)
                current -= 1
            
            return total
        
        # Try from largest to smallest peak
        for peak in range(maxSum, 0, -1):
            if calculate_min_sum(peak) <= maxSum:
                return peak
        
        return 1
```

### Solution 2: Binary Search with Mathematical Formula (Optimal)
**Time: O(log(maxSum)) → Binary search on answer range**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        Approach: Binary search on answer with arithmetic sequence formulas
        
        Key Insight:
        - Optimal array is mountain-shaped with peak at index
        - Use arithmetic sequence formulas for O(1) sum calculation
        - Binary search finds maximum feasible peak value
        """
        def calculate_sum(peak):
            left_length = index
            right_length = n - index - 1
            
            # Calculate left side sum
            if peak <= left_length:
                # Sequence reaches 1, then stays at 1
                # Decreasing part: (peak-1) + (peak-2) + ... + 1
                left_sum = peak * (peak - 1) // 2 + (left_length - (peak - 1))
            else:
                # Pure arithmetic sequence that doesn't reach 1
                # Sequence: (peak-left_length) + ... + (peak-1)
                left_sum = left_length * (2 * peak - left_length - 1) // 2
            
            # Calculate right side sum (symmetric logic)
            if peak <= right_length:
                right_sum = peak * (peak - 1) // 2 + (right_length - (peak - 1))
            else:
                right_sum = right_length * (2 * peak - right_length - 1) // 2
            
            return left_sum + peak + right_sum
        
        left = 1
        right = maxSum
        
        while left < right:
            mid = left + (right - left + 1) // 2  # Upper bound binary search
            
            if calculate_sum(mid) <= maxSum:
                left = mid      # mid is feasible, try larger values
            else:
                right = mid - 1  # mid is too large, must be smaller
        
        return left
```

### Solution 3: Binary Search with Direct Simulation (Alternative)
**Time: O(log(maxSum) * n) → Binary search with O(n) sum calculation**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        Approach: Binary search with mountain simulation
        
        This approach simulates actual array construction for each peak value.
        Less efficient than mathematical formula but more intuitive.
        """
        def is_feasible(peak):
            total = 0
            
            # Calculate sum by simulating mountain construction
            for i in range(n):
                distance = abs(i - index)
                value = max(1, peak - distance)
                total += value
                
                if total > maxSum:  # Early termination optimization
                    return False
            
            return True
        
        left = 1
        right = maxSum
        
        while left < right:
            mid = left + (right - left + 1) // 2
            
            if is_feasible(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
```

## ☀️ Notes

**Key Algorithm Components:**
- **Upper bound binary search template**: Required when searching for maximum feasible value
- **Arithmetic sequence formula**: Enables O(1) sum calculation instead of O(n) simulation
- **Mountain construction principle**: Minimizes sum while satisfying adjacency constraints
- **Two-case analysis**: Handles sequences that reach 1 vs sequences that don't reach 1

**Critical Insight:**
The algorithm leverages the mathematical property that the optimal array forms a mountain shape. The arithmetic sequence formulas are derived from this geometric insight, enabling efficient sum calculation.

## ☀️ Mathematical Formula Derivation

```
Mountain construction for peak=5, left_length=3:

Case 1: peak > left_length (doesn't reach 1)
Sequence: [2, 3, 4, 5] (values: peak-3, peak-2, peak-1, peak)
Sum = 3 * (2 + 4) / 2 = 9
Formula: left_length * (2*peak - left_length - 1) / 2

Case 2: peak <= left_length (reaches 1 and stays)
Sequence: [1, 1, 2, 3] for peak=3, left_length=3
Decreasing part: 2 + 1 = 3 = peak*(peak-1)/2
Constant part: 1 * (3 - 2) = 1
Formula: peak*(peak-1)/2 + (left_length - (peak-1))
```

## ☀️ Coding Walkthrough Script

I need to find the maximum possible value at a specific index while keeping the array sum within bounds and satisfying the adjacency constraint.
The key insight is that the optimal array forms a mountain shape with the peak at the given index. This minimizes the total sum because we make values as small as possible while satisfying the constraint that adjacent elements differ by at most 1.
I'll use binary search on the answer - trying different peak values from 1 to maxSum. For each candidate peak, I need to calculate the minimum possible sum of the resulting mountain array.
The mathematical insight is that each side of the mountain follows an arithmetic sequence, decreasing by 1 until it reaches 1, then staying at 1. I can calculate these sums using arithmetic sequence formulas rather than simulating the entire array.
For the binary search, since I want the maximum feasible peak value, I need to use the upper bound template with mid biased upward to avoid infinite loops. When a peak value works, I try larger values; when it doesn't work, I try smaller values.

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Brute Force | O(maxSum) | O(1) | Try all peak values | Simple but too slow |
| Mathematical BSOA | O(log(maxSum)) | O(1) | **Optimal**; Arithmetic sequence formulas | Most efficient; complex math |
| Simulation BSOA | O(log(maxSum) * n) | O(1) | Array simulation per candidate | More intuitive but slower |
| Greedy Construction | O(n) | O(1) | **FAILS**; Cannot guarantee optimality | Common wrong approach |

## ☀️ Binary Search on Answer Insights

- **Prerequisites:** Answer has monotonic property (larger peak → larger minimum sum)
- **Core insight:** Checking feasibility is easier than direct construction
- **Template choice:** Upper bound search since we want maximum feasible value
- **Decision criterion:** Compare calculated sum with maxSum constraint
- **Convergence:** Binary search naturally finds the boundary between feasible and infeasible
- **Mathematical optimization:** Arithmetic sequences enable efficient sum calculation

**Template Recognition:** This is a classic "find maximum value satisfying constraint" problem, which typically uses binary search on answer with upper bound template.

**Note:** Solution 1 demonstrates problem understanding but is too slow for large inputs. Solution 2 is the optimal approach expected in interviews, combining binary search with mathematical insight. Solution 3 provides an alternative that's easier to understand but less efficient. The key learning is recognizing the BSOA pattern and applying mathematical optimization for efficiency.
