# Leetcode 0105 - Construct Binary Tree from Preorder and Inorder Traversal

## ☀️ UMPIRE
- **Understand**:
  - Given preorder (root-left-right) and inorder (left-root-right) traversal lists
  - All values are unique
  - Return the root node of the constructed binary tree
- **Match**: Recursion + Tree construction problem
- **Plan**:
  - Use a hashmap to map inorder values to indices
  - Use recursion with index ranges to build subtrees
- **Implement**: See code below
- **Review**: Carefully calculate left subtree size and slicing bounds
- **Evaluate**:
  - Time: O(n) — each node visited once
  - Space: O(n) — recursion stack + hashmap


## ☀️ Metadata
- **Appears In**: Grind75
- **Pattern**: Construct Binary Tree from Traversal (#12)
- **Data Structure**: Binary Tree
- **Algorithm**: Recursion, Divide and Conquer
- **Tags**: Tree, Binary Tree, DFS, Recursion, Hash Map, Preorder, Inorder


## ☀️ Solution Code
```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_order_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            in_root_idx = in_order_map[root_val]
            left_size = in_root_idx - in_left

            root.left = helper(pre_left + 1, pre_left + left_size, in_left, in_root_idx - 1)
            root.right = helper(pre_left + left_size + 1, pre_right, in_root_idx + 1, in_right)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
```


## ☀️ Trace Example (Preorder = [3,9,20,15,7], Inorder = [9,3,15,20,7])
```
Call: helper(0, 4, 0, 4)
  root = 3 (preorder[0])
  root index in inorder = 1 → left_size = 1
  → build left: helper(1,1,0,0)
    root = 9
    → build left: helper(2,1,0,-1) → None
    → build right: helper(2,1,1,0) → None
  → build right: helper(2,4,2,4)
    root = 20
    root index = 3 → left_size = 1
    → build left: helper(3,3,2,2)
      root = 15
      → left: helper(4,3,2,1) → None
      → right: helper(4,3,3,2) → None
    → build right: helper(4,4,4,4)
      root = 7
      → left/right = None
```


## ☀️ Line-by-line Typing Script
- Start by creating a map from value to index using inorder
- Define a recursive helper function with index ranges
- If preorder range is invalid, return None (base case)
- Root is always the first element in current preorder range
- Find its index in inorder and calculate left subtree size
- Recursively build left subtree using calculated ranges
- Recursively build right subtree as well
- Return the root


## ☀️ Debugging Notes
| Mistake | Fix |
|--------|------|
| Used `preorder[0]` in recursion | ❌ Should use `preorder[pre_left]` |
| Used list slicing | ❌ Leads to O(n²) time — use indices |
| Forgot base case | ❌ Leads to infinite recursion — add `pre_left > pre_right` |


## ☀️ Index Mapping Reference
| Subtree        | preorder range                         | inorder range                      |
|----------------|-----------------------------------------|------------------------------------|
| Root node      | `preorder[pre_left]`                    | `inorder[in_root_idx]`             |
| Left subtree   | `pre_left+1 ~ pre_left+left_size`       | `in_left ~ in_root_idx - 1`        |
| Right subtree  | `pre_left+left_size+1 ~ pre_right`      | `in_root_idx + 1 ~ in_right`       |
