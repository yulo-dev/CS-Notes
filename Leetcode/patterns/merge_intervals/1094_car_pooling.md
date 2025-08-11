# Leetcode 1094 - Car Pooling

## ☀️ UMPIRE

- **Understand**:  
  We have a list of trips, where each trip is represented as `[numPassengers, from, to]`.  
  The car has a fixed passenger capacity.  
  Determine if it is possible to complete all trips without exceeding capacity at any point.

- **Match**:  
  This is a **Prefix Sum / Difference Array** problem because the location range is small (0 ≤ location ≤ 1000).  
  We can simulate passenger changes at each location without explicitly merging intervals.

- **Plan** (Difference Array):  
  1. Create a fixed-size array `diff` of length 1001 (indices 0–1000).  
  2. For each trip `(ppl, start, end)`:
     - `diff[start] += ppl` → pick up passengers
     - `diff[end] -= ppl` → drop off passengers
  3. Traverse `diff` to compute current passengers (`curr += diff[i]`).  
     - If `curr > capacity`, return `False`.
  4. If the loop finishes, return `True`.

- **Implement**:  
  See Solution 1 (Beginner) and Solution 2 (Optimized).

- **Review**:  
  Test with edge cases: overlapping trips, exact capacity, capacity exceeded at start, single trip larger than capacity.

- **Evaluate**:  
  - Time: O(n + L) where L ≤ 1000 (treated as O(1) here)
  - Space: O(L) for the difference array (also O(1) here due to fixed limit).

---

## ☀️ Solution 1: Difference Array 

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Difference array for locations 0..1000
        diff = [0] * 1001

        # Apply changes for each trip
        for ppl, start, end in trips:
            diff[start] += ppl
            diff[end] -= ppl

        # Compute prefix sum and check capacity
        curr = 0
        for i in range(1001):
            curr += diff[i]
            if curr > capacity:
                return False
        
        return True
```

**Complexity**  
- Time: O(n + 1000) → O(n)  
- Space: O(1001) → O(1) fixed

---

## ☀️ Solution 2: Heap + Sorting (Handles Large Ranges)

```python
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Sort trips by start location
        trips.sort(key=lambda x: x[1])
        curr = 0
        heap = []  # min-heap for (end, ppl)

        for ppl, start, end in trips:
            # Remove trips that have ended
            while heap and heap[0][0] <= start:
                curr -= heapq.heappop(heap)[1]

            # Add current trip
            heapq.heappush(heap, (end, ppl))
            curr += ppl

            # Check capacity
            if curr > capacity:
                return False

        return True
```

**Complexity**  
- Time: O(n log n)  
- Space: O(n) for heap

---

## ☀️ Tags  
- Array  
- Prefix Sum / Difference Array  
- Heap (Priority Queue)  
- Simulation  
- Sorting

## ☀️ Data Structure  
- **Primary**: Fixed-size list (`diff`) for difference array  
- **Alternative**: Min-heap for ongoing trips

## ☀️ Algorithm Summary  
1. If location range is small → use **difference array** for O(n) simulation.  
2. If location range is large → use **heap** to manage active trips.


---

## ☀️ Coding Walkthrough Script 

- I’ll treat each trip `[p, s, e)` as **+p at s** (pickup) and **−p at e** (drop), since intervals are half-open.
- Because the location range is small (0..1000), I’ll build a **difference array** `diff[0..1000]`:
  - For each trip: `diff[s] += p` and `diff[e] -= p`.
- Then I’ll do one **prefix-sum** scan over `diff` to compute the **current passengers** at each location:
  - Initialize `curr = 0`; for `i` from 0 to 1000: `curr += diff[i]`.
  - If at any point `curr > capacity`, return **False** (overload occurs there).
- If the loop completes without exceeding capacity, return **True`.
- Complexity: updating the diff is `O(n)`, scanning is `O(1001)` which we treat as `O(1)` → overall **O(n)** time, **O(1)** extra space.
