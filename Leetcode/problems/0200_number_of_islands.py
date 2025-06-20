class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Handle edge case: empty grid
        if not grid:
            return 0

        # Get number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])

        # Use a set to track visited land cells
        visited = set()
        island_count = 0  # Counter for total number of islands

        # DFS function to explore all connected '1's from a starting cell
        def dfs(r, c):
            # If out of bounds, already visited, or water → stop
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == '0' or 
                (r, c) in visited):
                return

            # Mark this cell as visited
            visited.add((r, c))

            # Recursively visit all 4 directions (up, down, left, right)
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        # Iterate through the entire grid
        for r in range(rows):
            for c in range(cols):
                # If this is unvisited land, it's a new island
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)  # explore the island
                    island_count += 1  # increment island count

        # Return total number of islands found
        return island_count
