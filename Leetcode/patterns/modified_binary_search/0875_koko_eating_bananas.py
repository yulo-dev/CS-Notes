"""
LeetCode 875 - Koko Eating Bananas

Problem Statement:
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas 
and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead 
and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9
"""

import math
from typing import List

# Solution 1: Brute Force (Naive Approach)
# Time: O(max(piles) * n) → Try every possible speed from 1 to max(piles)
# Space: O(1) → Only using constant extra space
class Solution1:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Approach: Try every possible eating speed from 1 to max(piles)
        
        This approach is straightforward but inefficient for large inputs.
        We test every possible speed until we find the minimum one that works.
        
        Logic:
        - Speed must be at least 1 (eat something each hour)
        - Speed never needs to exceed max(piles) (largest pile size)
        - For each speed, calculate total hours needed
        - Return first speed that allows finishing within h hours
        """
        def calculate_hours(speed: int) -> int:
            """Calculate total hours needed at given eating speed"""
            total_hours = 0
            for pile in piles:
                # Each pile takes ceil(pile/speed) hours to finish
                total_hours += math.ceil(pile / speed)
            return total_hours
        
        # Try speeds from 1 to maximum pile size
        for speed in range(1, max(piles) + 1):
            if calculate_hours(speed) <= h:
                return speed
        
        # This should never be reached given the constraints
        return max(piles)


# Solution 2: Binary Search on Answer (Optimal)
# Time: O(n * log(max(piles))) → Binary search on speed range
# Space: O(1) → Only using constant extra space
class Solution2:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Approach: Binary Search on Answer (BSOA) - Standard Template
        
        Key Insights:
        1. Speed range: [1, max(piles)] - minimum 1, maximum is largest pile
        2. Monotonic property: if speed k works, then k+1, k+2... also work
        3. We want the minimum speed that works, so search for left boundary
        4. For each speed, calculate total hours needed and compare with h
        
        Binary Search Template:
        - while left < right: ensures convergence to single answer
        - right = mid: when condition met, try smaller values
        - left = mid + 1: when condition not met, need larger values
        - return left: guaranteed to be minimum valid answer
        """
        left = 1           # Minimum possible eating speed
        right = max(piles) # Maximum needed eating speed

        while left < right:
            mid = left + (right - left) // 2  # Avoid overflow

            # Calculate total hours needed at speed 'mid'
            hours = 0
            for p in piles:
                # Ceiling division: ceil(p/mid) = (p + mid - 1) // mid
                # This avoids floating point operations
                hours += (p + mid - 1) // mid

            if hours <= h:
                # This speed works, try to find a smaller one
                right = mid
            else:
                # This speed is too slow, need faster speed
                left = mid + 1

        return left  # Minimum valid eating speed


"""
Key Insights and Analysis:

1. Problem Classification:
   - Binary Search on Answer (BSOA)
   - Optimization problem with monotonic property
   - Classic "minimize the maximum" pattern

2. Why Binary Search Works:
   - Monotonic property: if speed k allows finishing in h hours, then k+1, k+2... also work
   - If speed k doesn't work, then speeds 1, 2, ..., k-1 also don't work
   - This creates a clear binary search condition: FFFF...TTTTT pattern

3. Speed Range Analysis:
   - Minimum speed: 1 banana per hour (must eat at least something)
   - Maximum speed: max(piles) bananas per hour (never need faster than largest pile)
   - Search space: [1, max(piles)]

4. Time Calculation Logic:
   - For each pile of size p and speed k: time = ceil(p/k) hours
   - Why ceiling? If pile has p bananas and speed is k:
     * If p <= k: takes 1 hour (eat entire pile)
     * If p > k: takes ceil(p/k) hours (partial pile each hour except last)
   - Total time = sum of individual pile times

5. Ceiling Division Trick:
   - math.ceil(a/b) = (a + b - 1) // b
   - Avoids floating point arithmetic
   - Example: ceil(7/3) = 3, (7 + 3 - 1) // 3 = 9 // 3 = 3

6. Template Choice:
   - while left < right vs while left <= right
   - left < right: converges to single answer, cleaner logic
   - left <= right: needs result variable, more verbose

7. Common Mistakes:
   - Using floor division instead of ceiling for time calculation
   - Incorrect boundary updates (infinite loops)
   - Off-by-one errors in search range

8. Related BSOA Problems:
   - LeetCode 410: Split Array Largest Sum
   - LeetCode 1011: Capacity To Ship Packages Within D Days
   - LeetCode 1283: Find Smallest Divisor Given Threshold
   - LeetCode 2064: Minimized Maximum Products Distributed

9. 
   - Start with brute force to show understanding
   - Identify monotonic property: "if k works, then k+1 works too"
   - Implement binary search with proper template
   - Explain ceiling division optimization
   - Discuss time complexity improvement: O(max(piles) * n) → O(n * log(max(piles)))

10. Edge Cases:
    - Single pile: works with any reasonable speed
    - h equals number of piles: each pile gets exactly 1 hour
    - Large piles with small h: requires high eating speed
    - Many small piles: low eating speed sufficient

Solution Recommendation:
- Solution 1: Good for explaining the problem and brute force approach
- Solution 2: Standard interview answer using BSOA template
"""
