## ☀️ Leetcode 543 - Diameter of Binary Tree

### ☀️ Problem
Given the `root` of a binary tree, return the **length of the diameter** of the tree. The diameter of a binary tree is the **length of the longest path between any two nodes**, measured in **number of edges**. This path may or may not pass through the root.


### ☀️ UMPIRE Analysis

#### U — Understand
- We need to compute the longest path between any two nodes in a binary tree.
- The path length is measured by **number of edges**, not nodes.
- This path **can pass or not pass through the root**.
- Return `0` for an empty tree (since no path exists).

#### M — Match
- Binary Tree problem
- DFS (Post-order) traversal
- Global tracking of maximum result during recursion

#### P — Plan
1. Use a helper function `dfs(node)` to compute the height of each subtree.
2. At each node, calculate the diameter through it: `left_height + right_height`.
3. Update a global `self.max_diameter` if this value is larger.
4. Return the height of the current node's subtree: `max(left, right) + 1`.
5. Start DFS from the root and return `self.max_diameter`.

#### R — Review
- Confirmed: height is correctly computed with `max(left, right) + 1`
- Confirmed: diameter at each node is measured by `left + right`
- `self.max_diameter` properly tracks the global maximum

#### E — Evaluate
- Time: O(n), each node visited once
- Space: O(h), h = height of tree (stack space)
- Handles skewed trees and balanced trees properly

### ☀️ Solution
We use **DFS** (post-order traversal) to compute the **height of each subtree**, and at each node, calculate the path that passes through it:

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Global variable to store the maximum diameter found
        self.max_diameter = 0

        def dfs(node):
            # Base case: an empty node has height 0
            if not node:
                return 0

            # Recursively get the height of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # Update max_diameter if the path through this node is longer
            self.max_diameter = max(self.max_diameter, left + right)

            # Return the height of this subtree to the parent
            return max(left, right) + 1

        dfs(root)
        return self.max_diameter
```

### ☀️ Complexity
- **Time Complexity:** O(n), where n is the number of nodes. Each node is visited once.
- **Space Complexity:** O(h), where h is the height of the tree (due to recursion stack).


### ☀️ Key Concepts
- DFS (post-order)
- Recursion
- Binary Tree traversal
- Global state tracking


### ☀️ Notes
- At each node, we are not interested in the height itself, but rather the **sum of left and right subtree heights** as a candidate diameter.
- `return max(left, right) + 1` lets the parent node know how tall this subtree is.
- The final result is stored in `self.max_diameter`, which is updated along the way.

### ☀️ Verbal Walkthrough Script

- I'm solving the Diameter of Binary Tree problem using DFS. The idea is to find the longest path between any two nodes, which may or may not go through the root. 
- To do that, I define a helper function `dfs(node)` that returns the **height** of a subtree. While calculating height at each node, I also calculate the **diameter candidate** at that node, which is `left_height + right_height`.
- I keep a global variable `self.max_diameter` to store the maximum diameter seen so far.
- So for each node:
  - I recursively compute the height of the left and right children.
  - I update `self.max_diameter` with the sum of those heights.
  - Then I return `max(left, right) + 1` as this node’s height, so the parent node can use it.

- Finally, after the DFS completes, I return the value of `self.max_diameter`, which contains the longest path in terms of edges."

