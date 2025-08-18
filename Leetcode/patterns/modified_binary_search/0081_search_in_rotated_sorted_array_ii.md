# Leetcode 0081 - Search in Rotated Sorted Array II

## ☀️ UMPIRE

**Understand:** Given a rotated sorted array that may contain duplicates, determine if a target value exists in the array. The array was originally sorted in non-decreasing order before rotation. You must optimize the operation steps as much as possible.

**Match:** This is a Modified Binary Search problem with duplicate handling. The key insight is that duplicates can create ambiguity in determining which half of the array is sorted, requiring special handling to eliminate duplicates when they interfere with the binary search logic.

**Plan:**
1. Use binary search as the primary approach
2. Handle the duplicate ambiguity case: when nums[left] == nums[mid] == nums[right]
3. When ambiguity occurs, eliminate boundary duplicates to restore determinism
4. Apply standard rotated array binary search logic for non-ambiguous cases
5. Continue until target is found or search space is exhausted

**Implement:** See the code section below.

**Review:**
- Verify duplicate handling doesn't miss the target
- Ensure the algorithm handles all rotation cases correctly
- Test edge cases with heavy duplicates
- Confirm time complexity analysis (O(log n) average, O(n) worst case)

**Evaluate:**
- Time: O(log n) average case, O(n) worst case due to duplicates
- Space: O(1) - only using constant extra space

## ☀️ Why This Is a Modified Binary Search Problem

This problem extends the rotated sorted array search with duplicate complexity:
- **Standard rotated search**: Can always determine which half is sorted
- **With duplicates**: nums[left] == nums[mid] == nums[right] creates ambiguity
- **Ambiguity resolution**: Must eliminate duplicates to restore binary search properties
- **Worst-case degradation**: Heavy duplicates can force linear-time behavior

Key insights:
- Rotation creates two sorted halves, but duplicates can mask the rotation point
- When we can't determine which half is sorted, we eliminate boundary duplicates
- The duplicate elimination process can degrade performance to O(n) in worst case
- This is unavoidable - duplicates fundamentally limit our ability to eliminate half the search space

## ☀️ Duplicate Ambiguity Analysis

```
Example of ambiguity:
Array: [1,1,1,0,1,1,1], target = 0
Index:  0 1 2 3 4 5 6

At some point: left=0, mid=3, right=6
nums[left] = 1, nums[mid] = 0, nums[right] = 1

We can determine: left half [1,1,1] vs right half [1,1,1]
But when: nums[left] == nums[mid] == nums[right] = 1
We cannot tell which half contains the rotation point!

Solution: Shrink boundaries by eliminating duplicates
left++ and right-- until we can make a determination
```

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `nums = [2,5,6,0,0,1,2], target = 0` | Target exists with duplicates | `true` |
| `nums = [2,5,6,0,0,1,2], target = 3` | Target doesn't exist | `false` |
| `nums = [1,0,1,1,1], target = 0` | Heavy duplicates with target | `true` |
| `nums = [1,1,1,1,1], target = 2` | All duplicates, target not found | `false` |
| `nums = [1], target = 1` | Single element, target found | `true` |
| `nums = [1,1], target = 1` | All elements same, target found | `true` |
| `nums = [1,3,1,1,1], target = 3` | Target in non-duplicated region | `true` |
| `nums = [3,1,2,3,3,3,3], target = 2` | Complex rotation with duplicates | `true` |

These test:
- Different duplicate distributions
- Target in various positions relative to rotation
- Worst-case scenarios with heavy duplicates
- Boundary conditions and single elements

## ☀️ Code

### Solution 1: Linear Search (Naive Approach)
**Time: O(n) → Must scan entire array**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Approach: Linear search through the array
        
        This approach is straightforward but doesn't take advantage 
        of the sorted nature of the rotated array.
        """
        return target in nums
        
        # Alternative explicit implementation:
        # for num in nums:
        #     if num == target:
        #         return True
        # return False
```

### Solution 2: Binary Search with Duplicate Handling (Optimal)
**Time: O(log n) average, O(n) worst case → Binary search with duplicate elimination**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Approach: Modified binary search for rotated array with duplicates
        
        Key Insights:
        1. Array is rotated, so one half is always sorted
        2. Duplicates can make it ambiguous which half is sorted
        3. When nums[left] == nums[mid] == nums[right], eliminate boundaries
        4. Apply standard rotated array logic when no ambiguity
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Found target
            if nums[mid] == target:
                return True
            
            # Handle duplicates: when left, mid, right are all equal
            # We can't determine which half is sorted, so eliminate boundaries
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                # Check if target is in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left half
                else:
                    left = mid + 1   # Search right half
            else:  # Right half is sorted (nums[mid] < nums[right])
                # Check if target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Search right half
                else:
                    right = mid - 1  # Search left half
        
        return False
```

### Solution 3: Optimized Duplicate Elimination
**Time: O(log n) average, O(n) worst case → Binary search with pre-processing**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Optimized approach: Pre-eliminate boundary duplicates
        
        Instead of eliminating duplicates one by one during search,
        we can remove boundary duplicates more aggressively upfront.
        """
        left, right = 0, len(nums) - 1
        
        # Remove duplicates from left boundary
        while left < right and nums[left] == nums[left + 1]:
            left += 1
        
        # Remove duplicates from right boundary  
        while left < right and nums[right] == nums[right - 1]:
            right -= 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            
            # Handle remaining duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            
            # Standard rotated array binary search logic
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
        
        return False
