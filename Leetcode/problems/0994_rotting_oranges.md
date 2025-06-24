
# ☀️ Leetcode 994 - Rotting Oranges

## ☀️ U — Understand

🦢 You are given a 2D grid:
- `0` = empty cell  
- `1` = fresh orange  
- `2` = rotten orange  

Every minute, any fresh orange directly adjacent (up/down/left/right) to a rotten one will also become rotten.
Return the **minimum number of minutes** until all oranges are rotten, or `-1` if not all can rot.

### 🔍 Clarifying Questions

- Q: Are diagonals considered adjacent?  
  A: No. Only up/down/left/right.

- Q: Can there be only fresh oranges?  
  A: Yes. Return `-1` in that case.

- Q: Can the grid be all empty cells or no fresh oranges?  
  A: Yes. Return `0` if no fresh oranges exist at start.

## ☀️ M — Match

- Multi-source BFS
- Grid traversal

## ☀️ P — Plan

1. Loop through the grid:
   - Count all fresh oranges
   - Add all initial rotten oranges to a queue

2. While `queue` is not empty and `fresh > 0`:
   - For all cells in this layer (1 minute):
     - Pop from queue
     - Explore 4 directions
     - If neighbor is fresh:
       - Turn it rotten
       - Add to queue
       - Decrement fresh count

3. After BFS:
   - If `fresh == 0` → return `time`
   - Else → return `-1`

## ☀️ I — Implement

```python
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        # Step 1: Initialize queue and fresh count
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2: BFS
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1
```

## ☀️ R — Review

### Time Complexity: `O(m * n)`
- Each cell is visited once.
- Grid size = `m * n`

### Space Complexity: `O(m * n)`
- Worst case: all oranges in queue

---

## ☀️ E — Evaluate

### Edge Cases
| Grid | Output | Notes |
|------|--------|-------|
| Only fresh oranges | `-1` | No way to rot |
| Only rotten oranges | `0` | Nothing to do |
| Mixed and all can rot | Time | Based on infection steps |

## ☀️ Line by Line Script 

- Define a class Solution and implement orangesRotting and we get the number of rows and columns of the grid.
- We initialize `fresh` as the count of fresh oranges and a `queue` to store rotten ones.
- We iterate through the grid. If the cell is rotten, we append its coordinates to the queue. If the cell is fresh, we increase the `fresh` count.
- If there are no fresh oranges, we return 0 immediately.
- We define our four directions: up, down, left, right.
- While the queue is not empty and there are still fresh oranges:
- We loop through all cells currently in the queue (same minute).
- For each rotten orange, we check its 4 neighbors. If a neighbor is fresh, we rot it, add to the queue, and decrease `fresh`.
- After each level, we increase time by 1.
- If all fresh oranges have rotted, return `time`; else, return -1.

## ☀️ Path Walkthrough

### Input:
```
[ [2,1,1],
  [1,1,0],
  [0,1,1] ]
```

Minute-by-minute infection:
- Minute 1 → (0,1), (1,0)
- Minute 2 → (0,2), (1,1), (2,1)
- Minute 3 → (2,2)
→ Output: `4`
