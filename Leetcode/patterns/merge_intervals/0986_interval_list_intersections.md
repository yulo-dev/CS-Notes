# Leetcode 0986 - Interval List Intersections

## ☀️ UMPIRE

- **Understand**: Given two lists of **closed** intervals `firstList` and `secondList`, each list is pairwise disjoint and sorted by start. Return **all intersections** between the two lists. If two intervals touch at a single point (e.g., `[2,4]` and `[4,6]`), the intersection is `[4,4]`.
  
- **Match**: This is a classic **Intervals** problem. Since both lists are sorted and disjoint within themselves, we can use a **two‑pointer sweep**. For learning purposes, we also include a straightforward **brute force with early breaks** as a prior stage solution.

- **Plan**:
  1) (Brute Force, prior stage) For each interval in `A`, scan `B`:
     - If `B[j].end < A[i].start` → continue
     - If `B[j].start > A[i].end` → break the inner loop
     - Otherwise compute candidate intersection and keep it if valid.
  2) (Optimal) Use two pointers `i` and `j`:
     - Candidate intersection: `start = max(a_start, b_start)`, `end = min(a_end, b_end)`
     - If `start <= end`, append `[start, end]`
     - Advance the pointer whose interval ends first (`a_end < b_end → i++`, `a_end > b_end → j++`, else **both**).

- **Implement**: See the code sections below.

- **Review**:
  - Intervals are **closed**, so point-touching counts → keep `start <= end` (not `<`).
  - Make sure the while condition is `i < len(A) and j < len(B)`—once one list ends, no further intersections exist.

- **Evaluate**:
  - Brute Force: Time `O(m·n)`, Space `O(1)` auxiliary (excluding output).
  - Two Pointers: Time `O(m + n)`, Space `O(1)` auxiliary (excluding output).

---

## ☀️ Why This Is an Intervals Problem

Sorting (already given) and the disjoint property imply that any intersection for `A[i]` can only come from the **current** `B[j]`. 
Once one of them ends, that interval cannot intersect future intervals of the other list. This enables a clean **single pass** with two pointers and constant extra space.

---

## ☀️ Edge Case Notes

| Input (A, B)                              | Description                                  | Expected Output              |
|-------------------------------------------|----------------------------------------------|------------------------------|
| `[[1,3]]`, `[[4,6]]`                      | Disjoint with a gap                          | `[]`                         |
| `[[1,2]]`, `[[2,3]]`                      | Touch at a point (closed intervals)          | `[[2,2]]`                    |
| `[[1,5]], [[2,3]]`                        | B fully inside A                             | `[[2,3]]`                    |
| `[[2,3]], [[1,5]]`                        | A fully inside B                             | `[[2,3]]`                    |
| `[[1,5],[10,14],[16,18]]`, `[[2,6],[8,10],[11,20]]` | Multiple partial overlaps           | `[[2,5],[10,10],[11,14],[16,18]]` |

These test: no overlap, point-touch, containment, and multiple intersections.

---

## ☀️ Code — Solution 1 (Brute Force with Early Breaks)

```python
from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        Brute force with ordering-based pruning.
        Time:  O(m * n) in the worst case
        Space: O(1) extra (excluding the output list)
        """
        res: List[List[int]] = []

        for a_start, a_end in A:
            for b_start, b_end in B:
                # B ends before A starts → cannot intersect yet
                if b_end < a_start:
                    continue
                # B starts after A ends → later Bs won't intersect A either (lists are sorted)
                if b_start > a_end:
                    break

                # Candidate intersection (closed intervals)
                start = max(a_start, b_start)
                end   = min(a_end, b_end)
                if start <= end:
                    res.append([start, end])

        return res
```

**Complexity**: Time `O(m·n)`, Space `O(1)` extra (excluding output).

---

## ☀️ Code — Solution 2 (Two Pointers, Optimal)

```python
from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        Two-pointer scan (optimal):
        - Compare A[i] with B[j]
        - Emit intersection if max(starts) <= min(ends) (closed intervals)
        - Advance the side that ends first; if both end together, advance both.
        Time:  O(m + n)
        Space: O(1) extra (excluding the output list)
        """
        i = j = 0
        res: List[List[int]] = []

        while i < len(A) and j < len(B):
            a_start, a_end = A[i]
            b_start, b_end = B[j]

            # Candidate intersection boundaries
            start = max(a_start, b_start)  # later start
            end   = min(a_end, b_end)      # earlier end

            # Closed intervals: touching at a single point counts
            if start <= end:
                res.append([start, end])

            # Advance interval(s) that ended
            if a_end < b_end:
                i += 1
            elif a_end > b_end:
                j += 1
            else:
                i += 1
                j += 1

        return res
```

**Complexity**: Time `O(m + n)`, Space `O(1)` extra (excluding output).

---

## ☀️ Notes

- **Closed vs Half-Open**: This problem uses *closed* intervals → `start <= end`. For half-open `[l, r)`, the check becomes `start < end`.
- **Why advance the smaller end?** The interval that ends first cannot intersect any later interval of the other list—it's exhausted on the right.
- **Sorted + Disjoint is crucial**: If lists were not disjoint or not sorted, you would need preprocessing (merge/sort) before applying the two-pointer sweep.

---

## ☀️ Coding Walkthrough Script (Interview Voiceover)

- First, I note both lists are sorted and internally disjoint, which suggests a two-pointer sweep.
- I keep pointers `i` for A and `j` for B.
- At each step, I compute a candidate intersection with `start = max(a_start, b_start)` and `end = min(a_end, b_end)`.
- If `start <= end`, because these are closed intervals, I append `[start, end]` to the result.
- Next, I advance the pointer whose interval ends first; if both end at the same position, I advance both.
- The loop continues while both lists have intervals. As soon as one list is exhausted, no further intersections are possible.
- This yields `O(m + n)` time and `O(1)` extra space.

---

## ☀️ Brute Force vs Two Pointers — Quick Compare

| Method                 | Time              | Space (aux) | When to Use                                 |
|-----------------------|-------------------|-------------|---------------------------------------------|
| Brute Force + Pruning | O(m · n)          | O(1)        | Learning phase, very small inputs           |
| Two Pointers (Optimal)| O(m + n)          | O(1)        | Interviews & production; scaled inputs      |
