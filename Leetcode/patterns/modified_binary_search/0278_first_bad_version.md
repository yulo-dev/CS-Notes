# Leetcode 0278 - First Bad Version

## ☀️ UMPIRE

**Understand:** You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Given `n` versions `[1, 2, ..., n]` and an API `bool isBadVersion(version)` which returns whether `version` is bad, find the first bad version.

**Match:** This is a classic Binary Search problem. Since all versions after the first bad version are also bad, we can use binary search to efficiently locate the first bad version without checking every version linearly.

**Plan:**
1. Initialize two pointers: `left = 1` and `right = n`
2. Use binary search to narrow down the search range
3. When we find a bad version, it could be the first bad version or there might be earlier bad versions
4. When we find a good version, the first bad version must be to the right
5. Continue until we find the exact first bad version

**Implement:** See the code section below.

**Review:**
- Ensure we handle the API call efficiently (minimize calls)
- Consider edge cases like when the first version is bad
- Verify the search logic correctly identifies the first bad version

**Evaluate:**
- Time: O(log n) - we eliminate half of the search space each iteration
- Space: O(1) - only using constant extra space

## ☀️ Why This Is a Binary Search Problem

The key insight is that bad versions form a contiguous suffix of the array:
- All versions from the first bad version onward are bad
- All versions before the first bad version are good
- This creates a sorted property: `[Good, Good, ..., Good, Bad, Bad, ..., Bad]`

This allows us to:
- Use binary search to find the boundary between good and bad versions
- Eliminate half the search space with each API call
- Achieve O(log n) time complexity instead of O(n) linear search

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `n = 5, first bad = 4` | Normal case with bad versions at the end | `4` |
| `n = 1, first bad = 1` | Single version that is bad | `1` |
| `n = 5, first bad = 1` | First version is bad (all versions bad) | `1` |
| `n = 5, first bad = 5` | Last version is bad (only last version bad) | `5` |
| `n = 2, first bad = 1` | Two versions, first is bad | `1` |
| `n = 2, first bad = 2` | Two versions, second is bad | `2` |

These test:
- Boundary conditions (first/last version being bad)
- Single-element input
- Different positions of the first bad version
- Minimal input sizes

## ☀️ Code

### Solution 1: Binary Search (Lower Bound Template)
**Time: O(log n) → We eliminate half of the search space in each iteration**  
**Space: O(1) → Only using constant extra space for pointers**

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # First bad version is at mid or before mid
                right = mid
            else:
                # First bad version is after mid
                left = mid + 1
        
        # When left == right, we found the first bad version
        return left
```

### Solution 2: Binary Search with Record and Continue (Alternative Approach)
**Time: O(log n) → Same time complexity but may require more iterations**  
**Space: O(1) → Only using constant extra space for pointers**

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Find the first bad version using binary search with an 'ans' variable.
        - Keep a candidate 'ans' whenever we see a bad version.
        - Then continue searching on the left side to ensure it's the first bad.
        
        Time Complexity:  O(log n)
        Space Complexity: O(1)
        """
        left, right = 1, n
        ans = n  # Problem guarantees there is at least one bad version.
        
        while left <= right:
            # Middle index; avoids overflow in languages with fixed int width
            mid = left + (right - left) // 2
            # Call the API exactly once per loop and store the result
            bad = isBadVersion(mid)
            
            if bad:
                # mid is a bad version; it could be the first bad
                ans = mid
                # Exclude mid and everything to its right; continue searching left
                right = mid - 1
            else:
                # mid is good; the first bad must be to the right
                left = mid + 1
                
        return ans
```

## ☀️ Notes

**Solution 1 (Lower Bound Template):**
- Uses `while left < right` to converge pointers to the answer
- When finding a bad version, keeps it as a candidate by setting `right = mid`
- When finding a good version, eliminates it by setting `left = mid + 1`
- The final `left` naturally points to the first bad version

**Solution 2 (Record and Continue):**
- Uses `while left <= right` with an `ans` variable to track the best candidate
- Records every bad version found and continues searching for earlier ones
- More intuitive approach but may require additional iterations

## ☀️ Coding Walkthrough Script

**For Solution 1:**
"I'll use the lower bound binary search template to find the first bad version. I initialize left to 1 and right to n, representing the full range of versions.
I use a while loop with the condition left less than right, which ensures the pointers converge to a single position.
In each iteration, I calculate the middle index using left plus right minus left divided by 2 to prevent overflow.
I call the isBadVersion API once per iteration. If the middle version is bad, the first bad version could be at this position or earlier, so I set right to mid to keep this position as a candidate.
If the middle version is good, the first bad version must be to the right, so I set left to mid plus 1 to eliminate the left half including mid.
When the loop ends, left and right converge to the same position, which is guaranteed to be the first bad version."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Loop Condition | Notes |
|--------|----------------|------------------|----------------|-------|
| Linear Search | O(n) | O(1) | N/A | Brute force; calls API n times in worst case |
| Lower Bound Template | O(log n) | O(1) | `left < right` | **Recommended**; pointers converge naturally |
| Record and Continue | O(log n) | O(1) | `left <= right` | Intuitive but may need more iterations |

## ☀️ Binary Search Insights

- **Problem Pattern:** Finding the first position where a condition becomes true
- **Key Observation:** Bad versions form a contiguous suffix, creating a sorted property
- **Template Choice:** Lower bound template (`while left < right`) is ideal for "first occurrence" problems
- **API Efficiency:** Both solutions minimize API calls to O(log n)
- **Convergence Property:** In the lower bound template, the search space shrinks until left equals right, pointing to the answer

**Note:** Solution 1 is the most recommended approach using the `while left < right` template, which is optimal for finding "the first position that satisfies a condition". Solution 2 demonstrates a "record and continue" strategy but typically requires more iterations. Use Solution 1 in interviews for better efficiency.
