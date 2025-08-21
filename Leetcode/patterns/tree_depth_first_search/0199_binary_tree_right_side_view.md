# Leetcode 0199 - Binary Tree Right Side View

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom. This means we need to find the rightmost node at each level of the tree.

**Match:** This is a Tree Traversal problem that can be solved with either BFS (Breadth-First Search) or DFS (Depth-First Search). The key insight is that we need to identify the rightmost node at each level. BFS naturally processes level by level, while DFS can use right-first traversal with level tracking.

**Plan:**
1. Traverse the tree level by level (BFS) or with depth tracking (DFS)
2. For each level/depth, identify the rightmost node
3. Add the rightmost node value to the result
4. Return the collected values in top-to-bottom order

**Implement:** See the code section below.

**Review:**
- Ensure we capture exactly one node per level (the rightmost one)
- Verify that we handle empty trees and single nodes correctly
- Check that nodes are returned in top-to-bottom order
- Confirm that we don't miss any levels

**Evaluate:**
- Time: O(n) - visit each node exactly once
- Space: O(w) for BFS queue or O(h) for DFS recursion stack

## ☀️ Why This Is a Tree Level/Depth Traversal Problem

Right side view requires understanding tree structure by levels:
- **We need exactly one node per level (the rightmost)**
- **Level-by-level processing naturally fits the problem**
- **Both BFS and DFS can solve this with different approaches**
- **BFS processes complete levels, DFS tracks depth during traversal**

Key insights:
- BFS approach: process each level completely and take the last node
- DFS approach: use right-first traversal so first node at each depth is rightmost
- Level/depth tracking is essential for both approaches
- The "right side view" is equivalent to "rightmost node per level"

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root = [1,2,3,null,5,null,4]` | Standard tree with right bias | `[1,3,4]` |
| `root = [1,2,3,4]` | Left-heavy tree | `[1,3,4]` |
| `root = [1,2]` | Only left child | `[1,2]` |
| `root = [1,null,3]` | Only right child | `[1,3]` |
| `root = [1]` | Single node | `[1]` |
| `root = []` | Empty tree | `[]` |

These test:
- Trees with varying structures (left-heavy, right-heavy, balanced)
- Single child scenarios
- Empty tree boundary condition
- Single node edge case
- Standard right side view scenarios

## ☀️ Code

### Solution 1: BFS with Full Level Storage (Brute Force)
**Time: O(n) → Visit each node exactly once**  
**Space: O(w) → Where w is maximum width of tree (queue + level storage)**

```python
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes at current level
            for i in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Take the rightmost node from current level
            result.append(current_level[-1])
        
        return result
```

### Solution 2: Optimized BFS - Track Only Rightmost Node (Classic Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(w) → Where w is maximum width of tree (queue storage only)**

```python
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            # Process all nodes at current level
            for i in range(level_size):
                node = queue.popleft()
                
                # If this is the last node in current level, add to result
                if i == level_size - 1:
                    result.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
```

### Solution 3: DFS with Depth Tracking (Advanced Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return

            # If this is the first time we visit this depth level,
            # this node is the rightmost so far (due to right-first traversal)
            if depth == len(res):
                res.append(node.val)
            
            # Traverse right first, then left (to ensure rightmost is captured first)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res
```

## ☀️ Notes

**Key Algorithm Components:**
- Level/depth identification to group nodes properly
- Rightmost node selection strategy (last in BFS or first in right-first DFS)
- Proper tree traversal to visit all nodes exactly once
- Result collection in top-to-bottom order

**Critical Insight:**
The problem has two main approaches: BFS naturally processes complete levels making rightmost identification straightforward, while DFS uses clever right-first traversal where the first node encountered at each depth is guaranteed to be the rightmost.

## ☀️ Coding Walkthrough Script

I'll solve this using DFS with depth tracking for optimal space complexity.
The key insight is that if I traverse the tree in a right-first manner, the first node I encounter at each depth will be the rightmost node at that level.
I'll use a closure pattern where my DFS function can access the result array directly. For each node, I check if this is the first time I'm visiting this depth by comparing the depth with the current length of my result array.
If it's a new depth, I add this node's value to the result since it's guaranteed to be the rightmost at this level due to my right-first traversal order.
Then I recursively visit the right subtree first, followed by the left subtree. This ensures that for any given depth, the rightmost node is always encountered before any other nodes at that same depth.
The time complexity is O(n) since I visit each node exactly once, and the space complexity is O(h) for the recursion stack.
In balanced trees, this is better than the O(w) space required by BFS approaches, where h = O(log n) and w = O(n). However, in skewed trees, BFS may be more space-efficient with w = O(1) while h = O(n).

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| BFS Full Level | O(n) | O(w) | Store complete levels | Simple but memory inefficient |
| BFS Optimized | O(n) | O(w) | Track only rightmost per level | **Most common interview solution** |
| DFS Depth Tracking | O(n) | O(h) | Right-first traversal | **Most space efficient**; elegant |

## ☀️ Tree Right Side View Insights

- **Core concept:** Right side view = rightmost node at each level/depth
- **BFS advantage:** Natural level-by-level processing matches problem description
- **DFS advantage:** Better space complexity O(h) vs O(w), especially for wide trees
- **Right-first traversal:** Clever technique to ensure rightmost nodes are encountered first
- **Closure pattern:** Clean way to avoid passing extra parameters in DFS

**Mathematical Guarantee:** Since we systematically visit every level/depth and apply a consistent strategy to identify the rightmost node (either last in level or first in right-first traversal), we are guaranteed to capture exactly one node per level in the correct order.

**Note:** Solution 3 (DFS with Depth Tracking) is the most recommended approach for advanced interviews due to its superior space complexity and elegant use of right-first traversal. Solution 2 (Optimized BFS) is the most intuitive and commonly expected solution. The DFS approach particularly showcases understanding of tree traversal optimization and closure patterns.
