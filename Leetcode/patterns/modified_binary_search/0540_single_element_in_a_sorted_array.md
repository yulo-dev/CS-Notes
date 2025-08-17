# Leetcode 0540 - Single Element in a Sorted Array

## ☀️ UMPIRE

**Understand:** You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Return the single element that appears only once. Your solution must run in O(log n) time and O(1) space.

**Match:** This is a Modified Binary Search problem specifically for parity analysis and pattern disruption. The key insight is that the single element disrupts the pairing pattern - before the single element, pairs start at even indices, and after the single element, pairs start at odd indices.

**Plan:**
1. Use binary search with index parity analysis
2. Check if pairs at even indices are complete (nums[even] == nums[even+1])
3. If pair is complete, single element is on the right side
4. If pair is broken, single element is on the left side (including current position)
5. Continue until search space converges to single element

**Implement:** See the code section below.

**Review:**
- Ensure we meet the O(log n) time complexity requirement
- Verify parity analysis correctly identifies search direction
- Handle edge cases and boundary conditions
- Test with arrays where single element is at different positions

**Evaluate:**
- Time: O(log n) - binary search eliminates half search space each iteration
- Space: O(1) - only using constant extra space

## ☀️ Why This Is a Modified Binary Search Problem

This problem requires pattern disruption analysis rather than standard value search:
- **Standard binary search**: Looks for specific target value
- **Parity analysis**: Detects disruption in paired element pattern
- **Pattern recognition**: Single element breaks the even-index pairing rule
- **Monotonic decision**: Parity check provides consistent search direction

Key insights:
- Before single element: pairs start at even indices [0,1], [2,3], [4,5]...
- After single element: pairs start at odd indices due to shift
- By checking nums[even] == nums[even+1], we can determine which side contains the single element
- This creates a monotonic condition perfect for binary search

## ☀️ Pattern Analysis

```
Normal pairing (no single element):
[1,1,2,2,3,3,4,4]
 0 1 2 3 4 5 6 7  (indices)
[even,odd] pairs: (0,1), (2,3), (4,5), (6,7)

With single element at position 4:
[1,1,2,2,5,3,3,4,4]
 0 1 2 3 4 5 6 7 8  (indices)
Before single: (0,1), (2,3) - pairs at even indices ✓
After single: (5,6), (7,8) - pairs shifted to odd indices
```

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `nums = [1,1,2,3,3,4,4,7,8,8]` | Single element in middle | `2` |
| `nums = [3,3,7,7,10,11,11]` | Single element near end | `10` |
| `nums = [1,2,2,3,3,4,4]` | Single element at beginning | `1` |
| `nums = [1,1,2,2,3,3,4]` | Single element at end | `4` |
| `nums = [5]` | Array with single element | `5` |
| `nums = [1,1,2]` | Minimum case with single at end | `2` |
| `nums = [1,2,2]` | Minimum case with single at start | `1` |
| `nums = [1,1,2,2,3,3,4,4,5,5,6]` | Single at end of long array | `6` |

These test:
- Single element at different positions (start, middle, end)
- Minimum valid arrays (length 1, 3)
- Pattern disruption at various locations
- Boundary condition handling

## ☀️ Code

