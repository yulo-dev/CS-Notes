# Leetcode 0162 - Find Peak Element

## ☀️ UMPIRE

**Understand:** A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array nums, find a peak element and return its index. If the array contains multiple peaks, return the index to any of the peaks. You may imagine that nums[-1] = nums[n] = -∞. You must write an algorithm that runs in O(log n) time.

**Match:** This is a Modified Binary Search problem on an unsorted array. The key insight is to use peak properties rather than sorted properties. We can apply binary search by utilizing the monotonic nature of peak existence, not array sorting.

**Plan:**
1. Use binary search to find any peak element
2. Compare nums[mid] with nums[mid + 1] to determine search direction
3. If nums[mid] > nums[mid + 1], peak exists on left side (including mid)
4. If nums[mid] <= nums[mid + 1], peak exists on right side (excluding mid)
5. Use while left < right for natural convergence to peak position

**Implement:** See the code section below.

**Review:**
- Ensure we meet the O(log n) time complexity requirement
- Verify that we handle boundary conditions properly
- Confirm the algorithm works with the guarantee of at least one peak
- Test with various peak positions (start, middle, end)

**Evaluate:**
- Time: O(log n) - binary search eliminates half search space each iteration
- Space: O(1) - only using constant extra space

## ☀️ Why This Is a Modified Binary Search Problem

This problem demonstrates binary search beyond sorted arrays:
- **Not based on sorting**: Array is unsorted but has peak properties
- **Guaranteed solution**: At least one peak always exists due to boundary conditions
- **Monotonic decision**: Each comparison gives definitive direction for search
- **Position convergence**: We converge to a position rather than find exact value

Key insights:
- Binary search works on any problem with monotonic decision property
- We don't need global ordering, just local comparison rules
- The boundary condition (nums[-1] = nums[n] = -∞) guarantees peak existence
- Each mid comparison eliminates exactly half the search space

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `nums = [1,2,3,1]` | Peak at index 2 | `2` |
| `nums = [1,2,1,3,5,6,4]` | Multiple peaks possible | `1` or `5` |
| `nums = [1]` | Single element | `0` |
| `nums = [1,2]` | Two elements, ascending | `1` |
| `nums = [2,1]` | Two elements, descending | `0` |
| `nums = [1,3,2,1]` | Peak in middle | `1` |
| `nums = [1,2,3,4,5]` | Ascending array, peak at end | `4` |
| `nums = [5,4,3,2,1]` | Descending array, peak at start | `0` |

These test:
- Various peak positions (start, middle, end)
- Single and multiple peak scenarios
- Monotonic sequences (ascending/descending)
- Minimum input size constraints

## ☀️ Code

### Solution 1: Linear Search (Naive Approach)
**Time: O(n) → May need to scan entire array**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Approach: Linear search to find any peak element
        
        This approach is straightforward but doesn't meet the O(log n) requirement.
        Used here to demonstrate the basic idea before optimization.
        """
        n = len(nums)
        
        for i in range(n):
            # Check if current element is a peak
            left_smaller = (i == 0) or (nums[i - 1] < nums[i])
            right_smaller = (i == n - 1) or (nums[i] > nums[i + 1])
            
            if left_smaller and right_smaller:
                return i
        
        # Should never reach here given problem constraints
        return 0
```

### Solution 2: Binary Search with Position Convergence (Optimal)
**Time: O(log n) → Binary search eliminates half search space each iteration**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Approach: Binary search with natural boundary handling
        
        Key Insight: We don't need to find a specific value, but converge to a peak position.
        Use while left < right to let boundaries converge to the answer.
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[mid + 1]:
                # Peak exists on left side (including mid)
                right = mid  # Keep mid as potential answer
            else:
                # Peak exists on right side (excluding mid)
                left = mid + 1
        
        # When left == right, we found the peak
        return left
```

## ☀️ Notes

**Key Algorithm Components:**
- **Peak property utilization**: Compare adjacent elements to determine search direction
- **Boundary guarantee**: nums[-1] = nums[n] = -∞ ensures at least one peak exists
- **Position convergence**: Use while left < right for natural boundary convergence
- **Monotonic decision**: Each comparison provides definitive search direction

**Critical Insight:**
The algorithm works because of the guaranteed peak existence and the property that comparing nums[mid] with nums[mid + 1] always gives us a definitive direction where a peak must exist.

## ☀️ Algorithm Logic Explained

```
Array: [1, 2, 1, 3, 5, 6, 4]
Conceptual: [-∞, 1, 2, 1, 3, 5, 6, 4, -∞]

Binary Search Process:
1. Compare nums[mid] with nums[mid + 1]
2. If nums[mid] > nums[mid + 1]: declining slope → peak on left (including mid)
3. If nums[mid] < nums[mid + 1]: ascending slope → peak on right (excluding mid)
4. Continue until left == right (convergence to peak)
```

## ☀️ Coding Walkthrough Script

"I need to find any peak element in O(log n) time, which suggests binary search.
The key insight is that I don't need the array to be sorted. Instead, I can use the peak property: a peak is greater than both neighbors.
Since the problem guarantees at least one peak exists (due to boundary conditions where edges are considered -∞), I can use binary search to converge to a peak position.
I'll compare nums[mid] with nums[mid + 1]:
- If nums[mid] > nums[mid + 1], there's a declining slope, so a peak must exist on the left side including mid
- If nums[mid] < nums[mid + 1], there's an ascending slope, so a peak must exist on the right side excluding mid
I'll use while left < right because I want the boundaries to converge to a peak position, rather than searching for a specific value. When left equals right, I've found my peak.
This approach guarantees O(log n) time by eliminating half the search space in each iteration."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Linear Search | O(n) | O(1) | Check each position for peak | Simple but doesn't meet requirement |
| Binary Search | O(log n) | O(1) | Position convergence with peak properties | **Optimal**; meets requirement |
| Recursive Binary Search | O(log n) | O(log n) | Same logic with recursion | Higher space due to call stack |

## ☀️ Peak Finding Insights

- **Prerequisites:** Array with guaranteed peak existence (boundary conditions)
- **Core insight:** Use local comparison instead of global sorting
- **Template choice:** while left < right for position convergence
- **Decision making:** Each comparison eliminates exactly half the search space
- **Convergence guarantee:** Boundaries will meet at a peak position
- **Boundary handling:** Natural avoidance of index out of bounds

**Mathematical Guarantee:** Given the boundary conditions (conceptual -∞ at edges) and the property that adjacent elements are never equal, at least one peak must exist. Binary search will efficiently converge to any such peak.

**Note:** This problem showcases how binary search can be applied beyond sorted arrays to any problem with monotonic decision properties. The key is recognizing that we're converging to a position (peak) rather than searching for a specific value.
