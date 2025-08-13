# Leetcode 0033 - Search in Rotated Sorted Array

## ☀️ UMPIRE

**Understand:** There is an integer array `nums` sorted in ascending order (with distinct values). Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (where `1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`. Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

**Match:** This is a modified Binary Search problem. The key insight is that even though the array is rotated, at least one half of any subarray will always be completely sorted. We can leverage this property to determine which side to search.

**Plan:**
1. Use binary search with left and right pointers
2. For each iteration, determine which half is completely sorted
3. Check if target lies within the sorted half's range
4. If yes, search the sorted half; if no, search the other half
5. Continue until target is found or search space is exhausted

**Implement:** See the code section below.

**Review:**
- Ensure we correctly identify which side is sorted using `nums[left] <= nums[mid]`
- Verify range checks for target within sorted portions
- Handle edge cases like single elements and no rotation

**Evaluate:**
- Time: O(log n) - we eliminate half of the search space each iteration
- Space: O(1) - only using constant extra space

## ☀️ Why This Is a Modified Binary Search Problem

The rotation breaks the global sorted property but preserves a crucial characteristic:
- **At least one half is always completely sorted**
- We can determine which half is sorted by comparing endpoints
- Within the sorted half, we can make reliable range comparisons
- This allows us to eliminate half the search space in each iteration

Key insights:
- Normal binary search fails because rotation disrupts global ordering
- We must first identify the "trustworthy" (sorted) side
- Only in sorted regions can we reliably determine if target exists within range
- The unsorted side will become sorted in subsequent iterations as range shrinks

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `nums = [4,5,6,7,0,1,2], target = 0` | Standard rotated array | `4` |
| `nums = [4,5,6,7,0,1,2], target = 3` | Target not in array | `-1` |
| `nums = [1], target = 0` | Single element, target not found | `-1` |
| `nums = [1], target = 1` | Single element, target found | `0` |
| `nums = [1,3], target = 3` | Two elements, no rotation | `1` |
| `nums = [3,1], target = 1` | Two elements, rotated | `1` |
| `nums = [4,5,6,7,0,1,2], target = 4` | Target at rotation boundary | `0` |

These test:
- Standard rotation scenarios
- Target at rotation boundaries  
- Minimal input sizes
- No rotation cases
- Target not present in array

## ☀️ Code

### Solution 1: Binary Search with Ordered Side Detection (標準解法)
**Time: O(log n) → We eliminate half of the search space in each iteration**  
**Space: O(1) → Only using constant extra space for pointers**

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            
            # Determine which side is ordered
            if nums[left] <= nums[mid]:
                # Left side is ordered
                if nums[left] <= target < nums[mid]:
                    # Target is in the ordered left side
                    right = mid - 1
                else:
                    # Target is in the right side (may cross rotation point)
                    left = mid + 1
            else:
                # Right side is ordered
                if nums[mid] < target <= nums[right]:
                    # Target is in the ordered right side
                    left = mid + 1
                else:
                    # Target is in the left side (may cross rotation point)
                    right = mid - 1
        
        # Target not found
        return -1
```

### Solution 2: Binary Search with Rotation Point Analysis (進階解法)
**Time: O(log n) → Same time complexity but more explicit logic**  
**Space: O(1) → Only using constant extra space for pointers**

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Found the target
            if nums[mid] == target:
                return mid
            
            # Check if left side has no rotation (is sorted)
            if nums[left] <= nums[mid]:
                # Left side is sorted normally
                if target >= nums[left] and target < nums[mid]:
                    # Target lies within the sorted left portion
                    right = mid - 1
                else:
                    # Target must be in right portion (which may contain rotation)
                    left = mid + 1
            else:
                # Right side is sorted normally (left side contains rotation)
                if target > nums[mid] and target <= nums[right]:
                    # Target lies within the sorted right portion
                    left = mid + 1
                else:
                    # Target must be in left portion (which contains rotation)
                    right = mid - 1
        
        return -1
```

## ☀️ Notes

**Key Algorithm Components:**
- `nums[left] <= nums[mid]` determines which side is sorted
- Range checks like `nums[left] <= target < nums[mid]` only work on sorted sides
- We use elimination: if target is definitely not in the sorted side, it must be in the other side
- The rotation point will eventually be isolated as the search range shrinks

**Critical Insight:**
The algorithm works because rotation creates exactly one "break point" in the array. As we continue dividing the search space, subarrays will eventually become completely sorted (not containing the break point).

## ☀️ Coding Walkthrough Script

"I'll solve this using modified binary search that accounts for the rotation.

First, I initialize left and right pointers to span the entire array.

In each iteration, I calculate the middle index and check if it equals our target.

The key insight is that despite rotation, at least one half is always completely sorted. I determine which side is sorted by comparing nums[left] with nums[mid]. If nums[left] is less than or equal to nums[mid], the left side is sorted.

Once I identify the sorted side, I can reliably check if the target lies within that sorted range. For the left side, I check if target is between nums[left] and nums[mid]. If the target is in the sorted range, I search that side by updating the appropriate pointer.

If the target is not in the sorted side, it must be in the other side regardless of whether that side is sorted or not. This works because of the elimination principle.

I continue this process until I find the target or exhaust the search space. The algorithm guarantees that unsorted regions will become sorted as the range shrinks, since there's only one rotation point."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Linear Search | O(n) | O(1) | Check every element | Ignores any structure |
| Standard Binary Search | O(log n) | O(1) | **FAILS** on rotated arrays | Cannot handle rotation |
| Rotated Binary Search | O(log n) | O(1) | Identify sorted side first | **Recommended**; optimal and reliable |
| Find Pivot + Binary Search | O(log n) | O(1) | Two-phase approach | More complex, same efficiency |

## ☀️ Rotated Binary Search Insights

- **Prerequisite:** Array was originally sorted before rotation
- **Core insight:** At least one half is always completely sorted
- **Decision making:** Use sorted side for reliable range checking
- **Elimination principle:** If target not in sorted side, must be in other side
- **Convergence:** Rotation point gets isolated as search range shrinks
- **Range checking:** Only meaningful within sorted portions

**Mathematical Guarantee:** Since there's exactly one rotation point, continued bisection will eventually create subarrays that don't contain the rotation point, making them completely sorted and searchable with standard binary search logic.

**Note:** Solution 1 is the most recommended approach using clear logical conditions to identify the ordered side. 
Solution 2 provides more explicit comments about rotation analysis but follows the same core logic. 
Both solutions efficiently handle the rotation by leveraging the fact that at least one side is always completely sorted.
