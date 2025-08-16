# Leetcode 0035 - Search Insert Position

## ☀️ UMPIRE

**Understand:** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

**Match:** This is a Binary Search problem. The key insight is that we need to find either the exact position of the target or the position where it should be inserted to maintain sorted order.

**Plan:**
1. Use binary search with left and right pointers
2. For each iteration, compare middle element with target
3. If target is found, return the index
4. If target is smaller, search left half
5. If target is larger, search right half
6. When search ends, left pointer will be at the correct insertion position

**Implement:** See the code section below.

**Review:**
- Ensure we handle the case when target is not found
- Verify that left pointer gives correct insertion position
- Handle edge cases like empty array and target at boundaries

**Evaluate:**
- Time: O(log n) - we eliminate half of the search space each iteration
- Space: O(1) - only using constant extra space

## ☀️ Why This Is a Binary Search Problem

The sorted array property allows us to use binary search effectively:
- **Sorted order is maintained** throughout the entire array
- We can make reliable comparisons to eliminate half the search space
- When target is not found, the search naturally converges to insertion point
- The left pointer after search completion indicates where target should be inserted

Key insights:
- Standard binary search works directly since array is fully sorted
- No need for complex logic like rotated arrays
- The insertion position is naturally found when search terminates
- Left pointer will point to the first element greater than target

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `nums = [1,3,5,6], target = 5` | Target exists in array | `2` |
| `nums = [1,3,5,6], target = 2` | Target should be inserted | `1` |
| `nums = [1,3,5,6], target = 7` | Target larger than all elements | `4` |
| `nums = [1,3,5,6], target = 0` | Target smaller than all elements | `0` |
| `nums = [1], target = 1` | Single element, target found | `0` |
| `nums = [1], target = 0` | Single element, insert before | `0` |
| `nums = [1], target = 2` | Single element, insert after | `1` |

These test:
- Target exists in array
- Target needs insertion at various positions
- Boundary conditions (beginning, end)
- Minimal input sizes
- Edge positions for insertion

## ☀️ Code

### Solution 1: Linear Search 
**Time: O(n) → Need to scan through array in worst case**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Scan from left to right
        for i in range(len(nums)):
            # If we find target or a number larger than target
            if nums[i] >= target:
                return i
        
        # If target is larger than all elements, insert at end
        return len(nums)
```

### Solution 2: Binary Search 
**Time: O(log n) → We eliminate half of the search space in each iteration**  
**Space: O(1) → Only using constant extra space for pointers**

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target is in the right half
                left = mid + 1
            else:
                # Target is in the left half
                right = mid - 1
        
        # When loop ends, left is the insertion position
        # This works because:
        # - If target > all elements, left will be len(nums)
        # - If target < all elements, left will be 0
        # - Otherwise, left points to the first element > target
        return left
```

## ☀️ Notes

**Key Algorithm Components:**
- Standard binary search pattern with left and right pointers
- `nums[mid] < target` determines which half to search
- When target not found, left pointer naturally points to insertion position
- No special handling needed for insertion logic

**Critical Insight:**
The algorithm works because when binary search terminates without finding the target, the left pointer will be positioned at the exact location where the target should be inserted to maintain sorted order.

## ☀️ Coding Walkthrough Script

"I'll solve this using binary search to achieve O(log n) time complexity.
First, I initialize left and right pointers to span the entire array.
In each iteration, I calculate the middle index and compare nums[mid] with the target.
If I find the target exactly, I return the middle index immediately.
If nums[mid] is less than target, the target must be in the right half, so I move left pointer to mid + 1.
If nums[mid] is greater than target, the target must be in the left half, so I move right pointer to mid - 1.

The key insight is that when the loop terminates, the left pointer will be positioned exactly where the target should be inserted. This happens naturally because:
- If target is larger than all elements, left ends up at nums.length
- If target is smaller than all elements, left stays at 0  
- Otherwise, left points to the first element greater than target

This elegant property eliminates the need for separate insertion logic."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Linear Search | O(n) | O(1) | Check every element | Simple but inefficient |
| Binary Search | O(log n) | O(1) | Divide and conquer | **Recommended**; meets requirement |
| Built-in bisect | O(log n) | O(1) | Library function | Not allowed in interviews |

## ☀️ Binary Search Insights

- **Prerequisite:** Array must be sorted in ascending order
- **Core insight:** Elimination of half the search space each iteration
- **Decision making:** Compare middle element with target to determine direction
- **Insertion position:** Left pointer naturally converges to correct position
- **Termination condition:** When left > right, search space is exhausted
- **Position guarantee:** Left pointer indicates where target belongs

**Mathematical Guarantee:** Since the array is sorted, continued bisection will eventually isolate the exact position where target exists or should be inserted, with the left pointer marking this location.

**Note:** Solution 1 is straightforward but inefficient for large arrays.
Solution 2 leverages the sorted property with binary search for optimal performance.
The key insight in Solution 2 is that when the loop terminates, 'left' naturally points to the correct insertion position.
