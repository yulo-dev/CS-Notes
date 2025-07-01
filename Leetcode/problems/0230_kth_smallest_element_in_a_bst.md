# Leetcode 0230 - Kth Smallest Element in a BST

## ☀️ UMPIRE
- **Understand**: Given a binary search tree (BST) and an integer k, return the k-th smallest element in the BST (1-indexed).
- **Match**: BST + in-order traversal (which yields sorted order)
- **Plan**:
  - Perform an in-order traversal of the tree (left-root-right)
  - Track how many nodes have been visited using a counter
  - When the counter reaches k, record the node value
- **Implement**: See below
- **Review**: Verify k is decremented in the correct spot (at root), and base case handles null nodes
- **Evaluate**:
  - Time: O(n) in worst case (unbalanced tree); O(h + k) on average
  - Space: O(h) for call stack, where h is the tree height

## ☀️ Metadata
- **Appears In**: Grind75, Blind75
- **Pattern**: In-order Traversal
- **Data Structure**: Binary Search Tree
- **Algorithm**: DFS (Depth-First Search), In-order
- **Tags**: Tree, BST, DFS, Inorder Traversal

## ☀️ Solution Code
```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Initialize counter and result container
        self.k = k                # Counts how many nodes we have left to visit
        self.res = None           # Stores the kth smallest value once found

        # Helper function to perform in-order traversal
        def inorder(node):
            if not node:
                return  # Base case: empty subtree, do nothing

            inorder(node.left)  # Recurse into left subtree (smaller values first)

            self.k -= 1         # Visit current node: decrement k
            if self.k == 0:     # If this is the kth node visited
                self.res = node.val  # Record its value as the answer
                return          # Early return to stop further traversal

            inorder(node.right) # Recurse into right subtree (larger values)

        # Start traversal from the root
        inorder(root)
        return self.res  # Return the result found during traversal
```


## ☀️ Trace Example
Tree:
```
      10
     /  \
    5    15
   / \   / \
  3   7 12 18
 / \
1   4
```
k = 3

In-order traversal sequence:
[1, 3, 4, 5, 7, 10, 12, 15, 18]
- Visit 1: k = 2
- Visit 3: k = 1
- Visit 4: k = 0 ✅ => return 4

## ☀️ Line-by-line Typing Script 
- Define the `kthSmallest` function with inputs `root` and `k`
- Store `k` as `self.k` and initialize an empty `self.res`
- Define a helper function `inorder(node)` to perform DFS
- Base case: if node is `None`, return
- Recurse into the left subtree first (smaller values)
- When we return to the current node, decrement `self.k`
- If `self.k` reaches 0, this node is the k-th smallest → save value
- Recurse into the right subtree to continue traversal if needed
- Call `inorder(root)` to start, and return the saved result

## ☀️ Debugging Notes
| Mistake | Explanation | Fix |
|--------|-------------|-----|
| Used `k` directly in recursion | Python ints are immutable, updates don't persist | Use `self.k` to maintain shared state |
| Forgot base case for null | Would crash on `None.left` | Add `if not node: return` |
| Visited root before left | Not sorted order | Use correct in-order: left → root → right |


## ☀️ Concept Recap
- In BST, in-order traversal yields nodes in ascending order
- Decrement `k` only when visiting the current node (not during traversal)
- Once `k == 0`, that node is the answer
- `self.k` and `self.res` are used to share state across recursion
