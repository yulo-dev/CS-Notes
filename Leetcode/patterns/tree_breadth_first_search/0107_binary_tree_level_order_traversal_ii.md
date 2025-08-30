# Leetcode 107 - Binary Tree Level Order Traversal II

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. This means we traverse level by level from left to right, but return the levels in reverse order (deepest level first, root level last).

**Key Clarification Questions to Ask Interviewer:**
1. "Should I return an empty array for null root?"
2. "Is it acceptable to do normal level order traversal and then reverse, or do you prefer building the result in reverse order directly?"
3. "Are there memory constraints I should consider for the reversal operation on large trees?"
4. "Should I optimize for time complexity or space complexity if there's a trade-off?"

**Match:** This is fundamentally a BFS problem with a twist - it's LeetCode 102 with result reversal.

"When I see 'bottom-up level order traversal', I immediately recognize this as a variation of the classic level order traversal problem. The key insight is that I can reuse the exact same BFS approach from LeetCode 102, then simply reverse the final result.

BFS is still the most intuitive approach because:
- Level order traversal is naturally a BFS operation
- The 'bottom-up' requirement is just a post-processing step
- I can leverage existing BFS knowledge and add one line for reversal

My plan is to use standard BFS with level tracking to build the normal level order result, then reverse it at the end. This gives me clean separation of concerns and reuses proven BFS patterns."

**Plan:**
1. Handle null root edge case by returning empty array
2. Use BFS to traverse tree level by level from top to bottom
3. Store each level's values in separate arrays
4. Reverse the final result to get bottom-up order

**Implement:** See the code section below.

**Review:**
- Edge case: Empty tree returns empty array
- Edge case: Single node returns array with one level
- Algorithm correctness: BFS ensures proper level order, reversal gives bottom-up
- Result format: Array of arrays with deepest level first

**Evaluate:**
- Time: O(n) - Visit each node once, reversal is O(levels) which is at most O(n)
- Space: O(n) - Queue stores up to n/2 nodes, result stores all n values

## ☀️ Why This Is a BFS Problem

This problem is essentially LeetCode 102 (Binary Tree Level Order Traversal) with a final reversal step. The core traversal logic remains identical - we need to visit nodes level by level from left to right. BFS naturally provides this ordering through its queue-based exploration pattern.

Key insights:
- Bottom-up requirement doesn't change the traversal method, only the result presentation
- BFS queue ensures we process all nodes at distance k before any nodes at distance k+1
- Reversal is a simple post-processing operation that doesn't affect the core algorithm choice
- We can directly reuse BFS patterns from standard level order traversal

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `null` | Empty tree | `[]` |
| `TreeNode(1)` | Single node tree | `[[1]]` |
| `[3,9,20,null,null,15,7]` | Multi-level tree | `[[15,7],[9,20],[3]]` |

These test:
- Null input boundary condition
- Simplest valid tree case
- Standard multi-level tree with bottom-up ordering

## ☀️ Code

### Solution 1: BFS with Deque then Reverse (Brute Force)

**Time: O(n) → Visit each node exactly once**
**Space: O(n) → Queue stores up to n/2 nodes, result stores all n values**

```python
def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
    # Edge case: empty tree
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    # Standard BFS level order traversal
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
    
    # Reverse to get bottom-up order
    return result[::-1]
```

### Solution 2: BFS with Lists then Reverse (Classic Solution)

**Time: O(n) → Visit each node once, reversal is O(levels) which is O(log n) to O(n)**
**Space: O(n) → Two lists store up to n/2 nodes each in worst case**

```python
def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
    # BFS with level tracking then reverse - most intuitive approach
    if not root:
        return []
    
    result = []
    current_level = [root]
    
    # Process level by level from top to bottom
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
    
    # Reverse to get bottom-up order
    return result[::-1]
```

### Solution 3: DFS with Pre-calculated Depth (Advanced Solution)

**Time: O(n) → Two passes through tree, no reversal needed**
**Space: O(h + n) → Recursion stack height plus result storage**

```python
def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
    # DFS approach building result in reverse order - avoids final reversal
    if not root:
        return []
    
    # First pass: determine tree depth
    def get_depth(node):
        if not node:
            return 0
        return 1 + max(get_depth(node.left), get_depth(node.right))
    
    depth = get_depth(root)
    result = [[] for _ in range(depth)]
    
    # Second pass: fill result from bottom up
    def dfs(node, level):
        if not node:
            return
        
        # Add to result in reverse level order (depth - 1 - level)
        result[depth - 1 - level].append(node.val)
        
        # Process children at next level
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    return result
```

## ☀️ Notes

**Key Algorithm Components:**
- BFS traversal mechanism to ensure level-by-level processing
- Level boundary tracking to group nodes correctly
- Result reversal or direct bottom-up construction

**Critical Insight:**
This problem is LeetCode 102 with a twist. Rather than reinventing traversal logic, recognize the pattern and add the reversal step. This demonstrates algorithmic pattern recognition and code reuse.

## ☀️ Coding Walkthrough Script

"I recognize this as a variation of the classic level order traversal problem. I'll use BFS to traverse the tree level by level, collecting values into separate arrays for each level. The key difference from standard level order traversal is that I need the result in bottom-up order, so I'll reverse the final result. 

For time complexity, I visit each node exactly once during BFS, giving me O(n). The reversal operation is O(levels), which is at most O(n) in a completely unbalanced tree, but typically O(log n) for balanced trees, so overall time complexity remains O(n).

For space complexity, my queue stores at most the width of the tree - up to n/2 nodes in the worst case of a complete binary tree. The result array stores all n node values. So space complexity is O(n).

The BFS approach is intuitive because level order traversal is naturally what BFS does - it processes all nodes at distance k before any nodes at distance k+1."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| BFS + Deque + Reverse | O(n) | O(n) | Standard BFS with post-processing | Clean separation |
| BFS + Lists + Reverse | O(n) | O(n) | Intuitive level tracking | **Recommended** |
| DFS + Pre-calculation | O(n) | O(h + n) | Direct bottom-up construction | Avoids reversal |

## ☀️ Binary Tree BFS Insights

- Level order traversal problems often have variations (top-down, bottom-up, zigzag)
- Core BFS logic remains consistent across these variations
- Post-processing (like reversal) is often simpler than changing the core algorithm
- Pattern recognition helps solve variations quickly by building on known solutions

**Mathematical Guarantee:** BFS ensures all nodes at level k are processed before any nodes at level k+1, maintaining proper level grouping regardless of final ordering.
