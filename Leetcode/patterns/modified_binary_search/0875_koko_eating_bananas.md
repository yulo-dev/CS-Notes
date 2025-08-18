# Leetcode 0875 - Koko Eating Bananas

## ☀️ UMPIRE

**Understand:** Koko wants to eat all bananas before guards return in h hours. She can choose her eating speed k (bananas per hour). Each hour, she picks one pile and eats k bananas from it. If the pile has fewer than k bananas, she eats all remaining and stops for that hour. Find the minimum speed k to finish all bananas within h hours.

**Match:** This is a Binary Search on Answer (BSOA) problem. The key insight is that eating speeds form a monotonic sequence - if speed k works, then k+1, k+2... also work. We need to find the minimum valid speed using binary search on the answer space.

**Plan:**
1. Identify speed range: [1, max(piles)] - minimum 1, maximum is largest pile
2. Use binary search to find minimum valid speed
3. For each candidate speed, calculate total hours needed
4. Use ceiling division to handle partial pile consumption
5. Apply standard BSOA template with while left < right

**Implement:** See the code section below.

**Review:**
- Verify ceiling division logic for partial piles
- Ensure binary search boundaries are correct
- Test edge cases like single pile or h equals number of piles
- Confirm time complexity improvement over brute force

**Evaluate:**
- Time: O(n * log(max(piles))) - binary search on speed range
- Space: O(1) - only using constant extra space

## ☀️ Why This Is a Binary Search on Answer Problem

This problem exemplifies the BSOA pattern rather than traditional value search:
- **Traditional binary search**: Searches for a specific value in sorted data
- **Binary search on answer**: Searches for the optimal answer in a range of possibilities
- **Monotonic property**: If speed k allows completion within h hours, then k+1, k+2... also work
- **Optimization goal**: Find the minimum speed that satisfies the constraint

Key insights:
- Answer space: [1, max(piles)] represents all possible eating speeds
- Decision function: Can Koko finish all bananas in h hours at speed k?
- Monotonic nature: The decision function changes from False to True exactly once
- Search target: The leftmost True value (minimum valid speed)

## ☀️ Speed and Time Analysis

```
Example: piles = [3,6,7,11], h = 8

Speed k=1: 3+6+7+11 = 27 hours (too slow)
Speed k=2: 2+3+4+6 = 15 hours (too slow)
Speed k=3: 1+2+3+4 = 10 hours (too slow)
Speed k=4: 1+2+2+3 = 8 hours ✓ (works!)
Speed k=5: 1+2+2+3 = 8 hours ✓ (works but not minimum)

Ceiling division examples for pile=7:
- Speed 3: ceil(7/3) = ceil(2.33) = 3 hours
- Speed 4: ceil(7/4) = ceil(1.75) = 2 hours
- Speed 7: ceil(7/7) = ceil(1.0) = 1 hour
```

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `piles = [3,6,7,11], h = 8` | Standard case | `4` |
| `piles = [30,11,23,4,20], h = 5` | h equals number of piles | `30` |
| `piles = [30,11,23,4,20], h = 6` | Extra hour available | `23` |
| `piles = [312884470], h = 2` | Single large pile | `156442235` |
| `piles = [1,1,1,1], h = 4` | All small piles, enough time | `1` |
| `piles = [1,1,1,1], h = 8` | Plenty of time | `1` |
| `piles = [5,10,15], h = 3` | Each pile needs 1 hour | `15` |
| `piles = [1,2,3], h = 10` | Lots of extra time | `1` |

These test:
- Time pressure scenarios (h close to number of piles)
- Single pile edge cases
- Minimum speed scenarios
- Large pile sizes requiring speed optimization

## ☀️ Code

### Solution 1: Brute Force (Naive Approach)
**Time: O(max(piles) * n) → Try every possible speed**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Approach: Try every possible eating speed from 1 to max(piles)
        
        This approach shows the basic logic but is inefficient for large inputs.
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
        
        return max(piles)  # Fallback (should never reach here)
