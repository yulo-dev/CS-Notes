# Leetcode 0226 - Invert Binary Tree

## ☀️ UMPIRE

- **Understand**: Given the root of a binary tree, invert the tree by swapping the left and right children of every node.
- **Match**: Classic tree structure problem → fits post-order DFS recursion pattern.
- **Plan**: Use recursion to traverse down to leaf nodes, swap left and right at each node on the way back.
- **Implement**: Recurse on left and right subtrees, then swap pointers, and return root.
- **Review**: Ensure null nodes return properly, and no new nodes are created (in-place).
- **Evaluate**:
- **Time**: O(n) — each node is visited once
- **Space**: O(h) — recursion depth = tree height (O(log n) if balanced, O(n) worst case)

## ☀️ Metadata

- **Appears In**: Grind75
- **Pattern**: Binary Tree Transform
- **Data Structure**: Binary Tree
- **Algorithm**: Recursion, DFS
- **Tags**: Tree, Recursion, DFS


## ☀️ Solution Code

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: nothing to invert
        if not root:
            return None

        # Recursively invert left and right subtrees
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # Swap the pointers
        root.left = right
        root.right = left

        # Return current node with children swapped
        return root
```

## ☀️ Trace

```
Input: [4, 2, 7, 1, 3, 6, 9]

Level-order before inversion:
        4
       / \
      2   7
     / \ / \
    1  3 6  9

Recursive calls:
→ invertTree(4)
  → invertTree(2)
    → invertTree(1) → return 1
    → invertTree(3) → return 3
    → swap 1 and 3 → return 2
  → invertTree(7)
    → invertTree(6) → return 6
    → invertTree(9) → return 9
    → swap 6 and 9 → return 7
→ swap 2 and 7 → return 4

Level-order after inversion:
        4
       / \
      7   2
     / \ / \
    9  6 3  1
```

## ☀️ Line-by-line Script

- I’m defining the `invertTree` function that takes the root of a binary tree.
- If the root is `None`, I return immediately since there’s nothing to invert.
- I recursively call the function on the left and right child to process them first.
- After both recursive calls return, I swap the left and right children.
- Finally, I return the current root with its left and right subtrees inverted.