### Solution 1: XOR Approach (Simple but Not Optimal)
**Time: O(n) → Must scan entire array**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Approach: XOR all elements - paired elements cancel out
        
        This approach works but doesn't meet the O(log n) requirement.
        Used here to demonstrate basic understanding of the problem.
        """
        result = 0
        for num in nums:
            result ^= num
        return result
```

### Solution 2: Binary Search with Index Parity Analysis (Optimal)
**Time: O(log n) → Binary search eliminates half search space each iteration**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Approach: Binary search using index parity pattern analysis
        
        Key Insight:
        - Before single element: pairs start at even indices [0,1], [2,3], [4,5]...
        - After single element: pairs start at odd indices due to disruption
        - Check if nums[even] == nums[even+1] to determine search direction
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Ensure mid is even for consistent pattern checking
            if mid % 2 == 1:
                mid -= 1
            
            # Check if the pair starting at even index mid is complete
            if nums[mid] == nums[mid + 1]:
                # Pair is complete, single element must be on the right
                left = mid + 2
            else:
                # Pair is broken, single element is on the left (including mid)
                right = mid
        
        return nums[left]
```

### Solution 3: XOR Index Technique (Most Elegant)
**Time: O(log n) → Binary search eliminates half search space each iteration**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Elegant approach: Use XOR to find pair partner
        
        For any index i:
        - If i is even: partner should be at i+1
        - If i is odd: partner should be at i-1
        This can be computed elegantly as i^1 (XOR with 1)
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Find partner index using XOR trick
            # If mid is even: mid^1 = mid+1
            # If mid is odd: mid^1 = mid-1
            partner = mid ^ 1
            
            if nums[mid] == nums[partner]:
                # Pair is complete, single element is on the right
                left = mid + 1
            else:
                # Pair is broken, single element is on the left (including mid)
                right = mid
        
        return nums[left]
```

## ☀️ Notes

**Key Algorithm Components:**
- **Parity analysis template**: Modified binary search that detects pattern disruption
- **Even-index checking**: Ensures consistent pair analysis direction
- **Pattern recognition**: Identifies where pairing pattern breaks
- **Monotonic decision**: Parity provides reliable search direction

**Critical Insight:**
The algorithm works by recognizing that the single element disrupts the natural pairing pattern. Before the single element, all pairs start at even indices. After the single element, this pattern shifts, causing pairs to start at odd indices.

## ☀️ Parity Analysis Logic Explained

```
Array: [1,1,2,2,5,3,3,4,4]
Index:  0 1 2 3 4 5 6 7 8
Single element: 5 at index 4

Before single element (indices 0-3):
- Check even index 0: nums[0] == nums[1] ✓ (1 == 1)
- Check even index 2: nums[2] == nums[3] ✓ (2 == 2)
- Pattern intact: pairs start at even indices

After single element (indices 5-8):
- Check even index 6: nums[6] == nums[7] ✓ (3 == 4) ✗
- Pattern disrupted: pairs now start at odd indices

Binary search uses this pattern to determine search direction.
```

## ☀️ Coding Walkthrough Script

I need to find the single non-duplicate element in O(log n) time, which suggests binary search. But I can't search by value since I don't know what I'm looking for.
Instead, I'll use pattern analysis. In a normal array with all pairs, elements would be arranged as [a,a,b,b,c,c...], where pairs start at even indices: (0,1), (2,3), (4,5).
The single element disrupts this pattern. Before the single element, pairs still start at even indices. After the single element, everything shifts and pairs start at odd indices.
So my strategy is: at each step, I'll check if the pair starting at an even index is complete by comparing nums[even] with nums[even+1].
If they're equal, the pair is complete, meaning the single element hasn't appeared yet - it must be on the right side.
If they're not equal, the pattern is already broken, meaning the single element is on the left side, possibly at the current position.
I'll ensure my mid is always even by decrementing if it's odd, then apply this logic to guide my binary search. The search continues until left equals right, pointing to the single element."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| XOR All Elements | O(n) | O(1) | Mathematical cancellation | Simple but doesn't meet requirement |
| Parity Analysis | O(log n) | O(1) | Pattern disruption detection | **Optimal**; most intuitive |
| XOR Index Technique | O(log n) | O(1) | Elegant partner calculation | Most elegant; advanced technique |
| Linear Search | O(n) | O(1) | Direct comparison | Poor performance for large inputs |

## ☀️ Parity Analysis Insights

- **Prerequisites:** Array must be sorted with exactly one single element
- **Core insight:** Single element disrupts even-index pairing pattern
- **Template difference:** Analyzes pattern disruption vs searching for value
- **Decision criterion:** Parity check provides monotonic search direction
- **Comparison with standard binary search:** Different decision logic but same search structure
- **Mathematical guarantee:** Pattern analysis creates consistent left/right decisions

**Pattern Recognition:** This is a "disruption detection" template where we identify where a regular pattern breaks, then use binary search to locate the disruption point efficiently.

**Note:** Solution 1 demonstrates basic understanding but doesn't meet complexity requirements. Solution 2 is the recommended approach for interviews due to its clear parity logic. Solution 3 shows advanced mathematical insight with the XOR partner calculation technique.
