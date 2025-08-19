"""
Problem Statement:
You are given three integers n, index and maxSum. You want to construct an array nums (0-indexed) 
that satisfies the following conditions:

- nums.length == n
- nums[i] is a positive integer where 0 <= i < n.
- abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
- The sum of all the elements of nums does not exceed maxSum.

Return the maximum possible value of nums[index].

Example 1:
Input: n = 4, index = 2, maxSum = 6
Output: 2
Explanation: nums = [1,1,2,1] is one possible array.

Example 2:
Input: n = 6, index = 1, maxSum = 10
Output: 3
Explanation: nums = [1,3,3,1,1,1] is one possible array.

Constraints:
- 1 <= n <= 10^6
- 0 <= index < n
- 1 <= maxSum <= 10^9
"""

from typing import List

# Solution 1: Brute Force (Too Slow)
# Time: O(maxSum) → Try every possible peak value
# Space: O(1) → Only using constant extra space
class Solution1:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        Approach: Try every possible peak value from 1 to maxSum
        
        This approach is straightforward but inefficient.
        For each potential peak value, calculate minimum possible sum
        and check if it's within maxSum constraint.
        """
        def calculate_min_sum(peak):
            total = peak  # Start with peak value
            
            # Calculate left side
            for i in range(index - 1, -1, -1):
                prev_val = total if i == index - 1 else nums[i + 1]
                nums[i] = max(1, prev_val - 1)
                total += nums[i]
            
            # Calculate right side  
            for i in range(index + 1, n):
                prev_val = nums[i - 1]
                nums[i] = max(1, prev_val - 1)
                total += nums[i]
            
            return total
        
        # Try each possible peak value
        for peak in range(maxSum, 0, -1):
            nums = [0] * n
            nums[index] = peak
            if calculate_min_sum(peak) <= maxSum:
                return peak
        
        return 1


# Solution 2: Binary Search with Mathematical Formula (Optimal)
# Time: O(log(maxSum)) → Binary search on answer range
# Space: O(1) → Only using constant extra space
class Solution2:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        Approach: Binary search on answer with mathematical sum calculation
        
        Key Insight:
        - Optimal array is mountain-shaped with peak at index
        - Calculate minimum sum using arithmetic sequence formulas
        - Use binary search to find maximum feasible peak value
        """
        def calculate_sum(peak):
            left_length = index
            right_length = n - index - 1
            
            # Calculate left side sum
            if peak <= left_length:
                # Peak value decreases to 1, then stays at 1
                # Decreasing part: (peak-1) + (peak-2) + ... + 1 = peak*(peak-1)/2
                # Constant part: remaining positions stay at 1
                left_sum = peak * (peak - 1) // 2 + (left_length - (peak - 1))
            else:
                # Pure arithmetic sequence: doesn't reach 1
                # Sequence: (peak-left_length) + ... + (peak-2) + (peak-1)
                left_sum = left_length * (2 * peak - left_length - 1) // 2
            
            # Calculate right side sum (same logic)
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
                right = mid - 1  # mid is too large, try smaller values
        
        return left


# Solution 3: Binary Search with Simulation (Alternative)
# Time: O(log(maxSum) * n) → Binary search with O(n) sum calculation
# Space: O(1) → Only using constant extra space
class Solution3:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        Approach: Binary search with direct array simulation
        
        This approach simulates the actual array construction
        for each candidate peak value. Less efficient but more intuitive.
        """
        def is_feasible(peak):
            total = 0
            
            # Calculate sum by simulating mountain construction
            for i in range(n):
                distance = abs(i - index)
                value = max(1, peak - distance)
                total += value
                
                if total > maxSum:  # Early termination
                    return False
            
            return total <= maxSum
        
        left = 1
        right = maxSum
        
        while left < right:
            mid = left + (right - left + 1) // 2
            
            if is_feasible(mid):
                left = mid
            else:
                right = mid - 1
        
        return left


# Solution 4: Helper Function Approach (Clean Implementation)
# Time: O(log(maxSum)) → Binary search on answer range
# Space: O(1) → Only using constant extra space
class Solution4:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        Approach: Clean implementation with helper functions
        
        Separates the mathematical calculation into clear helper functions
        for better readability and maintainability.
        """
        def arithmetic_sum(first, last, count):
            """Calculate sum of arithmetic sequence"""
            if count <= 0:
                return 0
            return count * (first + last) // 2
        
        def calculate_side_sum(peak, side_length):
            """Calculate sum for one side of the mountain"""
            if peak <= side_length:
                # Decreasing sequence + constant 1's
                decreasing_sum = arithmetic_sum(peak - 1, 1, peak - 1)
                constant_sum = side_length - (peak - 1)
                return decreasing_sum + constant_sum
            else:
                # Pure decreasing sequence
                return arithmetic_sum(peak - 1, peak - side_length, side_length)
        
        def total_sum(peak):
            """Calculate total sum for given peak value"""
            left_sum = calculate_side_sum(peak, index)
            right_sum = calculate_side_sum(peak, n - index - 1)
            return left_sum + peak + right_sum
        
        # Binary search for maximum feasible peak
        left, right = 1, maxSum
        
        while left < right:
            mid = left + (right - left + 1) // 2
            
            if total_sum(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        
        return left


"""
Key Insights and Takeaways:

1. Problem Classification:
   - Binary search on answer (BSOA)
   - Mathematical optimization with constraints
   - Mountain/peak finding with arithmetic sequences

2. Core Mathematical Insight:
   - Optimal array is mountain-shaped with peak at given index
   - Adjacent difference ≤ 1 creates arithmetic sequence pattern
   - Minimize sum by making values as small as possible while maintaining peak

3. Binary Search Template - Upper Bound:
   - while left < right: (not <=)
   - mid = left + (right - left + 1) // 2 (upper bound template)
   - if feasible: left = mid (keep trying larger values)
   - else: right = mid - 1 (current value too large)

4. Mathematical Formula Derivation:
   - Mountain shape: decreases by 1 on each side until reaching 1
   - Two cases per side: sequence reaches 1 vs doesn't reach 1
   - Arithmetic sequence sum: n * (first + last) / 2

5. Why Upper Bound Binary Search:
   - We want maximum feasible value
   - When condition is met, try larger values (left = mid)
   - Requires mid to be biased upward to avoid infinite loop

6. Strategy:
   - Start with brute force to show understanding
   - Explain mountain shape optimization insight
   - Implement binary search with mathematical calculation
   - Mention that simulation approach is also valid but slower

7. Common Pitfalls:
   - Binary search infinite loop (must use upper bound template)
   - Off-by-one errors in arithmetic sequence calculation
   - Integer overflow (use appropriate data types)
   - Forgetting the peak element in total sum

8. Related Problems:
   - Other binary search on answer problems
   - Mathematical optimization with constraints
   - Array construction with adjacency constraints

9. Template Recognition:
   - "Maximum/minimum value satisfying constraint" → BSOA
   - Optimization with monotonic property
   - When direct calculation is complex but checking feasibility is easier

10. Solution Recommendation:
    - Solution 2 is optimal and most commonly expected
    - Solution 4 provides cleaner code organization
    - Solution 3 is good for initial understanding
    - Solution 1 shows problem comprehension but is too slow

Note: This is indeed a more specialized problem that combines binary search
with mathematical insight. The arithmetic sequence formulas are the tricky part,
but the binary search pattern is a valuable template for optimization problems.
"""