```

## ☀️ Notes

**Key Algorithm Components:**
- **Duplicate detection**: Identify when duplicates create ambiguity
- **Boundary elimination**: Remove duplicates that interfere with binary search
- **Sorted half identification**: Determine which half maintains sorted order
- **Range checking**: Verify if target falls within the sorted half's range

**Critical Insight:**
The algorithm handles the fundamental challenge that duplicates can make it impossible to determine which half of a rotated array is sorted. The duplicate elimination process is necessary but can degrade performance to linear time in worst-case scenarios.

## ☀️ Duplicate Handling Logic Explained

```
Array: [1,1,1,0,1,1,1], searching for 0
Index:  0 1 2 3 4 5 6

Step 1: left=0, mid=3, right=6
nums[0]=1, nums[3]=0, nums[6]=1
Left half appears sorted: nums[0] <= nums[3] (1 <= 0) ✗
Right half appears sorted: nums[3] <= nums[6] (0 <= 1) ✓
Target 0 in range [0,1]? Yes → search right half

But what if mid=1?
nums[0]=1, nums[1]=1, nums[6]=1
All equal! Cannot determine which half is sorted.
Solution: left++, right-- to eliminate boundary duplicates.
```

## ☀️ Coding Walkthrough Script

This problem is an extension of the classic rotated sorted array search, but with duplicates that can create ambiguity.
My approach uses binary search as the foundation, but I need to handle the case where duplicates make it impossible to determine which half is sorted.
The key insight is that in a rotated sorted array, one half is always sorted. I can identify the sorted half by comparing nums[left] with nums[mid]. If nums[left] <= nums[mid], the left half is sorted. Otherwise, the right half is sorted.
However, when nums[left] == nums[mid] == nums[right], I can't make this determination because duplicates mask the rotation point. In this case, I eliminate the boundary duplicates by incrementing left and decrementing right, then continue the search.
Once I identify the sorted half, I check if the target falls within that half's range. If yes, I search that half; otherwise, I search the other half.
The worst-case time complexity becomes O(n) when the array has many duplicates, because I might need to eliminate up to n/2 duplicates. This degradation is unavoidable - duplicates fundamentally limit our ability to eliminate half the search space in all cases.

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Linear Search | O(n) | O(1) | Direct iteration | Simple but ignores sorted property |
| Modified Binary Search | O(log n) avg, O(n) worst | O(1) | Duplicate elimination + binary search | **Optimal average case** |
| Optimized Elimination | O(log n) avg, O(n) worst | O(1) | Pre-process + binary search | Better constants, same complexity |
| Two-pass approach | O(n) | O(1) | Find rotation + binary search | Always O(n), not recommended |

## ☀️ Complexity Analysis Insights

- **Why O(n) worst case is unavoidable:** When array is mostly duplicates (e.g., [1,1,1,1,0,1,1,1,1]), we may need to check every element to distinguish rotation from duplicates
- **Average case analysis:** For typical inputs with moderate duplicates, binary search properties are preserved most of the time
- **Comparison with LC 33:** Without duplicates, we can always determine sorted half in O(1), guaranteeing O(log n)
- **Practical performance:** Despite O(n) worst case, performs well on real-world data with limited duplicates

**Algorithm Classification:** This represents a "degraded binary search" where external factors (duplicates) can force worst-case linear behavior, but optimal logarithmic performance is maintained when those factors don't interfere.

**Note:** Solution 1 shows understanding but doesn't leverage the problem structure. Solution 2 is the standard interview solution that balances clarity with optimality. Solution 3 demonstrates optimization thinking while maintaining the same complexity bounds.
