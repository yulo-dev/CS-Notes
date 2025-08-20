"""
Problem Statement:
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] 
(inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), 
and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

Example 1:
Input: ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
       [[[1,3]],[],[],[],[],[]]
Output: [null,1,1,1,1,0]
Explanation:
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. The probability of picking index 1 is 3/4 = 0.75
solution.pickIndex(); // return 1. Same as above
solution.pickIndex(); // return 1. Same as above  
solution.pickIndex(); // return 1. Same as above
solution.pickIndex(); // return 0. The probability of picking index 0 is 1/4 = 0.25

Constraints:
- 1 <= w.length <= 10^4
- 1 <= w[i] <= 10^5
- pickIndex will be called at most 10^4 times.
"""

import random
from typing import List

# Solution 1: Linear Search (Naive Approach)
# Time: O(n) for pickIndex, O(n) for __init__
# Space: O(n) → Store prefix sum array
class Solution1:
    def __init__(self, w: List[int]):
        """
        Approach: Build prefix sum and use linear search
        
        This approach is straightforward but inefficient for pickIndex.
        Used to demonstrate the basic idea before optimization.
        """
        self.prefix_sum = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)
    
    def pickIndex(self) -> int:
        """Linear search to find the target index"""
        target = random.randint(1, self.prefix_sum[-1])
        
        # Linear search for first prefix_sum[i] >= target
        for i in range(len(self.prefix_sum)):
            if self.prefix_sum[i] >= target:
                return i
        
        return len(self.prefix_sum) - 1  # Should never reach here


# Solution 2: Binary Search (Optimal Approach)
# Time: O(log n) for pickIndex, O(n) for __init__
# Space: O(n) → Store prefix sum array
class Solution2:
    def __init__(self, w: List[int]):
        """
        Approach: Build prefix sum for efficient range mapping
        
        Key Insight:
        - Convert weights to cumulative ranges using prefix sum
        - Each index i covers range [prefix_sum[i-1] + 1, prefix_sum[i]]
        - Binary search efficiently finds which range contains the random number
        """
        self.prefix_sum = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)
    
    def pickIndex(self) -> int:
        """Binary search to find the target index"""
        # Generate random number in range [1, total_weight]
        target = random.randint(1, self.prefix_sum[-1])
        
        # Binary search for first prefix_sum[i] >= target
        left, right = 0, len(self.prefix_sum) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if self.prefix_sum[mid] >= target:
                # mid might be the answer, keep it in search space
                right = mid
            else:
                # mid is definitely not the answer, exclude it
                left = mid + 1
        
        return left


# Solution 3: Using Python's bisect module (Clean Implementation)
# Time: O(log n) for pickIndex, O(n) for __init__
# Space: O(n) → Store prefix sum array
import bisect

class Solution3:
    def __init__(self, w: List[int]):
        """
        Approach: Use Python's built-in binary search
        
        This approach leverages Python's bisect module for cleaner code.
        Same algorithm as Solution 2 but with library optimization.
        """
        self.prefix_sum = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)
    
    def pickIndex(self) -> int:
        """Use bisect_left to find insertion point"""
        target = random.randint(1, self.prefix_sum[-1])
        
        # bisect_left finds the leftmost position to insert target
        # This gives us the first index where prefix_sum[i] >= target
        return bisect.bisect_left(self.prefix_sum, target)


# Solution 4: Alternative Binary Search Template (Find Right Boundary)
# Time: O(log n) for pickIndex, O(n) for __init__
# Space: O(n) → Store prefix sum array
class Solution4:
    def __init__(self, w: List[int]):
        """
        Approach: Alternative binary search implementation
        
        This shows a different binary search template that can be used.
        Same efficiency but different boundary handling.
        """
        self.prefix_sum = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)
    
    def pickIndex(self) -> int:
        """Alternative binary search template"""
        target = random.randint(1, self.prefix_sum[-1])
        
        left, right = 0, len(self.prefix_sum) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if self.prefix_sum[mid] < target:
                left = mid + 1
            else:
                # Found a valid candidate, but there might be a smaller one
                if mid == 0 or self.prefix_sum[mid - 1] < target:
                    return mid
                right = mid - 1
        
        return left


"""
Key Insights and Takeaways:

1. Problem Classification:
   - Weighted random selection using prefix sum + binary search
   - Classic application of cumulative probability distribution
   - Range mapping problem with efficient lookup requirement

2. Core Algorithm - Prefix Sum + Binary Search:
   - Convert weights to cumulative ranges using prefix sum
   - Map random numbers to indices using binary search
   - Time complexity: O(n) init + O(log n) per query

3. Range Mapping Technique:
   - Weight [1,3,2] → Prefix sum [1,4,6] → Ranges [1,1], [2,4], [5,6]
   - Random number 1-6 maps to correct index with proper probability
   - Binary search finds "first prefix_sum[i] >= target"

4. Why This Works:
   - Each index gets number of slots proportional to its weight
   - Random number generation ensures uniform distribution over slots
   - Binary search efficiently maps slots back to original indices

5. Interview Strategy:
   - Start with linear search to show understanding
   - Identify inefficiency and propose binary search optimization
   - Explain the prefix sum + range mapping concept clearly
   - Code the binary search template correctly

6. Common Mistakes to Avoid:
   - Wrong random number range (should be 1 to total, not 0 to total-1)
   - Incorrect binary search boundary conditions
   - Not handling edge cases in prefix sum calculation
   - Confusing search space (array indices) with comparison values

7. Related Problems:
   - Random sampling from distributions
   - Cumulative frequency problems
   - Any weighted selection algorithms

8. Template Value:
   - Prefix sum for range queries and cumulative calculations
   - Binary search for efficient lookup in sorted arrays
   - Weighted random selection pattern

9. Python-specific Notes:
   - bisect module provides optimized binary search
   - random.randint(a,b) includes both endpoints
   - List comprehension can simplify prefix sum calculation

10. Solution Recommendation:
    - Solution 2 is the standard implementation for interviews
    - Solution 3 shows Python-specific optimization
    - Solution 1 demonstrates understanding but is suboptimal
    - Solution 4 shows alternative binary search template

Note: This problem demonstrates a fundamental technique in probability and 
algorithms - converting discrete probability distributions into efficient 
sampling procedures using cumulative distribution functions and binary search.
"""
