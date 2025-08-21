# Leetcode 0104 - Maximum Depth of Binary Tree

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Match:** This is a Tree Traversal problem using either DFS (Depth-First Search) or BFS (Breadth-First Search). The key insight is that we need to explore all paths to find the deepest one. DFS recursive approach is most natural since tree depth has a recursive definition.

**Plan:**
1. Handle base case: empty tree has depth 0
2. For each node, recursively calculate depth of left and right subtrees
3. Current node's depth = 1 + maximum of left and right subtree depths
4. Return the calculated depth

**Implement:** See the code section below.

**Review:**
- Ensure we handle empty tree (null root) correctly
- Verify that we add 1 for current node to the maximum subtree depth
- Check edge cases like single node and linear trees

**Evaluate:**
- Time: O(n) - visit each node exactly once
- Space: O(h) where h is tree height - recursion stack depth

## ☀️ Why This Is a Tree DFS Problem

Tree depth calculation is naturally recursive because:
- **Each subtree's depth can be calculated independently**
- **Current node's depth depends on its children's depths**
- **We need to explore all paths to find the maximum**

Key insights:
- Depth has a recursive definition: depth(node) = 1 + max(depth(left), depth(right))
- DFS naturally follows the tree structure from root to leaves
- Each recursive call handles a smaller subproblem
- Base case (empty node) terminates the recursion cleanly

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root = [3,9,20,null,null,15,7]` | Standard balanced tree | `3` |
| `root = [1,null,2]` | Right-skewed tree | `2` |
| `root = [1]` | Single node | `1` |
| `root = []` | Empty tree | `0` |
| `root = [1,2,3,4,null,null,5]` | Unbalanced tree | `3` |

These test:
- Balanced and unbalanced tree structures
- Linear tree cases (left or right skewed)
- Minimal input sizes
- Empty tree boundary condition
- Trees where longest path doesn't go through deepest level

## ☀️ Code

### Solution 1: BFS Level Order Traversal (Brute Force)
**Time: O(n) → Visit each node exactly once**  
**Space: O(w) → Where w is maximum width of tree for queue storage**

```python
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            level_size = len(queue)
            depth += 1
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth
```

### Solution 2: Recursive DFS Top-Down (Classic Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: empty node has depth 0
        if not root:
            return 0
        
        # Recursively find depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Current depth is 1 + maximum of left and right depths
        return max(left_depth, right_depth) + 1
```

### Solution 3: Iterative DFS with Stack (Advanced Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Stack storage for DFS traversal**

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Stack stores (node, current_depth) pairs
        stack = [(root, 1)]
        max_depth = 0
        
        while stack:
            node, current_depth = stack.pop()
            max_depth = max(max_depth, current_depth)
            
            if node.left:
                stack.append((node.left, current_depth + 1))
            if node.right:
                stack.append((node.right, current_depth + 1))
        
        return max_depth
```

## ☀️ Notes

**Key Algorithm Components:**
- Base case handling for empty nodes (returns 0)
- Recursive depth calculation: max(left_depth, right_depth) + 1
- Tree traversal to visit all nodes and find maximum depth
- Proper handling of null children to avoid infinite recursion

**Critical Insight:**
The recursive solution directly implements the mathematical definition of tree depth. Each node's depth is one more than the maximum depth of its children, making the recursive approach both intuitive and efficient.

## ☀️ Coding Walkthrough Script

I'll solve this using recursive DFS, which naturally fits the tree depth definition.
The base case is straightforward: if the node is null, the depth is 0.
For any non-null node, I need to find the depth of both left and right subtrees recursively. The depth of the current node is then 1 plus the maximum of these two depths.
This approach works because tree depth has a recursive structure - each subtree's depth can be calculated independently, and the overall depth depends on the deepest subtree.
The recursion naturally terminates when we reach leaf nodes, where both children are null, giving us depth 0 for the base case.
The time complexity is O(n) since we visit each node exactly once, and space complexity is O(h) due to the recursion stack, where h is the tree height.

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| BFS Level Order | O(n) | O(w) | Level-by-level traversal | w = maximum tree width |
| Recursive DFS | O(n) | O(h) | Top-down recursive calls | **Recommended**; most intuitive |
| Iterative DFS | O(n) | O(h) | Stack-based simulation | Good for avoiding recursion limits |

## ☀️ Tree Depth Insights

- **Recursive definition:** depth(node) = 1 + max(depth(left_child), depth(right_child))
- **Base case:** empty nodes have depth 0
- **DFS vs BFS:** Both work, but DFS is more natural for depth calculation
- **Space consideration:** BFS uses O(w) space, DFS uses O(h) space
- **Interview preference:** Recursive DFS is cleanest and most expected

**Mathematical Guarantee:** Since we recursively calculate the maximum depth of all subtrees and take the maximum, we are guaranteed to find the globally maximum depth in the tree.

**Note:** Solution 2 (Recursive DFS) is the most recommended approach for interviews due to its elegance, clarity, and direct implementation of the depth definition. Solution 1 shows understanding of BFS, while Solution 3 demonstrates knowledge of recursion-to-iteration conversion.
