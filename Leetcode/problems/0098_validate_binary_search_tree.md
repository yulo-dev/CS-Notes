# Leetcode 0098 - Validate Binary Search Tree

## ☀️ UMPIRE
- **Understand**:
  - Return True if the input binary tree is a valid Binary Search Tree (BST)
  - BST definition: for every node, all nodes in the left subtree < node < all nodes in the right subtree
- **Match**: Tree structure → use DFS to validate constraints
- **Plan**: Pass (lower, upper) bounds during DFS and validate node.val within range
- **Implement**: See below
- **Review**: Make sure bounds update correctly, and base case handles null
- **Evaluate**: Time O(n) to visit each node once, Space O(h) where h is the height of the tree (call stack)

## ☀️ Metadata
- **Appears In**: Grind75, Blind75
- **Pattern**: Valid Range Check in Recursion
- **Data Structure**: Binary Tree
- **Algorithm**: DFS
- **Tags**: Tree, DFS, Recursion, Binary Search Tree


## ☀️ Solution Code

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True

            if not (lower < node.val < upper):
                return False

            if not dfs(node.left, lower, node.val):
                return False

            if not dfs(node.right, node.val, upper):
                return False

            return True

        return dfs(root, float('-inf'), float('inf'))
```


## ☀️ Trace (Example Tree)

```
        10
       /  \
      5    15
          /  \
        11    20

→ dfs(10, -inf, inf)
    → dfs(5, -inf, 10)
        → dfs(None) ✅
        → dfs(None) ✅
    → dfs(15, 10, inf)
        → dfs(11, 10, 15)
            → dfs(None) ✅
            → dfs(None) ✅
        → dfs(20, 15, inf)
            → dfs(None) ✅
            → dfs(None) ✅
```


## ☀️ Line-by-line Typing Script 
- I define the `isValidBST` function which will return whether a given binary tree is a valid BST.
- Inside it, I define a helper function `dfs(node, lower, upper)` to validate each node.
- If the current node is null, we return True — an empty subtree is valid.
- If the node's value falls outside the allowed range (not in (lower, upper)), return False.
- Otherwise, recursively check the left subtree — it must be less than the current node.
- Then recursively check the right subtree — it must be greater than the current node.
- If both subtrees are valid, return True.
- Finally, we call `dfs` from the root with the initial bounds (-inf, inf).


## ☀️ Debugging Notes

| Mistake | Explanation | Fix |
|--------|-------------|-----|
| Called `dfs(root.val, ...)` | Passed an int instead of a TreeNode | Should pass `root` (the node) |
| Only compared to left/right child | This misses deeper subtree violations | Use global range with (lower, upper) |
| Forgot base case | Leads to crash or infinite recursion | Add `if not node: return True` |

## ☀️ Concept Recap
- Each node must fall strictly within the range inherited from all ancestors.
- When traversing left, update upper bound to `node.val`
- When traversing right, update lower bound to `node.val`
- This ensures the entire subtree structure respects BST rules
