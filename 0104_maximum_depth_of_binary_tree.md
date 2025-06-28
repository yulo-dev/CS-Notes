# Leetcode 0104 - Maximum Depth of Binary Tree

## ☀️ UMPIRE

- **Understand**: Given the root of a binary tree, return the maximum depth (longest path from root to a leaf).
- **Match**: This is a classic post-order DFS problem — we need to go all the way down before making decisions.
- **Plan**: Recursively compute the depth of the left and right subtrees, then return max(left, right) + 1.
- **Implement**: Base case is null node → return 0. Recursive step returns 1 + max depth from left/right.
- **Review**: Make sure it handles empty trees and unbalanced trees correctly.
- **Evaluate**:
  - **Time**: O(n) — each node is visited once
  - **Space**: O(h) — call stack depth = tree height (O(log n) if balanced, O(n) worst case)

## ☀️ Metadata

- **Appears In**: Grind75
- **Pattern**: Binary Tree Recursion
- **Data Structure**: Binary Tree
- **Algorithm**: DFS
- **Tags**: Tree, DFS, Recursion


## ☀️ Solution Code

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: empty node has depth 0
        if not root:
            return 0

        # Recursively find depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Return the greater of the two, plus 1 for the current node
        return max(left_depth, right_depth) + 1
```

## ☀️ Trace

```
Input: [3, 9, 20, None, None, 15, 7]

Tree:
        3
       / \
      9  20
         / \
        15  7

Recursive calls:
→ maxDepth(3)
  → maxDepth(9) → return 1
  → maxDepth(20)
      → maxDepth(15) → return 1
      → maxDepth(7)  → return 1
      → return max(1,1)+1 = 2
→ return max(1,2)+1 = 3
```

## ☀️ Line-by-line Script

- I’m defining the `maxDepth` function that receives the root of a binary tree.
- If the root is `None`, the depth is 0 and I return immediately.
- I recursively compute the depth of the left and right subtrees.
- Then I take the maximum of the two and add 1 to account for the current node.
- Finally, I return this value as the maximum depth of the tree.
