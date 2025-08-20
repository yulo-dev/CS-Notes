# Leetcode 528 - Random Pick with Weight

**Tags:** `Binary Search`, `Prefix Sum`, `Random`, `Math`, `Array`

**Data Structures:** `Array`, `Prefix Sum Array`

**Algorithms:** `Binary Search`, `Prefix Sum`, `Weighted Random Selection`, `Cumulative Distribution`

## ☀️ UMPIRE

**Understand:** You are given a 0-indexed array of positive integers `w` where `w[i]` describes the weight of the `ith` index. You need to implement `pickIndex()`, which randomly picks an index in range `[0, w.length - 1]` and returns it. The probability of picking index `i` is `w[i] / sum(w)`.

**Match:** This is a Prefix Sum + Binary Search problem for weighted random selection. The key insight is to convert weights into cumulative ranges using prefix sum, then use binary search to efficiently map random numbers to corresponding indices.

**Plan:**
1. Build prefix sum array to create cumulative weight ranges
2. Generate random number in range [1, total_weight]
3. Use binary search to find first prefix_sum[i] >= random_number
4. Return the found index i

**Implement:** See the code section below.

**Review:**
- Ensure random number range is [1, total_weight] not [0, total_weight-1]
- Verify binary search correctly finds "first element >= target"
- Test with edge cases like single element or equal weights
- Confirm probability distribution matches expected weights

**Evaluate:**
- Time: O(n) for initialization, O(log n) for each pickIndex call
- Space: O(n) for storing prefix sum array

## ☀️ Why This Is a Prefix Sum + Binary Search Problem

This problem combines two classic algorithmic techniques:
- **Prefix Sum**: Converts weights into cumulative ranges for probability mapping
- **Binary Search**: Efficiently locates which range contains the random number
- **Weighted Random Selection**: Maps uniform random distribution to weighted distribution
- **Range Mapping**: Each index gets range size proportional to its weight

Key insights:
- Direct probability calculation would be complex and inefficient
- Prefix sum creates non-overlapping ranges that sum to total weight
- Binary search reduces lookup time from O(n) to O(log n)
- Random number generation provides uniform distribution over all ranges

## ☀️ Probability Distribution Visualization

```
Weight Array: [1, 3, 2]
Total Weight: 6
Probability: [1/6, 3/6, 2/6] = [16.67%, 50%, 33.33%]

Prefix Sum: [1, 4, 6]
Range Mapping:
Index 0: [1, 1]     (1 number,  probability 1/6)
Index 1: [2, 4]     (3 numbers, probability 3/6)  
Index 2: [5, 6]     (2 numbers, probability 2/6)

Random Number → Index Mapping:
1     → Index 0
2,3,4 → Index 1
5,6   → Index 2
```

## ☀️ Edge Case Notes

| Input | Description | Expected Behavior |
|-------|-------------|------------------|
| `w = [1]` | Single element | Always return 0 |
| `w = [1, 1, 1]` | Equal weights | Equal probability for each index |
| `w = [1, 100]` | Highly skewed weights | Index 1 chosen ~99% of time |
| `w = [5, 0, 3]` | Zero weight (invalid) | Not allowed per constraints |
| `w = [1, 2, 3, 4]` | Increasing weights | Higher indices more likely |

These test:
- Boundary conditions with minimal arrays
- Uniform vs non-uniform weight distributions
- Extreme probability skew scenarios
- Various array sizes and weight patterns

## ☀️ Code

### Solution 1: Linear Search (Demonstration)
**Time: O(n) for pickIndex, O(n) for initialization**  
**Space: O(n) → Store prefix sum array**

```python
import random

class Solution:
    def __init__(self, w: List[int]):
        """
        Approach: Build prefix sum and use linear search
        
        This approach demonstrates the core concept but is inefficient.
        Used to show the basic idea before binary search optimization.
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
```

### Solution 2: Binary Search (Optimal for Interview)
**Time: O(log n) for pickIndex, O(n) for initialization**  
**Space: O(n) → Store prefix sum array**

```python
import random

class Solution:
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
```

## ☀️ Notes

**Key Algorithm Components:**
- **Prefix sum construction**: Converts weights to cumulative ranges in O(n) time
- **Left boundary binary search**: Finds first element >= target efficiently
- **Random number generation**: Uniform distribution over [1, total_weight]
- **Range mapping**: Each index gets slots proportional to its weight

**Critical Insight:**
The algorithm transforms a weighted selection problem into a range lookup problem. By using prefix sums to create cumulative ranges and binary search for efficient lookup, we achieve optimal time complexity for repeated queries.

## ☀️ Algorithm Walkthrough Example

```
Weight Array: [1, 3, 2]

Step 1: Build prefix sum
total = 0
total += 1 → total = 1, prefix_sum = [1]
total += 3 → total = 4, prefix_sum = [1, 4] 
total += 2 → total = 6, prefix_sum = [1, 4, 6]

Step 2: Generate random number
target = random.randint(1, 6)  // Assume target = 3

Step 3: Binary search in [1, 4, 6]
left=0, right=2, mid=1
prefix_sum[1] = 4, 4 >= 3? YES → right = 1

left=0, right=1, mid=0  
prefix_sum[0] = 1, 1 >= 3? NO → left = 1

Final: left = right = 1, return 1
```

## ☀️ Coding Walkthrough Script

I need to implement weighted random selection where each index has a probability proportional to its weight.
My approach is to convert this into a range mapping problem using prefix sums. I'll build a prefix sum array where each element represents the cumulative weight up to that index. This creates non-overlapping ranges for each index.
For example, with weights [1,3,2], my prefix sum becomes [1,4,6]. This means index 0 covers range [1,1], index 1 covers [2,4], and index 2 covers [5,6].
To pick an index, I'll generate a random number from 1 to the total weight, then use binary search to find which range contains this number. I'm looking for the first prefix sum value that's greater than or equal to my random number.
The binary search ensures O(log n) lookup time, making this efficient even for large weight arrays.

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Linear Search | O(n) per query | O(n) | Sequential scan | Simple but inefficient |
| Binary Search | O(log n) per query | O(n) | **Recommended**; Range mapping + efficient lookup | Optimal for multiple queries |
| Direct Probability | O(n) per query | O(1) | Calculate cumulative probability | Complex and inefficient |

## ☀️ Prefix Sum + Binary Search Insights

- **Prerequisites:** Array of positive weights, need for efficient repeated queries
- **Core insight:** Transform probability distribution into range lookup problem
- **Template recognition:** "First element >= target" binary search pattern
- **Range construction:** Prefix sum creates cumulative weight boundaries
- **Lookup efficiency:** Binary search reduces O(n) to O(log n) per query
- **Probability preservation:** Range sizes maintain original weight proportions

**Mathematical Guarantee:** The prefix sum construction ensures that each index receives a number of "slots" exactly equal to its weight, and binary search correctly maps random numbers to their corresponding indices while preserving the weighted probability distribution.

**Note:** Solution 1 demonstrates the core concept but is too slow for large inputs. Solution 2 is the recommended approach for interviews, combining prefix sum preprocessing with efficient binary search lookup. This pattern is fundamental for weighted sampling algorithms and appears in many probability-related programming problems.
