# Leetcode 199 - Binary Tree Right Side View

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom. This means we need to find the rightmost visible node at each level of the tree.

**Key Clarification Questions to Ask Interviewer:**
1. "Should I return an empty array for a null root?"
2. "When a level has only left children (no right children), should the leftmost node be considered 'visible from the right'?"
3. "Should the result be ordered from top to bottom (root level first)?"
4. "Are there performance preferences between level-order traversal and depth-first approaches?"

**Match:** This is a level-order traversal problem where we need to capture the rightmost node from each level.

"When I see 'right side view', I recognize this as a level-order processing problem where I need the rightmost visible node from each level. The key insight is that 'rightmost visible' doesn't necessarily mean 'right child' - it means the last node when viewing each level from left to right.

This can be solved with either BFS or DFS approaches:
- BFS naturally processes levels, so I can easily capture the last node of each level
- DFS with right-first traversal ensures the first node I visit at each depth is the rightmost

My plan is to use BFS for the most intuitive approach, processing each level completely and capturing the rightmost node (last node processed in each level). This directly maps to the problem requirement of viewing from the right side."

**Plan:**
1. Handle null root edge case by returning empty array
2. Use BFS to process tree level by level
3. For each level, track which node is the last one processed
4. Add the last node's value from each level to result
5. Return result array with rightmost visible nodes from top to bottom

**Implement:** See the code section below.

**Review:**
- Edge case: Empty tree returns empty array
- Edge case: Single node returns array with that node
- Rightmost logic: Last node processed in each level, not necessarily right child
- Level boundaries: Properly track when each level ends

**Evaluate:**
- Time: O(n) - Visit each node once during traversal
- Space: O(w) → O(n) worst case, where w is maximum width of tree level

## ☀️ Why This Is a Level Order Traversal Problem

Right side view is fundamentally about identifying the rightmost visible node at each level of the tree. This requires level-by-level processing to determine which node is actually visible from the right side at each depth.

Key insights:
- "Rightmost visible" means the last node when traversing each level left to right
- A left child can be rightmost visible if no right siblings exist at that level
- Level boundaries are crucial - we need to know which nodes belong to the same level
- Both BFS and DFS can solve this, but with different approaches to level tracking

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `null` | Empty tree | `[]` |
| `TreeNode(1)` | Single node | `[1]` |
| `[1,2,3,null,5,null,4]` | Standard case | `[1,3,4]` |
| `[1,2,3,4]` | Left child visible | `[1,3,4]` |

These test:
- Null input boundary condition
- Single level tree
- Multiple levels with clear rightmost nodes
- Case where left child is rightmost visible in its level

## ☀️ Code

### Solution 1: BFS Level Order Traversal (Brute Force)

**Time: O(n) → Visit each node once in level order traversal**
**Space: O(w) → O(n) worst case, where w is max width of tree level**

```python
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    # BFS level order traversal - capture rightmost node of each level
    if not root:
        return []
    
    res = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            # Last node in current level is rightmost visible node
            if i == level_size - 1:
                res.append(node.val)
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    return res
```

### Solution 2: DFS Right-First Traversal (Classic Solution)

**Time: O(n) → Visit each node once in DFS traversal**
**Space: O(h) → O(n) worst case, where h is height of tree (balanced O(log n), skewed O(n))**

```python
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    # DFS with right-first traversal - first node at each depth is rightmost
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

### Solution 3: DFS with Level Mapping (Advanced Solution)

**Time: O(n) → Visit each node once, but may store more nodes in result tracking**
**Space: O(h + d) → O(n) worst case, where h is recursion depth and d is tree depth**

```python
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    # Alternative DFS approach - update rightmost node for each level
    if not root:
        return []
    
    level_map = {}
    
    def dfs(node, depth):
        if not node:
            return
        
        # Always update with current node (later nodes at same depth override)
        level_map[depth] = node.val
        
        # Traverse left first, then right (so right nodes override left nodes)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    
    dfs(root, 0)
    
    # Extract values in level order
    return [level_map[i] for i in range(len(level_map))]
```

## ☀️ Notes

**Key Algorithm Components:**
- Level boundary detection to identify rightmost node at each level
- Queue management (BFS) or depth tracking (DFS) for level processing
- Right-first traversal logic to ensure correct rightmost node identification

**Critical Insight:**
"Right side view" doesn't mean "right children only" - it means the rightmost visible node at each level. A left child can be rightmost visible if it's the only node at that level or if no right siblings exist.

## ☀️ Coding Walkthrough Script

"I need to find the rightmost visible node at each level of the tree. This is essentially a level-order traversal problem where I capture the last node processed at each level.

I'll use BFS to process the tree level by level. For each level, I'll process all nodes from left to right, keeping track of which node is the last one in that level. The last node processed in each level is the rightmost visible node from that level.

For time complexity, I visit each node exactly once during the BFS traversal, giving me O(n). For space complexity, my queue stores at most one complete level of nodes. In a complete binary tree, the widest level contains up to n/2 nodes, so worst case space complexity is O(w) where w can be up to n, making it O(n) worst case.

The key insight is that level boundaries are crucial here - I need to know exactly when each level ends so I can identify which node is truly the rightmost at that level. The BFS approach makes this natural since I process complete levels at a time."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| BFS Level Order | O(n) | O(w) → O(n) | Process levels, capture last node | Intuitive approach |
| DFS Right-First | O(n) | O(h) → O(n) | Right-first traversal | **Recommended** |
| DFS Level Map | O(n) | O(h + d) → O(n) | Track rightmost per level | Alternative organization |

## ☀️ Tree Level Processing Insights

- Right side view problems require level-aware processing
- "Visible from right" means rightmost at each level, not necessarily right children
- BFS naturally handles level boundaries, DFS requires depth tracking
- Right-first DFS is an elegant alternative to level-order BFS

**Mathematical Guarantee:** The rightmost visible node at each level is the last node encountered when traversing that level from left to right.
