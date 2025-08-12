# Leetcode 1094 - Car Pooling

## ☀️ UMPIRE

- **Understand**:  
  We have a list of trips, where each trip is represented as `[numPassengers, from, to]`.  
  The car has a fixed passenger capacity.  
  Determine if it is possible to complete all trips without exceeding capacity at any point.

- **Match**:  
  This can be solved by simulating passenger changes along the route.  
  Approaches vary in efficiency depending on how we model the problem:
  1. Brute force simulate each location (slowest).
  2. Use a **Min-Heap** to track active trips (general & scalable).
  3. Use a **Difference Array** if location range is small (fastest for this problem).

- **Plan**:  
  1. **Brute Force**: simulate passenger count for every location per trip.  
  2. **Min-Heap**: sort by start location, pop ended trips, push new trips.  
  3. **Difference Array**: mark +p at start, -p at end, prefix-sum once.

- **Review**:  
  Test with edge cases: overlapping trips, exact capacity, capacity exceeded at start, single trip larger than capacity.

- **Evaluate**:  
  | Approach       | Time Complexity   | Space Complexity |
  |----------------|-------------------|------------------|
  | Brute Force    | O(n * L)          | O(L)             |
  | Min-Heap       | O(n log n)        | O(n)             |
  | Diff Array     | O(n + L)          | O(L)             |
  Here L ≤ 1000 in this problem.

---

## ☀️ Solution 1: Brute Force (Slowest)

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = [0] * 1001  # passenger count at each location

        for p, s, e in trips:
            if p > capacity:
                return False
            for x in range(s, e):
                car[x] += p
                if car[x] > capacity:
                    return False

        return True
```

**Complexity**  
- Time: O(n * 1000) → O(n) here since L=1000 fixed  
- Space: O(1000) → O(1) fixed  
- Pros: Very easy to implement  
- Cons: Inefficient for large ranges

---

## ☀️ Solution 2: Min-Heap by End (General & Intuitive)

```python
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])  # sort by start location
        curr = 0
        heap = []  # min-heap for (end, passengers)

        for p, s, e in trips:
            # Drop off passengers for trips ending at/before s
            while heap and heap[0][0] <= s:
                curr -= heapq.heappop(heap)[1]

            # Pick up current trip
            heapq.heappush(heap, (e, p))
            curr += p

            if curr > capacity:
                return False

        return True
```

**Complexity**  
- Time: O(n log n)  
- Space: O(n) for heap  
- Pros: Works well when location range is large  
- Cons: More complex than brute force for small ranges

---

## ☀️ Solution 3: Difference Array + Prefix Sum (Fastest Here)

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001  # difference array for locations 0..1000

        for p, s, e in trips:
            if p > capacity:
                return False
            diff[s] += p
            diff[e] -= p  # passengers get off at e

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
- Pros: Short, fast, optimal for bounded ranges  
- Cons: Only optimal if location range is small

---

## ☀️ Tags  
- Array  
- Simulation  
- Prefix Sum / Difference Array  
- Heap (Priority Queue)  
- Sorting

## ☀️ Data Structure  
- **Brute Force**: Array of size L for passenger counts  
- **Heap**: Min-heap to store active trips by end location  
- **Difference Array**: Fixed-size list for passenger changes

---

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
