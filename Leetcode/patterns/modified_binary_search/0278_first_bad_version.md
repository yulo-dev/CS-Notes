# Leetcode 0278 - First Bad Version

## ☀️ UMPIRE

**Understand:** You are a product manager with n versions [1, 2, ..., n]. All versions after a bad version are also bad. Given an API `bool isBadVersion(version)`, find the first bad version while minimizing API calls.

**Match:** This is a Modified Binary Search problem, specifically a left boundary search. The versions form a pattern: [good, good, ..., good, bad, bad, ..., bad]. We need to find the transition point from good to bad.

**Plan:**
1. Use binary search on the version range [1, n]
2. When isBadVersion(mid) returns true, search left for earlier bad versions
3. When isBadVersion(mid) returns false, search right for bad versions
4. Continue until we find the leftmost bad version

**Implement:** See the code section below.

**Review:**
- Ensure we minimize API calls with O(log n) solution
- Verify boundary conditions when first/last version is bad
- Handle potential integer overflow in mid calculation
- Test with edge cases like n=1

**Evaluate:**
- Time: O(log n) - binary search eliminates half the search space each iteration
- Space: O(1) - only using constant extra space

## ☀️ Why This Is a Modified Binary Search Problem

This problem has the perfect structure for binary search:
- **Sorted property**: Versions have a clear order [1, 2, ..., n]
- **Monotonic property**: Once a version is bad, all subsequent versions are bad
- **Boundary search**: We need to find the transition point from good to bad
- **Search space reduction**: Each comparison eliminates half the remaining versions

Key insights:
- This is NOT a standard "find target" binary search
- This IS a "find first occurrence" boundary search
- Similar to LeetCode 34's findLeft function
- We're looking for the leftmost position where isBadVersion returns true

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `n = 5, bad = 4` | Standard case with bad version in middle | `4` |
| `n = 1, bad = 1` | Single version, it's bad | `1` |
| `n = 10, bad = 1` | First version is bad | `1` |
| `n = 10, bad = 10` | Last version is bad | `10` |
| `n = 100, bad = 50` | Bad version exactly in middle | `50` |
| `n = 2^31-1, bad = large` | Maximum constraint test | `large` |

These test:
- Boundary positions (first, last, middle)
- Single element case
- Large input handling
- Various bad version positions
- Integer overflow prevention

## ☀️ Code

### Solution 1: Linear Search (Naive Approach)
**Time: O(n) → May need to check every version**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Approach: Linear search from version 1 to n
        
        This approach is straightforward but inefficient.
        It doesn't utilize the sorted property of the problem.
        """
        for version in range(1, n + 1):
            if isBadVersion(version):
                return version
        
        return n  # Should never reach here
```

### Solution 2: Binary Search with Left Boundary Template (Optimal)
**Time: O(log n) → Binary search eliminates half search space each iteration**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Approach: Binary search to find the first bad version
        
        Key Insight:
        - This is a left boundary search problem
        - Use the same template as LeetCode 34 (Find First and Last Position)
        - When we find a bad version, continue searching left for earlier bad versions
        """
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2  # Prevent overflow
            
            if isBadVersion(mid):
                # Found a bad version, but search left for the first one
                right = mid - 1
            else:
                # Current version is good, first bad version is to the right
                left = mid + 1
        
        # When loop ends, left points to the first bad version
        return left
```

### Solution 3: Alternative Binary Search Template
**Time: O(log n) → Binary search eliminates half search space each iteration**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Alternative binary search template using while left < right
        
        Note: This template requires different boundary handling
        """
        left, right = 1, n
        
        while left < right:  # No equal sign
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # mid might be the first bad version, so don't exclude it
                right = mid  # Not mid - 1
            else:
                # mid is definitely not the first bad version
                left = mid + 1
        
        # When loop ends, left == right, pointing to first bad version
        return left
```

### Solution 4: Binary Search with Recording (Consistent with LeetCode 34)
**Time: O(log n) → Binary search eliminates half search space each iteration**  
**Space: O(1) → Only using constant extra space**

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Binary search with explicit recording of found bad versions
        This style is consistent with LeetCode 34 approach
        """
        left, right = 1, n
        first_bad = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                first_bad = mid  # Record this bad version
                right = mid - 1  # Continue searching left for earlier ones
            else:
                left = mid + 1   # Search right for bad versions
        
        return first_bad
```

## ☀️ Notes

**Key Algorithm Components:**
- **Left boundary search**: Find the first occurrence of a condition becoming true
- **Monotonic property**: Exploit the fact that bad versions are consecutive from some point
- **API minimization**: Binary search reduces calls from O(n) to O(log n)
- **Overflow prevention**: Use `left + (right - left) // 2` instead of `(left + right) // 2`

**Critical Insight:**
This problem is essentially finding the boundary between two regions: good versions and bad versions. The binary search efficiently narrows down to this transition point by eliminating half the search space in each iteration.

## ☀️ Binary Search Logic Explained

```
Versions: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Status:   [G, G, G, B, B, B, B, B, B, B ]  (G=Good, B=Bad)
Target: Find first B (position 4)

Binary Search Process:
1. Check middle (5): Bad → search left half for earlier bad
2. Check middle of left (2): Good → search right for first bad  
3. Check middle of remaining (4): Bad → this is our answer
```

## ☀️ Coding Walkthrough Script

"I need to find the first bad version while minimizing API calls, which suggests using binary search.
The key insight is that this forms a sorted pattern: all good versions come before all bad versions. I'm looking for the boundary - the first position where the condition changes from false to true.
I'll use binary search on the range [1, n]. For each middle version, I'll call isBadVersion:
If it returns true, I've found a bad version, but I need to check if there's an earlier bad version, so I'll search the left half.
If it returns false, the first bad version must be to the right, so I'll search the right half.
I'll continue this process until the search space is exhausted. At that point, my left pointer will be positioned at the first bad version.
This approach gives me O(log n) API calls instead of O(n), which significantly minimizes the number of calls as required."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | API Calls | Key Strategy | Notes |
|--------|----------------|------------------|-----------|--------------|-------|
| Linear Search | O(n) | O(1) | O(n) | Check versions sequentially | Simple but inefficient |
| Binary Search (Template 1) | O(log n) | O(1) | O(log n) | Left boundary search | **Recommended**; consistent with LeetCode 34 |
| Binary Search (Template 2) | O(log n) | O(1) | O(log n) | Alternative boundary search | Valid but different boundary handling |
| Binary Search (Recording) | O(log n) | O(1) | O(log n) | Explicit recording approach | Consistent with recording pattern |

## ☀️ Binary Search Boundary Insights

- **Prerequisites:** Monotonic property (good versions followed by bad versions)
- **Core insight:** Find transition point between two distinct regions
- **Template choice:** Use consistent boundary search template across problems
- **API efficiency:** Binary search minimizes expensive API calls
- **Boundary guarantee:** Left pointer converges to first bad version
- **Overflow safety:** Always use safe mid calculation for large inputs

**Mathematical Guarantee:** Since versions form a monotonic sequence (good then bad), binary search will correctly identify the transition point in logarithmic time, minimizing API calls while guaranteeing the correct first bad version.

**Note:** Solution 2 is recommended for its consistency with other boundary search problems like LeetCode 34. The template `while left <= right` with appropriate boundary updates provides a reliable pattern for similar problems.
