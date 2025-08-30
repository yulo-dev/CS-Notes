# Leetcode 111 - Minimum Depth of Binary Tree

## ☀️ UMPIRE

**Understand:** Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node. A leaf is a node with no children.

**Key Clarification Questions to Ask Interviewer:**
1. "Should I return 0 for an empty tree (null root)?"
2. "For a node with only one child, do I need to continue to that child's subtree, or can I consider it a 'pseudo-leaf'?"
3. "Are there performance preferences between DFS and BFS approaches for this problem?"
4. "Should I optimize for the case where the minimum depth is likely to be small?"

**Match:** This is fundamentally a shortest path problem in a tree, which makes BFS the natural choice.

"When I see 'minimum depth' or 'shortest path', I immediately think BFS because BFS explores nodes level by level, guaranteeing that the first leaf node I encounter will be at the minimum depth.

BFS is particularly well-suited for this problem because:
- It processes all nodes at distance k before any nodes at distance k+1
- The first leaf node encountered is guaranteed to be at minimum depth
- I can terminate early as soon as I find any leaf, avoiding unnecessary exploration
- Unlike DFS, I don't need to explore all paths to find the minimum

My plan is to use BFS with level tracking, processing nodes level by level until I find the first leaf node, which will give me the minimum depth directly."

**Plan:**
1. Handle null root edge case by returning 0
2. Initialize BFS queue with root node and depth 1
3. Process nodes level by level using BFS
4. For each node, check if it's a leaf (no left or right child)
5. Return depth immediately when first leaf is found
6. Add children to queue with incremented depth for next level

**Implement:** See the code section below.

**Review:**
- Edge case: Empty tree returns 0
- Edge case: Single node (root only) returns 1
- Leaf definition: Node with no children (not just missing one child)
- Early termination: Return immediately on first leaf found

**Evaluate:**
- Time: O(n) - Best case terminates early, worst case visits all nodes
- Space: O(n) - Queue stores up to one complete level (n/2 nodes in complete tree)

## ☀️ Why This Is a BFS Problem

Minimum depth is essentially a shortest path problem in an unweighted tree. BFS is the optimal algorithm for finding shortest paths in unweighted graphs because it explores nodes in order of increasing distance from the source.

Key insights:
- BFS guarantees that nodes are visited in order of their depth from root
- The first leaf node encountered is guaranteed to be at minimum depth
- Early termination is possible - no need to explore deeper levels once a leaf is found
- DFS would need to explore all paths to ensure the minimum, making it less efficient

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `null` | Empty tree | `0` |
| `TreeNode(1)` | Single node tree | `1` |
| `[3,9,20,null,null,15,7]` | Unbalanced tree | `2` |
| `[1,2,null,3,null,4]` | Skewed tree | `4` |

These test:
- Null input boundary condition
- Simplest valid tree case
- Tree where left subtree has shorter path than right
- Tree where minimum depth requires going to actual leaf, not just missing child

## ☀️ Code

### Solution 1: DFS with Recursion (Brute Force)

**Time: O(n) → In worst case, visit all nodes if tree is completely unbalanced**
**Space: O(n) → Recursion stack in worst case (skewed tree)**

```python
def minDepth(self, root: Optional[TreeNode]) -> int:
    # DFS approach - simple but may visit unnecessary nodes
    if not root:
        return 0
    
    # Leaf node case
    if not root.left and not root.right:
        return 1
    
    # If only one child exists, go to that subtree
    if not root.left:
        return 1 + self.minDepth(root.right)
    if not root.right:
        return 1 + self.minDepth(root.left)
    
    # Both children exist, take minimum
    return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```

### Solution 2: BFS with Tuple Tracking (Classic Solution)

**Time: O(n) → Best case O(w) where w is width of first leaf level, worst case O(n)**
**Space: O(n) → Queue stores at most one level worth of nodes (up to n/2 in complete binary tree)**

```python
def minDepth(self, root: Optional[TreeNode]) -> int:
    # BFS approach with level tracking - optimal for minimum depth problems
    if not root:
        return 0

    queue = deque([(root, 1)])

    while queue:
        for _ in range(len(queue)):
            node, depth = queue.popleft()

            # Found first leaf - this is guaranteed minimum depth
            if not node.left and not node.right:
                return depth

            # Add children with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
```

### Solution 3: BFS with Level Counter (Advanced Solution)

**Time: O(n) → Best case O(w) where w is width of first leaf level, worst case O(n)**
**Space: O(n) → Queue stores at most one level worth of nodes (up to n/2 in complete binary tree)**

```python
def minDepth(self, root: Optional[TreeNode]) -> int:
    # BFS with explicit level counter - cleanest level-by-level approach
    if not root:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        level_size = len(queue)
        
        # Process entire current level
        for _ in range(level_size):
            node = queue.popleft()
            
            # First leaf found at this level
            if not node.left and not node.right:
                return depth
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```

## ☀️ Notes

**Key Algorithm Components:**
- BFS queue mechanism to process nodes level by level
- Leaf detection logic to identify termination condition
- Early termination to avoid unnecessary exploration

**Critical Insight:**
This problem demonstrates BFS's natural advantage for shortest path problems. The key insight is recognizing minimum depth as a shortest path problem rather than just a tree traversal problem.

## ☀️ Coding Walkthrough Script

"I recognize this as a shortest path problem - finding the minimum distance from root to any leaf. This immediately suggests BFS since BFS processes nodes in order of increasing distance from the source.

I'll use BFS with depth tracking, where I store each node with its current depth in the queue. As I process nodes level by level, the first leaf node I encounter is guaranteed to be at the minimum depth, allowing me to return immediately.

For time complexity, in the best case I only need to process nodes until I find the first leaf, which could be O(w) where w is the width of that level. In the worst case, if all leaves are at the deepest level, I process all O(n) nodes. So time complexity is O(n) in worst case.

For space complexity, my queue stores at most one complete level of the tree. In a complete binary tree, the widest level contains up to n/2 nodes, giving me O(n) space complexity.

The key advantage of BFS here is early termination - I can stop as soon as I find any leaf, unlike DFS which would need to explore all paths to guarantee the minimum."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| DFS Recursion | O(n) | O(n) | Explore all paths, take minimum | May visit unnecessary nodes |
| BFS with Tuple | O(n) | O(n) | Level-by-level with depth tracking | **Recommended** |
| BFS with Counter | O(n) | O(n) | Explicit level processing | Clean level-by-level logic |

## ☀️ Tree Shortest Path Insights

- Minimum depth problems are shortest path problems in disguise
- BFS naturally provides shortest path guarantees in unweighted structures
- Early termination is a key optimization for minimum/shortest path problems
- Level-by-level processing ensures optimal solution discovery order

**Mathematical Guarantee:** BFS ensures that all nodes at depth k are processed before any nodes at depth k+1, guaranteeing the first leaf found is at minimum depth.
