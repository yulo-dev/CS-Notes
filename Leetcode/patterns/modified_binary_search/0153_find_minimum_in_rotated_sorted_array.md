# Leetcode 0153 - Find Minimum in Rotated Sorted Array

## ☀️ UMPIRE

**Understand:** Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Given the array nums after possible rotation, return the minimum element. You must write an algorithm that runs in O(log n) time. All integers are unique.

**Match:** This is a Modified Binary Search problem on a rotated sorted array. The key insight is to find the rotation point, which always contains the minimum element. We use position convergence approach similar to peak finding.

**Plan:**
1. Use binary search to find the rotation point (minimum element)
2. Compare nums[mid] with nums[right] to determine which side contains rotation
3. If nums[mid] > nums[right]: rotation point is on right side
4. If nums[mid] <= nums[right]: left side is sorted or mid is the minimum
5. Use while left < right for position convergence to minimum

**Implement:** See the code section below.

**Review:**
- Ensure we meet the O(log n) time complexity requirement
- Verify we compare nums[mid] with nums[right] (not nums[left])
- Confirm the algorithm handles all rotation scenarios
- Test edge cases like no rotation and single element

**Evaluate:**
- Time: O(log n) - binary search eliminates half search space each iteration
- Space: O(1) - only using constant extra space

## ☀️ Why This Is a Modified Binary Search Problem

This problem showcases binary search beyond standard sorted arrays:
- **Rotated structure**: Array is sorted but with one rotation point
- **Guaranteed minimum**: Exactly one minimum element always exists
- **Monotonic decision**: Comparing nums[mid] with nums[right] gives definitive direction
- **Position convergence**: We converge to the minimum position rather than search for specific value

Key insights:
- The minimum element is always at the rotation point
- Rotation creates at most one "break" in the sorted order
- Each comparison eliminates exactly half the search space
- We use structural properties rather than value-based searching

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `nums = [3,4,5,1,2]` | Rotated 3 times | `1` |
| `nums = [4,5,6,7,0,1,2]` | Rotated 4 times | `0` |
| `nums = [11,13,15,17]` | No rotation | `11` |
| `nums = [2,1]` | Two elements | `1` |
| `nums = [1]` | Single element | `1` |
| `nums = [2,3,4,5,1]` | Minimum at end | `1` |
| `nums = [5,1,2,3,4]` | Minimum near start | `1` |
| `nums = [1,2,3,4,5]` | No rotation | `1` |

These test:
- Various rotation amounts (0 to n-1)
- Different minimum positions
- Boundary conditions (start, end, middle)
- Minimum input size constraints
- Edge rotations

## ☀️ Code

### Solution 1: Linear Search (Naive Approach)
**Time: O(n) → May need to scan entire array**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Approach: Linear search to find minimum element
        
        This approach is straightforward but doesn't meet the O(log n) requirement.
        Simply iterate through the array to find the minimum value.
        """
        min_val = nums[0]
        
        for num in nums:
            if num < min_val:
                min_val = num
        
        return min_val
```

### Solution 2: Binary Search with Position Convergence (Optimal)
**Time: O(log n) → Binary search eliminates half search space each iteration**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Approach: Binary search to find the rotation point (minimum element)
        
        Key Insight:
        - Compare nums[mid] with nums[right] to determine rotation side
        - If nums[mid] > nums[right]: rotation point is on right side
        - If nums[mid] <= nums[right]: left side is sorted or mid is minimum
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # Right side contains the rotation point (minimum)
                left = mid + 1
            else:
                # Left side is sorted, or mid is the minimum
                right = mid
        
        # When left == right, we found the minimum element
        return nums[left]
```

## ☀️ Notes

**Key Algorithm Components:**
- **Rotation point identification**: Minimum element is always at rotation point
- **Right comparison strategy**: Compare nums[mid] with nums[right] for monotonic decision
- **Position convergence**: Use while left < right to converge to minimum position
- **Boundary preservation**: Use right = mid to preserve potential minimum

**Critical Insight:**
The algorithm works because a rotated sorted array has exactly one rotation point, and the minimum element is always located at this rotation point. By comparing the middle element with the rightmost element, we can always determine which side contains the rotation.

## ☀️ Rotation Point Analysis

```
Original: [1, 2, 3, 4, 5]

No rotation:    [1, 2, 3, 4, 5] → min at index 0
Rotate 1 time:  [5, 1, 2, 3, 4] → min at index 1  
Rotate 2 times: [4, 5, 1, 2, 3] → min at index 2
Rotate 3 times: [3, 4, 5, 1, 2] → min at index 3
Rotate 4 times: [2, 3, 4, 5, 1] → min at index 4

Pattern: Rotation point = minimum element position
```

## ☀️ Why Compare with nums[right]?

```python
# Comparing with right gives clear monotonic decision:

if nums[mid] > nums[right]:
    # Example: [4,5,6,7,0,1,2], mid=3, nums[3]=7, nums[6]=2
    # 7 > 2 → rotation point must be on right side
    left = mid + 1
    
else:  # nums[mid] <= nums[right]
    # Example: [4,5,6,7,0,1,2], mid=5, nums[5]=1, nums[6]=2  
    # 1 < 2 → left side is sorted or mid is minimum
    right = mid
```

## ☀️ Coding Walkthrough Script

I need to find the minimum element in a rotated sorted array in O(log n) time.
The key insight is that the minimum element is always at the rotation point. In a rotated sorted array, there's exactly one point where the order breaks - that's where the minimum is located.
I'll use binary search by comparing nums[mid] with nums[right]:
If nums[mid] is greater than nums[right], this means there's a rotation point somewhere on the right side, because in a properly sorted portion, the middle should be less than the right end.
If nums[mid] is less than or equal to nums[right], this means the right portion is properly sorted, so the minimum must be on the left side or at mid itself.
I'll use while left < right because I want to converge to the minimum position. The minimum is guaranteed to exist, so when left equals right, I've found it.
This approach eliminates half the search space in each iteration, giving me O(log n) time complexity."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Linear Search | O(n) | O(1) | Scan entire array | Simple but doesn't meet requirement |
| Binary Search | O(log n) | O(1) | Position convergence to rotation point | **Optimal**; meets requirement |
| Find Rotation + Binary Search | O(log n) | O(1) | Two-phase approach | More complex, same efficiency |

## ☀️ Rotation Point Binary Search Insights

- **Prerequisites:** Rotated sorted array with unique elements
- **Core insight:** Minimum element is always at rotation point
- **Comparison strategy:** nums[mid] vs nums[right] gives monotonic decision
- **Template choice:** while left < right for position convergence
- **Boundary handling:** right = mid preserves potential minimum
- **Convergence guarantee:** Boundaries will meet at minimum position

**Mathematical Guarantee:** Since a rotated sorted array has exactly one rotation point and the minimum element is always at this point, binary search with proper comparison strategy will converge to the minimum in logarithmic time.

**Template Similarity:** This problem uses the same while left < right template as LeetCode 162 (Find Peak Element) because both are position convergence problems where the answer is guaranteed to exist.

**Note:** This solution assumes no duplicate elements. For arrays with duplicates, see LeetCode 154 which requires additional handling for ambiguous cases.