```

### Solution 2: Binary Search on Answer (Optimal)
**Time: O(n * log(max(piles))) → Binary search on speed range**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Approach: Binary Search on Answer - Standard Template
        
        Key Insights:
        - Speed range: [1, max(piles)]
        - Monotonic property: if speed k works, then k+1, k+2... also work
        - Search for minimum valid speed using BSOA template
        """
        left = 1           # Minimum possible eating speed
        right = max(piles) # Maximum needed eating speed

        while left < right:
            mid = left + (right - left) // 2  # Avoid overflow

            # Calculate total hours needed at speed 'mid'
            hours = 0
            for p in piles:
                # Ceiling division: ceil(p/mid) = (p + mid - 1) // mid
                hours += (p + mid - 1) // mid

            if hours <= h:
                # This speed works, try to find a smaller one
                right = mid
            else:
                # This speed is too slow, need faster speed
                left = mid + 1

        return left  # Minimum valid eating speed
```

## ☀️ Notes

**Key Algorithm Components:**
- **BSOA template**: Search for optimal answer in range rather than specific value
- **Monotonic decision**: Speed validity creates clear True/False boundary
- **Ceiling division**: Handle partial pile consumption correctly
- **Boundary convergence**: while left < right ensures single answer

**Critical Insight:**
The algorithm works by recognizing that eating speeds have a monotonic property. Instead of searching for a value in data, we search for the optimal parameter that satisfies our constraint. The decision "Can finish in h hours?" creates a clear boundary in our search space.

## ☀️ Ceiling Division Logic Explained

```
Why ceiling division is needed:

Pile size: 7 bananas, Speed: 3 bananas/hour
Hour 1: Eat 3 bananas (4 remaining)
Hour 2: Eat 3 bananas (1 remaining)  
Hour 3: Eat 1 banana (0 remaining)
Total: 3 hours = ceil(7/3)

Mathematical equivalence:
ceil(a/b) = (a + b - 1) // b

Examples:
ceil(7/3) = (7 + 3 - 1) // 3 = 9 // 3 = 3 ✓
ceil(9/3) = (9 + 3 - 1) // 3 = 11 // 3 = 3 ✓
ceil(10/3) = (10 + 3 - 1) // 3 = 12 // 3 = 4 ✓
```

## ☀️ Coding Walkthrough Script

This problem asks for the minimum eating speed, which suggests optimization. I need to find the minimum value that satisfies a constraint - this is a classic Binary Search on Answer pattern.
Let me think about the constraints: Koko's speed can range from 1 (minimum) to max(piles) (she never needs to eat faster than the largest pile). This gives me a clear search range.
The key insight is monotonicity: if speed k allows finishing in h hours, then any faster speed k+1, k+2... will also work. This creates a False-False-True-True pattern perfect for binary search.
For my implementation, I'll use the standard BSOA template with while left < right. For each candidate speed, I calculate the total hours needed by summing ceil(pile/speed) for each pile. I use the ceiling division trick (p + mid - 1) // mid to avoid floating point operations.
If the total hours is within the limit, I know this speed works, so I search for potentially smaller speeds. Otherwise, I need a faster speed. The algorithm converges to the minimum valid speed automatically."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Brute Force | O(max(piles) * n) | O(1) | Linear search through speeds | Simple but inefficient |
| Binary Search on Answer | O(n * log(max(piles))) | O(1) | BSOA with monotonic property | **Optimal**; standard template |
| Ternary Search | O(n * log(max(piles))) | O(1) | Alternative search method | Same complexity, less common |
| Mathematical Approach | O(n) | O(1) | Direct formula calculation | Complex derivation, not practical |

## ☀️ Binary Search on Answer Insights

- **Problem pattern**: "Find minimum/maximum value that satisfies constraint"
- **Monotonic property**: Essential for binary search validity
- **Answer space**: Define clear range of possible solutions
- **Decision function**: Boolean test for constraint satisfaction
- **Template choice**: while left < right for boundary problems
- **Optimization**: Ceiling division and early termination techniques

**BSOA Recognition:** When you see "minimum speed," "maximum capacity," "smallest divisor," or similar optimization language with constraints, consider Binary Search on Answer. The key is identifying the monotonic relationship between the parameter and the constraint satisfaction.

**Note:** Solution 1 demonstrates the brute force baseline for comparison. Solution 2 is the interview-standard BSOA implementation that efficiently solves the optimization problem. This template applies to many similar constraint optimization problems.
