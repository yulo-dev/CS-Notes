# Leetcode 103 - Binary Tree Zigzag Level Order Traversal

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. This means we traverse level by level, but alternate the direction: left-to-right for the first level, right-to-left for the second level, left-to-right for the third level, and so on.

**Key Clarification Questions to Ask Interviewer:**
1. "Should I return an empty array for null root, consistent with other level order traversal problems?"
2. "For the zigzag pattern, does level 0 (root) count as left-to-right, or should I clarify the starting direction?"
3. "Are there performance preferences between reversing arrays versus using deque insertion directions?"
4. "Should I optimize for code readability or minimize the number of operations?"

**Match:** This is a BFS problem with directional control - essentially LeetCode 102 with alternating level directions.

"When I see 'zigzag level order traversal', I recognize this as a variation of the standard level order traversal with a direction pattern. The core is still BFS since I need to process nodes level by level, but I need to handle the alternating left-right, right-left pattern.

BFS remains the natural choice because:
- Level order traversal is fundamentally what BFS does
- The zigzag requirement is just a presentation layer on top of standard BFS
- I can collect each level normally, then decide whether to reverse based on the level number

My plan is to use standard BFS to collect nodes level by level, then apply direction logic by either keeping the level as-is or reversing it before adding to the result. This separates the traversal logic from the direction logic cleanly."

**Plan:**
1. Handle null root edge case by returning empty array
2. Use BFS to traverse tree level by level
3. For each level, collect all node values in left-to-right order
4. Apply zigzag logic: keep even levels as-is, reverse odd levels
5. Toggle direction flag after each level

**Implement:** See the code section below.

**Review:**
- Edge case: Empty tree returns empty array
- Edge case: Single node returns array with one level
- Direction pattern: Level 0 left-to-right, level 1 right-to-left, alternating
- Algorithm correctness: BFS ensures level boundaries, direction logic handles zigzag

**Evaluate:**
- Time: O(n) - Visit each node once, reverse operations total O(n) across all levels
- Space: O(n) - Queue stores up to n/2 nodes, result stores all n values

## ☀️ Why This Is a BFS Problem

Zigzag level order traversal is still fundamentally a level order traversal problem, just with alternating direction per level. BFS naturally processes nodes level by level, which is exactly what we need. The zigzag requirement doesn't change the traversal method - it only affects how we present each level's results.

Key insights:
- The traversal order (visiting nodes) remains the same as standard BFS
- Only the result presentation (left-to-right vs right-to-left) changes per level
- We can separate concerns: use BFS for traversal, apply direction logic for presentation
- Level boundaries are naturally maintained by BFS queue mechanics

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `null` | Empty tree | `[]` |
| `TreeNode(1)` | Single node tree | `[[1]]` |
| `[3,9,20,null,null,15,7]` | Standard multi-level | `[[3],[20,9],[15,7]]` |

These test:
- Null input boundary condition
- No zigzag needed for single level
- Multiple levels with alternating directions

## ☀️ Code

### Solution 1: BFS with Level Counter and Reverse (Brute Force)

**Time: O(n) → Visit each node once, plus O(level_width) for reverse operations**
**Space: O(n) → Queue stores up to n/2 nodes, result stores all n values**

```python
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # Edge case: empty tree
    if not root:
        return []
    
    result = []
    queue = deque([root])
    level = 0
    
    # BFS with level tracking
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
        
        # Reverse odd levels for zigzag pattern
        if level % 2 == 1:
            current_level.reverse()
        
        result.append(current_level)
        level += 1
    
    return result
```

### Solution 2: BFS with Direction Flag and Conditional Reverse (Classic Solution)

**Time: O(n) → Visit each node exactly once, reverse operations total O(n) across all levels**
**Space: O(n) → Queue stores up to n/2 nodes, result stores all n values**

```python
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # BFS with conditional reverse - clean and intuitive approach
    if not root:
        return []

    queue = deque([root])
    result = []
    left_to_right = True
    
    while queue:
        level = []

        # Process all nodes in current level
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Add level to result with correct direction
        if left_to_right:
            result.append(level)
        else:
            result.append(level[::-1])

        left_to_right = not left_to_right

    return result
```

### Solution 3: DFS with Level Tracking and Insertion Control (Advanced Solution)

**Time: O(n) → DFS visits each node once, insertion operations are O(1) or O(k) per node**
**Space: O(h + n) → Recursion stack height plus result storage**

```python
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # DFS approach with level tracking and direction control
    if not root:
        return []
    
    result = []
    
    def dfs(node, level):
        if not node:
            return
        
        # Expand result if we reach a new level
        if level >= len(result):
            result.append([])
        
        # Insert based on level parity
        if level % 2 == 0:
            result[level].append(node.val)         # Left to right
        else:
            result[level].insert(0, node.val)      # Right to left
        
        # Recursively process children
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    return result
```

## ☀️ Notes

**Key Algorithm Components:**
- BFS traversal mechanism for level-by-level processing
- Direction tracking to determine when to reverse level results
- Level boundary detection to apply direction changes correctly

**Critical Insight:**
Zigzag traversal doesn't require a fundamentally different algorithm - it's standard BFS with directional post-processing. The key is recognizing this as a presentation problem rather than a traversal problem.

## ☀️ Coding Walkthrough Script

"I recognize this as a level order traversal with alternating directions. I'll use BFS to process nodes level by level, collecting each level's values normally from left to right. Then I'll apply the zigzag logic by checking if the current level number is odd - if so, I'll reverse the level before adding it to my result.

For time complexity, I visit each node exactly once during BFS, giving me O(n) for the traversal. The reverse operations might seem like extra work, but if I analyze it carefully: the total cost of all reverse operations across all levels equals O(n), since I'm only reversing each node's value once throughout the entire algorithm. So my overall time complexity remains O(n).

For space complexity, my queue stores at most the width of the tree - up to n/2 nodes in a complete binary tree. My result stores all n node values. The additional space for level arrays and direction tracking is negligible. So space complexity is O(n).

The BFS approach is natural because level order traversal is exactly what BFS provides, and the zigzag requirement is just a matter of selectively reversing certain levels."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Level Counter + Reverse | O(n) | O(n) | Math-based level detection | Clean logic |
| Direction Flag + Reverse | O(n) | O(n) | State-based direction control | **Recommended** |
| DFS + Insertion Control | O(n) | O(h + n) | Direct insertion by direction | Avoids reversal |

## ☀️ Binary Tree Level Traversal Insights

- Level order variations (normal, bottom-up, zigzag) share the same core BFS structure
- Direction and presentation logic can often be separated from traversal logic
- Post-processing approaches (like reversal) are often simpler than modifying core algorithms
- Pattern recognition helps solve variations efficiently by building on known solutions

**Mathematical Guarantee:** BFS ensures all nodes at level k are processed before any nodes at level k+1, providing the level boundaries needed for zigzag direction changes.
