from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        # Step 1: Count fresh oranges and enqueue all rotten ones
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c)) # Rotten orange
                elif grid[r][c] == 1:
                    fresh += 1 # Fresh orange


        # If there are no fresh oranges, no time needed
        if fresh == 0:
            return 0

        time = 0
        directions = (1,0), (-1,0), (0, 1), (0, -1)

        # Step 2: BFS - simulate rotting process minute by minute
        while queue and fresh > 0: 
            for _ in range(len(queue)): # Process all rotten oranges of current minute
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # If neighbor is in bounds and is a fresh orange, rot it
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1 # One fewer fresh orange

            time += 1 # One minute has passed

        # If no fresh oranges remain, return time; otherwise return -1
        return time if fresh == 0 else -1
