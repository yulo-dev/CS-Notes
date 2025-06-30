
# Leetcode 0236 - Lowest Common Ancestor of a Binary Tree

## ☀️ UMPIRE

- **Understand**  
  Given the `root` of a binary tree and two nodes `p` and `q`, return their **lowest common ancestor** (LCA).  
  LCA is defined as the **lowest node** in the tree that has **both `p` and `q` as descendants** (a node can be a descendant of itself).

- **Match**  
  - Tree structure → use DFS  
  - Need to traverse entire tree → use postorder DFS (bottom-up)  
  - Goal: identify the first node that connects `p` and `q`

- **Plan**  
  Use recursive DFS:
  1. Traverse left and right subtree
  2. If current node is `p` or `q`, return itself
  3. If both left and right subtree returned non-null, current node is the LCA

- **Implement**  
  See code section below.

- **Review**  
  - Base case: `if not root or root == p or root == q`
  - Recursively check left and right
  - Key logic: if both sides return non-null → return root

- **Evaluate**  
  - Time: O(n) — must traverse all nodes  
  - Space: O(h) — height of tree due to recursion stack

## ☀️ Metadata

- **Appears In**: AlgoMonster DFS Track, Leetcode Top 150  
- **Pattern**: DFS, Postorder Traversal  
- **Data Structure**: Binary Tree  
- **Algorithm**: Depth-First Search (DFS), Backtracking  
- **Tags**: Tree, DFS, Recursion, Binary Tree  
- **14 Pattern**: #10 Tree DFS


## ☀️ Solution Code

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if root == p or root == q:
            return root

        if left and right:
            return root

        return left if left else right
```

## ☀️ Complexity

- **Time Complexity**: O(n)  
  Must visit every node once

- **Space Complexity**: O(h)  
  Due to recursion stack, where h is tree height  
  Worst case: skewed tree → O(n), balanced → O(log n)

## ☀️ Example Trace

Input Tree:

```
        5
       / \
      3   8
     / \
    2   4
```

Given: `p = 3`, `q = 4`

Recursive Trace:

- `dfs(5)`  
  - → `dfs(3)`  
    - → `dfs(2)` → return None  
    - → `dfs(4)` → return 4 ✅  
    - root == p → return 3 ✅  
  - → `dfs(8)` → return None  
  → left = 3, right = None → return 3 ✅

Final Output: `3`

## ☀️ Return Rule Summary

| Condition | Return |
|-----------|--------|
| `root == p or q` | Return root itself (signal that one target was found) |
| `left` and `right` are both non-null | Current root is LCA |
| Only one side is non-null | Return that side’s result up the call stack |

## ☀️ Insight

- Avoid early `return root` before traversing children — this version ensures both sides are searched
- This postorder DFS guarantees you find the *lowest* common ancestor
