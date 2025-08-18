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

# Solution 1: Linear Search (Naive Approach)
# Time: O(max(piles) * n) → Try every possible speed from 1 to max(piles)
# Space: O(1) → Only using constant extra space
class Solution1:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Approach: Try every possible eating speed from 1 to max(piles)
        
        This approach is straightforward but inefficient for large inputs.
        We test every possible speed until we find the minimum one that works.
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
        Approach: Binary search on the eating speed
        
        Key Insights:
        1. Speed range: [1, max(piles)] - minimum 1, maximum is largest pile
        2. Monotonic property: if speed k works, then k+1, k+2... also work
        3. We want the minimum speed that works, so search for left boundary
        4. For each speed, calculate total hours needed and compare with h
        """
        def calculate_hours(speed: int) -> int:
            """Calculate total hours needed at given eating speed"""
            total_hours = 0
            for pile in piles:
                # Each pile takes ceil(pile/speed) hours to finish
                # Using math.ceil or integer division trick: (pile + speed - 1) // speed
                total_hours += math.ceil(pile / speed)
            return total_hours
        
        left, right = 1, max(piles)
        result = right  # Initialize to maximum possible speed
        
        while left <= right:
            mid = left + (right - left) // 2
            hours_needed = calculate_hours(mid)
            
            if hours_needed <= h:
                # This speed works, try to find a smaller one
                result = mid
                right = mid - 1
            else:
                # This speed is too slow, need faster speed
                left = mid + 1
        
        return result


# Solution 3: Binary Search with Optimized Calculation (Alternative)
# Time: O(n * log(max(piles))) → Binary search on speed range
# Space: O(1) → Only using constant extra space
class Solution3:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Alternative binary search implementation using integer division trick
        
        Instead of math.ceil(pile / speed), we use (pile + speed - 1) // speed
        This avoids floating point operations and is slightly more efficient.
        """
        def can_finish_in_time(speed: int) -> bool:
            """Check if Koko can finish all bananas in h hours at given speed"""
            total_hours = 0
            for pile in piles:
                # Ceiling division without floating point: (a + b - 1) // b
                total_hours += (pile + speed - 1) // speed
                if total_hours > h:  # Early termination optimization
                    return False
            return True
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if can_finish_in_time(mid):
                # This speed works, try smaller speeds
                right = mid
            else:
                # This speed doesn't work, try larger speeds
                left = mid + 1
        
        return left


# Solution 4: Binary Search with Range Optimization
# Time: O(n * log(max(piles))) → Binary search on speed range
# Space: O(1) → Only using constant extra space
class Solution4:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Optimized approach with better initial range estimation
        
        We can sometimes reduce the search range by calculating bounds more intelligently.
        """
        def calculate_hours(speed: int) -> int:
            return sum(math.ceil(pile / speed) for pile in piles)
        
        # Better lower bound: total_bananas / h (minimum average speed needed)
        total_bananas = sum(piles)
        left = math.ceil(total_bananas / h)
        right = max(piles)
        
        # Edge case: if we have more hours than piles, minimum speed is 1
        left = max(1, left)
        
        result = right
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if calculate_hours(mid) <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result


# Solution 5: Ternary Search (Alternative Approach - Educational)
# Time: O(n * log(max(piles))) → Ternary search on speed range
# Space: O(1) → Only using constant extra space
class Solution5:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Ternary search approach (educational purpose)
        
        Since the function is monotonic, we could use ternary search,
        but binary search is more standard and equally efficient for this problem.
        """
        def calculate_hours(speed: int) -> int:
            return sum(math.ceil(pile / speed) for pile in piles)
        
        left, right = 1, max(piles)
        
        while right - left > 2:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            
            if calculate_hours(mid1) <= h:
                right = mid1
            elif calculate_hours(mid2) > h:
                left = mid2
            else:
                left = mid1
                right = mid2
        
        # Check remaining candidates
        for speed in range(left, right + 1):
            if calculate_hours(speed) <= h:
                return speed
        
        return right


"""
Key Insights and Analysis:

1. Problem Classification:
   - Binary Search on Answer (BSOA)
   - Optimization problem with monotonic property
   - Resource allocation under time constraints

2. Core Insight - Monotonic Property:
   - If speed k allows finishing in h hours, then k+1, k+2... also work
   - If speed k doesn't work, then speeds 1, 2, ..., k-1 also don't work
   - This creates a clear binary search condition

3. Speed Range Analysis:
   - Minimum speed: 1 banana per hour (must eat at least something)
   - Maximum speed: max(piles) (never need to eat faster than largest pile)
   - Alternative lower bound: ceil(total_bananas / h) for better optimization

4. Time Calculation:
   - For each pile of size p and speed k: time = ceil(p/k) hours
   - Total time = sum of individual pile times
   - Must be <= h for the speed to be valid

5. Implementation Techniques:
   - Ceiling division: math.ceil(a/b) or (a + b - 1) // b
   - Early termination in validation function
   - Better initial bounds for optimization

6. Why This is BSOA (Binary Search on Answer):
   - We're searching for the minimum valid answer (speed)
   - The answer space has a clear range [1, max(piles)]
   - The validity function is monotonic
   - We want the leftmost (minimum) valid answer

7. Common Mistakes to Avoid:
   - Using floor division instead of ceiling for time calculation
   - Not handling the case where pile < speed correctly
   - Incorrect binary search boundary conditions
   - Off-by-one errors in the search range

8. Optimization Opportunities:
   - Better lower bound calculation
   - Early termination in validation
   - Integer arithmetic instead of floating point

9. Related Problems (BSOA Pattern):
   - Minimum time to complete trips
   - Capacity to ship packages within D days
   - Minimum speed to arrive on time
   - Allocate mailboxes

10. 
    - Start with brute force (Solution 1) to show understanding
    - Identify the monotonic property
    - Implement binary search (Solution 2)
    - Discuss optimizations if time permits

Solution Recommendation:
- Solution 2 is the standard interview answer
- Solution 3 shows understanding of integer arithmetic optimization
"""
