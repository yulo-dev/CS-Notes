
# Leetcode 0235 - Lowest Common Ancestor of a Binary Search Tree

## ☀️ UMPIRE

- **Understand**  
  Given a Binary Search Tree and two nodes `p` and `q`, return their lowest common ancestor (LCA).  
  The LCA is the deepest node that has both `p` and `q` as descendants.  
  (A node can be a descendant of itself.)

- **Match**  
  - Tree input → likely DFS  
  - But it's a **BST**, so we can use the value ordering to guide traversal  
  - Use value comparison instead of full subtree search

- **Plan**  
  At each node:
  1. If both `p` and `q` are smaller than root → LCA is in left subtree
  2. If both are larger than root → LCA is in right subtree
  3. Otherwise → current node is where they split → LCA found

- **Implement**  
  See solution code below

- **Review**  
  - Does not require checking both sides (unlike general binary tree)  
  - Return immediately when split point found

- **Evaluate**  
  - Time: O(h), where h is the height of the BST  
  - Space: O(h) due to recursion stack (or O(1) if iterative)

## ☀️ Metadata

- **Appears In**: Grind75, Leetcode Top 150  
- **Pattern**: Binary Search, Recursion  
- **Data Structure**: Binary Search Tree  
- **Algorithm**: DFS with directional pruning  
- **Tags**: Tree, DFS, Recursion, BST, Binary Search

## ☀️ Solution Code (with English Comments)

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If both nodes are smaller than root, search left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # If both nodes are greater than root, search right subtree
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Otherwise, we've found the split point — this is the LCA
        else:
            return root
```

## ☀️ Trace Example

Tree:
```
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      /
     3
```

Find LCA of p=2, q=4:

1. At root 6 → both p and q are smaller → go left  
2. At node 2 → one is 2 (equal), one is in right subtree (4) → this is the split  
✅ Return 2

## ☀️ Line-by-line Typing Script

- I define a recursive function to find the lowest common ancestor in a BST.
- If both p and q are smaller than the current root, I recursively search the left subtree.
- If both p and q are greater than the current root, I search the right subtree.
- If they split — meaning one is on the left and one on the right — or one equals the root, then the current node is their lowest common ancestor.
