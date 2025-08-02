
# Leetcode 1537 - Get the Maximum Score

## ☀️ UMPIRE

### Understand
We are given two **strictly increasing sorted arrays** `nums1` and `nums2`.  
We can start from either array and move only to the right.  
Whenever we encounter a **common element** in both arrays, we can choose to switch to the other array or stay on the same one.  
We need to find the **maximum score** we can get by walking this path.  
The result must be returned modulo \(10^9 + 7\).

### Match
- This is a **two pointer** problem combined with **path merging** at intersection points.  
- A brute force solution is possible but inefficient.

### Plan (Optimal O(m+n))
1. Use two pointers `i` and `j` to traverse `nums1` and `nums2`.
2. Maintain two cumulative sums:  
   - `sum1`: score if we only walk on nums1 so far.  
   - `sum2`: score if we only walk on nums2 so far.
3. If `nums1[i] < nums2[j]`, add `nums1[i]` to `sum1` and move `i`.
4. If `nums1[i] > nums2[j]`, add `nums2[j]` to `sum2` and move `j`.
5. If they are equal (intersection), choose the better path so far:  
   `best = max(sum1, sum2) + nums1[i]`  
   then set `sum1 = sum2 = best` and move both pointers.
6. After one array is fully traversed, add remaining elements of the other array.
7. Return `max(sum1, sum2) % mod`.

### Implement (Optimal Solution)
```python
from typing import List

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9 + 7  # result modulo
        i = j = 0        # two pointers
        sum1 = sum2 = 0  # cumulative sums

        # Traverse both arrays until one ends
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                # Intersection point
                best = max(sum1, sum2) + nums1[i]
                sum1 = sum2 = best
                i += 1
                j += 1

        # Add remaining values
        while i < len(nums1):
            sum1 += nums1[i]
            i += 1
        while j < len(nums2):
            sum2 += nums2[j]
            j += 1

        # Take max and modulo
        return max(sum1, sum2) % mod
```

### Review
- Why two sums? → To track both possible paths and choose the optimal one at intersections.
- Why intersection sync? → Because at a common value, we can switch to the best scoring path.
- Why two while loops after the main one? → After one array is done, no new intersection can occur, so the remaining path is linear.

### Evaluate
- **Time Complexity**: O(m+n) (one pass through both arrays)
- **Space Complexity**: O(1) (only pointers and sums)

---

## ☀️ Brute Force (Exponential)
### Idea
Simulate all paths using DFS:
- At each intersection, branch into two choices (stay or switch).
- Take the maximum total score.

### Code (Teaching Only)
```python
def dfs(nums1, nums2, i, j, from1):
    if from1 and i >= len(nums1):
        return 0
    if not from1 and j >= len(nums2):
        return 0
    
    if from1:
        val = nums1[i]
        stay = val + dfs(nums1, nums2, i+1, j, True)
        switch = 0
        if nums1[i] in nums2[j:]:
            switch_index = nums2.index(nums1[i], j)
            switch = val + dfs(nums1, nums2, i+1, switch_index+1, False)
        return max(stay, switch)
    else:
        val = nums2[j]
        stay = val + dfs(nums1, nums2, i, j+1, False)
        switch = 0
        if nums2[j] in nums1[i:]:
            switch_index = nums1.index(nums2[j], i)
            switch = val + dfs(nums1, nums2, switch_index+1, j+1, True)
        return max(stay, switch)

def maxSumBruteForce(nums1, nums2):
    return max(dfs(nums1, nums2, 0, 0, True), dfs(nums1, nums2, 0, 0, False))
```

### Complexity
- **Time Complexity**: Exponential (worst case many intersections)
- **Space Complexity**: O(k) for recursion depth (k = intersections count)

---

## ☀️ Interview Walkthrough Script
The problem gives two sorted arrays and allows switching at intersection points.  
I track two cumulative sums: one for staying in nums1, one for staying in nums2.  
At each intersection, I sync both sums to the better path so far plus the intersection value.  
After one array finishes, I add the remaining values of the other because no more intersections are possible.  
Finally, I return the max of both sums modulo 1e9+7.  

The reason for two sums is to simulate two potential starting paths.  
The intersection sync ensures we always choose the optimal path when switching is allowed.  
This gives O(m+n) time, O(1) space, which is efficient for input sizes up to 10^5.  
There is a brute-force way to explore all paths, but it’s exponential and not practical.

---

## ☀️ Key Notes
- `% mod` is taking the remainder → keeps numbers in range, doesn’t affect complexity.
- Optimal solution is a common template: **Two Pointers + Intersection Sync**.
