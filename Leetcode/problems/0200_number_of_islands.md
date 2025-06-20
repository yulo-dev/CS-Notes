## ☀️ Leetcode 200 - Number of Islands

### ☀️ Problem Summary
Given a 2D grid of '1' (land) and '0'(water), count the number of islands.  
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

Return the total number of islands.

## ☀️ UMPIRE

- **Understand**  
  We are given a 2D grid map of `'1'`s (land) and `'0'`s (water).  
  An island is a group of `'1'`s connected **horizontally or vertically**.  
  We must return the total number of islands.

- **Match**  
  This is a **grid traversal** problem.  
  Suitable for **DFS**, **BFS**, or **Union-Find** (advanced).  
  For now, we use **DFS** for simplicity.

- **Plan**  
  1. Traverse each cell in the grid.
  2. When a cell is `'1'` and not visited, it’s a new island → start DFS.
  3. DFS explores all adjacent land cells and marks them as visited.
  4. Count how many times we initiate DFS.

- **Review**  
  Make sure visited tracking works, DFS stops at water/out-of-bounds, and all islands are counted exactly once.

- **Evaluate**  
  Time = `O(m × n)`  
  Space = `O(m × n)` in worst case (visited + call stack)


### ☀️ Approach: DFS
- Treat the grid as a graph
- Each cell with `'1'` is a potential start of an island
- Use DFS to visit all connected land (`'1'`) from that cell
- Use a `visited` set to track visited coordinates
- Every time we start DFS from a new `'1'`, we’ve found a new island


### ☀️ Code 
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_count = 0

        def dfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == '0' or
                (r, c) in visited):
                return

            visited.add((r, c))

            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    island_count += 1

        return island_count

## ☀️ Line-by-Line Typing Script

- Define a class called Solution, as required by Leetcode. The main function `numIslands` receives a 2D list of strings. 
- If the grid is empty, return 0 immediately and store the number of rows and columns. 
- Create a `visited` set to record coordinates we’ve already processed.
- Initialize a counter `island_count` to track number of islands.
- Define a recursive DFS function to explore from cell `(r, c)`.
- If out of bounds, or water, or already visited — return immediately.
- Mark this coordinate as visited.
- From here, recursively explore 4 directions: up, down, left, right.
- Now loop through each cell in the grid.
- If it’s land and not visited, call DFS from that point and increment island count.
- Return the final count after all cells are checked.

## ☀️ Time & Space Complexity

- **Time Complexity**: `O(m × n)`  
  Each cell is visited at most once.

- **Space Complexity**: `O(m × n)`  
  - In worst case (entire grid is land), visited set + recursion call stack.

## ☀️ Tags

- Graph  
- DFS  
- Matrix  
- Flood Fill
