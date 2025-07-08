# Leetcode 0973 - K Closest Points to Origin

## ☀️ UMPIRE  
- **Understand**: Given a list of 2D points, return the k closest points to the origin (0, 0).  
- **Match**: This is a Top-K selection problem → suitable for a heap-based approach.  
- **Plan**: Use a max-heap of size k to store the k closest points so far. For each new point, compute the squared distance to origin and push into the heap. If heap size exceeds k, pop the farthest point.  
- **Implement**: See below  
- **Review**: Verify that the heap always contains the k closest seen so far, and ensure output format is List[List[int]].  
- **Evaluate**:  
  - **Time**: O(n log k), where n is the number of points, because each `heappush`/`heappop` is O(log k).  
  - **Space**: O(k) for the heap size. Output list is also O(k).  

## ☀️ Metadata  
- **Appears In**: Grind75, NeetCode 150  
- **Pattern**: Heap / Top K Elements  
- **Data Structure**: Max-Heap (simulated with `heapq` and negative distance)  
- **Algorithm**: Heap-based filtering  
- **Tags**: Heap, Priority Queue, Top K, Sorting


## ☀️ Solution Code  

```python
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            dist = -(x * x + y * y)  # Negative distance to simulate max-heap
            heapq.heappush(max_heap, (dist, x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [[x, y] for (_, x, y) in max_heap]
```

## ☀️ Trace  

Input: `points = [[1,3],[-2,2],[2,-2]], k = 2`  

1. Push (−10, 1, 3) → heap = [(-10, 1, 3)]  
2. Push (−8, -2, 2) → heap = [(-10, 1, 3), (-8, -2, 2)]  
3. Push (−8, 2, -2) → heap = [(-10, 1, 3), (-8, -2, 2), (-8, 2, -2)]  
   → len = 3 > k → pop (-10, 1, 3)  
   → heap = [(-8, -2, 2), (-8, 2, -2)]  
Output: `[[−2,2],[2,−2]]` (order may vary)

## ☀️ Line-by-line Typing Script  

- I’m importing `heapq` and `List` from typing to support heap operations and type hints.  
- I define the `kClosest` function, which returns the k points closest to origin.  
- I initialize an empty list called `max_heap` to simulate a max-heap using negative distances.  
- I iterate through each point (x, y) in the input list.  
- For each point, I calculate its squared Euclidean distance from origin and negate it.  
- I push a tuple of (negative distance, x, y) into the heap.  
- If the heap now contains more than k elements, I pop the top (farthest) point.  
- Finally, I return the remaining k closest points as a list of [x, y], using list comprehension to ignore the distance part.
