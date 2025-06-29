## ☀️ Leetcode 199 - Binary Tree Right Side View

### ☀️ Problem
Given the `root` of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see ordered from top to bottom.

### ☀️ UMPIRE Analysis

#### U — Understand (with Q&A)
- We want to collect the **rightmost node value** at each level of a binary tree.
- We return a list of these values from top to bottom.

**Q: What if the tree is empty?**  
A: Return an empty list `[]`

**Q: Is the length measured in edges or nodes?**  
A: We're not measuring length — we collect node **values**.

**Q: Do we need to return the path or just the values?**  
A: Just the node values, one per level.

#### M — Match
- Binary Tree traversal
- Right-side visibility per level
- DFS with right-first priority

#### P — Plan
1. Use DFS to traverse the tree.
2. Pass current `depth` as a parameter to track which level we're on.
3. If the current `depth == len(res)`, this is the first node we've visited at this level → it's the rightmost.
4. Recurse right-first to ensure rightmost nodes are visited first.
5. Return the collected result `res`.

#### R — Review
- Correctly captures only the first node seen at each depth.
- Traverses all nodes with DFS.
- Right-first ensures correct visibility order.

#### E — Evaluate
- **Time Complexity:** O(n), where n = number of nodes. Each node is visited once.
- **Space Complexity:** O(h), where h = tree height (call stack).
  - O(log n) for balanced tree
  - O(n) for skewed tree

### ☀️ Solution (DFS with right-first traversal)

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            # Base case: if the node is null, return
            if not node:
                return

            # If this is the first time we reach this depth,
            # then this node is the rightmost node at this level
            if depth == len(res):
                res.append(node.val)

            # Visit right child first to ensure rightmost nodes come first
            dfs(node.right, depth + 1)
            # Then visit left child
            dfs(node.left, depth + 1)

        # Start DFS from root at depth 0
        dfs(root, 0)
        return res
```

### ☀️ Key Concepts
- Right-first DFS traversal
- Depth-based decision
- Level-based visibility logic
- `depth == len(res)` means "first time at this level"


### ☀️ Verbal Walkthrough Script
- We want to return the rightmost node at each level of the binary tree. To do this, I use a right-prioritized DFS traversal. 
- I pass the current depth during traversal. If the depth equals the length of the result array, it means this is the first node visited at this level — and since we go right first, it’s the rightmost one.
- So, we append its value, and continue recursively to right and then left children. The base case is simply returning when the node is null.
