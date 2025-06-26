class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])  # Get the size of the board

        def dfs(r, c, i):
            # Base case: if we've matched the whole word
            if i == len(word):
                return True

            # Boundary check + character mismatch check
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != word[i]):
                return False

            # Mark this cell as visited by replacing the character
            temp = board[r][c]
            board[r][c] = "#"  # Mark visited so we don't reuse it

            # Explore all 4 directions: down, up, right, left
            found = (dfs(r + 1, c, i + 1) or 
                     dfs(r - 1, c, i + 1) or 
                     dfs(r, c + 1, i + 1) or 
                     dfs(r, c - 1, i + 1))

            # Restore the original value (backtrack)
            board[r][c] = temp

            return found  # Return True if any path matched the word

        # Try every cell as the starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):  # Start DFS from (r, c) with word[0]
                    return True  # If any path finds the full word, return True

        return False  # No path matched the word
