# 79. Word Search

☀️ **Problem**

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

☀️ **Example**

```
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]],
       word = "ABCCED"
Output: true
```

☀️ **Constraints**

- `1 <= board.length <= 6`
- `1 <= board[i].length <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consist only of lowercase English letters.

☀️ **UMPIRE Summary**

- **Understand**: Search for a word by moving up/down/left/right on a board, without reusing the same cell.
- **Match**: DFS + Backtracking pattern in a matrix.
- **Plan**: For every cell, start DFS if it matches `word[0]`. At each step, move in 4 directions and compare `board[r][c]` to `word[i]`. Use `#` to mark visited and backtrack after.
- **Implement**: See full code below.
- **Review**: Ensure correct base case (`i == len(word)`), bounds check, marking and unmarking of visited.
- **Evaluate**: Time O(m \* n \* 4^L), Space O(L)

☀️ **Approach**

We perform DFS from every cell that matches the first letter of `word`. At each step, we try moving up, down, left, or right. We mark the visited cell to avoid reusing it during the current path, and backtrack afterward.

☀️ **Code**

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != word[i]):
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
```

☀️ **Complexity**

- Time: `O(m * n * 4^L)` where `L` is the length of the word
- Space: `O(L)` recursion depth (call stack)

☀️ **Pattern**

- DFS
- Backtracking
- Matrix traversal

☀️ **Key Insight**

- Use in-place marking (`'#'`) to avoid extra visited matrix
- Only start DFS from cells that match `word[0]`
- Restore board state after each DFS attempt (backtracking)
