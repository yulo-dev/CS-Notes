# Leetcode 102 - Binary Tree Level Order Traversal

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, return the level order traversal of its nodes' values. We need to traverse the tree level by level from left to right, collecting values at each level into separate arrays.

**Key Clarification Questions to Ask Interviewer:**
1. "Should I return an empty array if the root is null, or should I handle this as an error case?"
2. "Are there any constraints on the tree size? Should I be concerned about memory limits for very wide trees?"
3. "Should the traversal be strictly left-to-right within each level, or is right-to-left acceptable?"
4. "Are there any constraints on the node values? Can they be negative or duplicate?"
5. "Should I optimize for time complexity, space complexity, or code readability?"
6. "Since BFS is O(n) in both time and space, is there any preference for using DFS here?"

**Match:** This is definitely a BFS (Breadth-First Search) problem, and here's my reasoning: 

"When I see 'level order traversal', I immediately think BFS because the problem is asking me to process nodes by their distance from the root. Level order means I need to visit all nodes at depth 0, then all nodes at depth 1, then depth 2, and so on. This is exactly what BFS does naturally - it explores all neighbors at the current depth before moving to the next depth level.

I could technically use DFS with level tracking, but BFS is the most intuitive approach because:
- The queue in BFS naturally maintains the order I need to process nodes
- I can easily track level boundaries by checking queue size
- The algorithm directly maps to the problem requirements without additional complexity

My plan is to use an iterative BFS approach with a queue, processing one complete level at a time before moving to the next level. This gives me clean level boundaries and optimal performance."

**Plan:**
1. Handle edge case where root is null - return empty array
2. Initialize queue with root node and result array
3. While queue is not empty, process all nodes at current level
4. For each level, track level size and collect node values
5. Add children of current level nodes to queue for next iteration

**Implement:** See the code section below.

**Review:**
- Edge case: Empty tree returns empty array
- Edge case: Single node tree returns array with single level
- Algorithm correctness: BFS guarantees level-by-level processing
- All nodes are visited exactly once

**Evaluate:**
- Time: O(n) - Each node is visited exactly once during traversal
- Space: O(n) - Queue stores up to n/2 nodes in worst case, result stores all n values

## ☀️ Why This Is a BFS Problem

Level order traversal is fundamentally a BFS problem because we need to explore nodes "horizontally" (level by level) rather than "vertically" (depth-first). BFS naturally processes nodes in the order we need - all nodes at distance k before any nodes at distance k+1.

Key insights:
- Level order traversal requires processing nodes by their distance from root
- BFS explores nodes in order of increasing distance from starting point
- Each level of the tree corresponds to nodes at the same distance from root
- Queue data structure ensures First-In-First-Out processing needed for level order

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `null` | Empty tree | `[]` |
| `TreeNode(1)` | Single node tree | `[[1]]` |
| `[3,9,20,null,null,15,7]` | Complete binary tree | `[[3],[9,20],[15,7]]` |

These test:
- Boundary condition of empty input
- Simplest valid input case
- Standard multi-level tree structure

## ☀️ Code

### Solution 1: BFS with Deque (Brute Force)

**Time: O(n) → Visit each node exactly once**
**Space: O(n) → Queue stores at most the width of the tree (maximum nodes at any level)**

```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # Edge case: empty tree
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    # Process each level
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```

### Solution 2: BFS with Lists (Classic Solution)

**Time: O(n) → Visit each node exactly once using BFS approach**
**Space: O(n) → Queue stores up to n/2 nodes in worst case (complete binary tree last level)**

```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # BFS with level tracking - most common interview approach
    if not root:
        return []
    
    result = []
    current_level = [root]
    
    # Process level by level
    while current_level:
        level_values = []
        next_level = []
        
        # Process all nodes in current level
        for node in current_level:
            level_values.append(node.val)
            
            # Collect children for next level
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        
        result.append(level_values)
        current_level = next_level
    
    return result
```

### Solution 3: DFS with Level Tracking (Advanced Solution)

**Time: O(n) → DFS visits each node once, list operations are O(1) amortized**
**Space: O(h + n) → Recursion stack height + result storage**

```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # DFS approach with level tracking - demonstrates depth-first alternative
    if not root:
        return []
    
    result = []
    
    def dfs(node, level):
        if not node:
            return
        
        # Expand result if we reach a new level
        if level >= len(result):
            result.append([])
        
        # Add current node to its level
        result[level].append(node.val)
        
        # Recursively process children at next level
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    return result
```

## ☀️ Notes

**Key Algorithm Components:**
- Queue or list to track nodes at current processing level
- Level size tracking to know when current level is complete
- Result structure to store values grouped by level

**Critical Insight:**
Level order traversal is essentially BFS applied to trees. The key is maintaining level boundaries while processing nodes in breadth-first order.

## ☀️ Walkthrough Script

"I'll solve this step by step. First, I recognize this is a level order traversal, which is a classic BFS problem. I'll use a queue to process nodes level by level. For each level, I'll track how many nodes are in the current level, process all of them, and add their children to the queue for the next level. This ensures I collect values level by level from left to right."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| BFS with Deque | O(n) | O(n) | Use deque with level size tracking | Standard approach |
| BFS with Lists | O(n) | O(n) | Use two lists for current/next level | **Recommended** |
| DFS with Level | O(n) | O(h + n) | Recursion with level parameter | Alternative approach |

## ☀️ BFS Tree Traversal Insights

- BFS naturally processes nodes in level order due to queue's FIFO nature
- Level boundaries are maintained by tracking queue size at start of each level
- Space complexity is dominated by the widest level of the tree (up to n/2 nodes)

**Mathematical Guarantee:** BFS ensures all nodes at distance k from root are processed before any nodes at distance k+1.
