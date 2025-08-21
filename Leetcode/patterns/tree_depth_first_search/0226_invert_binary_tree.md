# Leetcode 0226 - Invert Binary Tree

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, invert the tree, and return its root. Inverting a binary tree means swapping the left and right children of every node in the tree.

**Match:** This is a Tree Traversal problem using DFS (Depth-First Search) or BFS (Breadth-First Search). The key insight is that we need to swap the left and right children for every node in the tree. This is a classic tree manipulation problem that can be solved recursively or iteratively.

**Plan:**
1. Handle the base case: empty tree returns None
2. For each node, swap its left and right children
3. Recursively apply the same operation to all subtrees
4. Return the modified tree root

**Implement:** See the code section below.

**Review:**
- Ensure we handle empty trees and single nodes correctly
- Verify that we swap children for every node, not just some
- Check that the tree structure is preserved (only children positions change)
- Confirm that we return the root after inversion

**Evaluate:**
- Time: O(n) - visit each node exactly once
- Space: O(h) where h is tree height - recursion stack depth

## ☀️ Why This Is a Tree DFS Problem

Tree inversion requires visiting every node and performing a local operation:
- **Every node needs the same operation applied (swap children)**
- **The operation is naturally recursive (invert subtree = invert children + invert each subtree)**
- **DFS allows us to process nodes in a systematic order**
- **Both pre-order and post-order traversals work effectively**

Key insights:
- Inversion is a local operation that affects node relationships
- Recursive structure: invert(tree) = swap children + invert(left) + invert(right)
- Can be done with either pre-order (swap first) or post-order (recurse first) traversal
- BFS also works but DFS is more natural for tree structure modifications

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root = [4,2,7,1,3,6,9]` | Complete binary tree | `[4,7,2,9,6,3,1]` |
| `root = [2,1,3]` | Simple three-node tree | `[2,3,1]` |
| `root = []` | Empty tree | `[]` |
| `root = [1]` | Single node | `[1]` |
| `root = [1,2]` | Two nodes (left child only) | `[1,null,2]` |
| `root = [1,null,2]` | Two nodes (right child only) | `[1,2]` |

These test:
- Complete and incomplete tree structures
- Empty tree boundary condition
- Single node edge case
- Trees with only left or right children
- Standard inversion scenarios

## ☀️ Code

### Solution 1: BFS Level Order Traversal (Brute Force)
**Time: O(n) → Visit each node exactly once**  
**Space: O(w) → Where w is maximum width of tree (queue storage)**

```python
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Use BFS to traverse level by level and swap children
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # Swap left and right children
                node.left, node.right = node.right, node.left
                
                # Add children to queue for next level processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root
```

### Solution 2: Recursive DFS Post-Order (Classic Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: If the current node is None, nothing to invert
        if not root:
            return None

        # Recursively invert the left and right subtrees first
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # After both subtrees are processed, swap them
        root.left = right
        root.right = left

        # Return the root with its left and right subtrees inverted
        return root
```

### Solution 3: Recursive DFS Pre-Order (Advanced Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: empty node needs no inversion
        if not root:
            return None
        
        # Swap the left and right children first (pre-order)
        root.left, root.right = root.right, root.left
        
        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
```

## ☀️ Notes

**Key Algorithm Components:**
- Base case handling for empty nodes (return None)
- Child swapping operation: swap left and right children
- Recursive application to all subtrees
- Proper return of the modified tree root

**Critical Insight:**
Tree inversion is a perfect example of divide-and-conquer. The problem can be broken down into smaller subproblems: invert the left subtree, invert the right subtree, then swap them. The choice between pre-order and post-order traversal is a matter of style - both work correctly.

## ☀️ Coding Walkthrough Script

I'll solve this using recursive DFS with a post-order traversal approach.
The base case is simple: if the current node is None, there's nothing to invert, so I return None.
For any non-null node, I first recursively invert the left and right subtrees. This follows the divide-and-conquer principle - I solve the smaller subproblems first.
After both subtrees are completely inverted, I swap them by assigning the inverted right subtree to the left position and the inverted left subtree to the right position.
Finally, I return the current node, which now has its subtrees properly inverted and swapped.
This post-order approach is elegant because it ensures that when I perform the swap, both subtrees are already fully processed. The time complexity is O(n) since I visit each node exactly once, and the space complexity is O(h) due to the recursion stack."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| BFS Level Order | O(n) | O(w) | Level-by-level processing | w = maximum tree width |
| DFS Post-Order | O(n) | O(h) | Recurse first, then swap | **Recommended**; most elegant |
| DFS Pre-Order | O(n) | O(h) | Swap first, then recurse | Alternative recursive style |

## ☀️ Tree Inversion Insights

- **Local operation:** Each node only needs its immediate children swapped
- **Recursive structure:** Inversion naturally breaks into smaller subproblems
- **Traversal flexibility:** Both pre-order and post-order work correctly
- **Post-order advantage:** Clearer logic flow (solve subproblems first)
- **Pre-order advantage:** Slightly more concise code with tuple swapping

**Mathematical Guarantee:** Since we apply the swap operation to every node in the tree exactly once, and recursion ensures we reach every node, the entire tree will be correctly inverted.

**Note:** Solution 2 (Post-Order DFS) is the most recommended approach for interviews due to its clear logical flow and explicit variable handling. It demonstrates strong understanding of recursion and tree traversal principles. The post-order approach makes the algorithm easier to trace and debug, which is valuable during interviews.
