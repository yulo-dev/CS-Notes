# Leetcode 0110 - Balanced Binary Tree

## ☀️ UMPIRE

- **Understand**:  
  Return `True` if the binary tree is height-balanced.  
  A height-balanced binary tree means for **every node**, the left and right subtree heights differ by **at most 1**.
- **Match**:  
  Requires post-order DFS — perfect fit for recursive bottom-up traversal.
- **Plan**:  
  Use DFS to compute subtree height. If any subtree is unbalanced, return -1 immediately (early termination).  
  Return the actual height if balanced.
- **Implement**:  
  Define `dfs(node)` helper that returns height if balanced, else -1.  
  Final result is `dfs(root) != -1`.
- **Review**:  
  Check null (empty tree), leaf node (height = 0), and balance at each level.  
  Use early exit to avoid redundant computation.
- **Evaluate**:  
  - **Time**: O(n) — each node visited once  
  - **Space**: O(h) recursion stack (h = tree height)

## ☀️ Metadata

- **Appears In**: Grind75  
- **Pattern**: Subtree recursion  
- **Data Structure**: Binary Tree  
- **Algorithm**: DFS, Post-order  
- **Tags**: Tree, DFS, Recursion

## ☀️ Solution Code

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # DFS returns height if balanced, -1 if not
        def dfs(node):
            if not node:
                return 0  # Empty node has height 0

            left = dfs(node.left)
            if left == -1:
                return -1  # Left subtree not balanced

            right = dfs(node.right)
            if right == -1:
                return -1  # Right subtree not balanced

            if abs(left - right) > 1:
                return -1  # Current node not balanced

            return 1 + max(left, right)  # Return height of current subtree

        return dfs(root) != -1
```

## ☀️ Trace

Example:
```
      1
     / \
    2   3
   /
  4
```

```
dfs(4) → left=0, right=0 → height=1 → ✅
dfs(2) → left=1, right=0 → height=2 → ✅
dfs(3) → left=0, right=0 → height=1 → ✅
dfs(1) → left=2, right=1 → height=3 → ✅
→ final result: True
```

Unbalanced example:
```
      1
     /
    2
   /
  3
```

```
dfs(3) → height=1
dfs(2) → left=1, right=0 → height=2
dfs(1) → left=2, right=0 → abs(2-0)=2 > 1 → return -1
→ final result: False
```

## ☀️ Line-by-line Script

- I define the `isBalanced` function which takes the root of a binary tree.
- Inside, I define a helper `dfs(node)` to recursively compute subtree height.
- If the node is None, I return 0 as the base case (empty subtree).
- I recursively call `dfs(node.left)` to get the left subtree height.
- If the left subtree is unbalanced (returns -1), I propagate -1 upward.
- I do the same for the right subtree.
- If the absolute difference between left and right height is more than 1, I return -1 — meaning this node is unbalanced.
- Otherwise, I return the height of the current subtree, which is `1 + max(left, right)`.
- Finally, in `isBalanced`, I return whether the result of `dfs(root)` is not -1, indicating the whole tree is balanced.
