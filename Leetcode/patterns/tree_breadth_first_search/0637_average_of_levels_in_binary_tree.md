# Leetcode 637 - Average of Levels in Binary Tree

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. For each level of the tree, we need to calculate the arithmetic mean of all node values at that level and return these averages from top to bottom.

**Key Clarification Questions to Ask Interviewer:**
1. "Should I return an empty array for a null root?"
2. "Is O(n) time with O(w) space acceptable? Is recursion OK, or do you prefer iterative?"
3. "Are negative node values possible, and does this affect the calculation approach?"
4. "Output order is top-down by level, correct?"
5. "Could the depth be large enough to risk stack overflow if I use recursion?"

**Match:** This is a level-order processing problem where we need to compute aggregate statistics (averages) for each level.

"When I see 'average of levels', I recognize this as a level-order traversal problem where I need to process complete levels to calculate statistics. The key requirement is to compute the arithmetic mean for each level, which requires both the sum and count of nodes at each level.

BFS is the natural choice for this problem because:
- I need to process complete levels to calculate accurate averages
- Level boundaries are crucial for separating calculations
- I can compute averages incrementally as I process each level
- The problem structure directly maps to BFS level-by-level processing

My plan is to use BFS to process each level completely, calculating the sum and count of nodes for each level, then computing the average before moving to the next level. This approach is both intuitive and efficient."

**Plan:**
1. Handle null root edge case by returning empty array
2. Use BFS with queue to process tree level by level
3. For each level, calculate sum and count of all node values
4. Compute average (sum/count) and add to result array
5. Continue until all levels are processed

**Implement:** See the code section below.

**Review:**
- Edge case: Empty tree returns empty array
- Edge case: Single node returns array with that node's value as float
- Arithmetic: Ensure proper float division for averages
- Overflow: Consider potential integer overflow for large sums

**Evaluate:**
- Time: O(n) - Visit each node once during level-order traversal
- Space: O(w) → O(n) worst case, where w is maximum width of tree level

## ☀️ Why This Is a Level Order Processing Problem

Average of levels requires computing aggregate statistics for each level of the tree. This necessitates level-aware processing where we can identify which nodes belong to the same level and process them as a group to calculate the arithmetic mean.

Key insights:
- Averages require both sum and count for each level
- Level boundaries are essential for accurate calculations  
- Processing must be level-complete to avoid mixing statistics across levels
- BFS naturally provides the level-by-level structure needed

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `null` | Empty tree | `[]` |
| `TreeNode(1)` | Single node | `[1.0]` |
| `[3,9,20,null,null,15,7]` | Multi-level tree | `[3.0, 14.5, 11.0]` |
| `[1,-5,-5,1,null,0]` | Negative values | `[1.0, -5.0, 0.5]` |

These test:
- Null input boundary condition
- Single level calculation
- Standard multi-level average calculation
- Negative numbers and mixed positive/negative values

## ☀️ Code

### Solution 1: BFS Level Order Processing (Classic Solution)

**Time: O(n) → Visit each node once during level order traversal**
**Space: O(w) → O(n) worst case, where w is max width of tree level**

```python
def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    # BFS level order traversal - calculate average for each level
    if not root:
        return []

    queue = deque([root])
    res = []

    while queue:
        level_sum = 0
        level_len = len(queue)

        # Process all nodes in current level
        for _ in range(level_len):
            node = queue.popleft()
            level_sum += node.val

            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        # Calculate and store average for this level
        res.append(level_sum / level_len)
    
    return res
```

### Solution 2: DFS with Sum and Count Arrays (Alternative Solution)

**Time: O(n) → Visit each node once in DFS traversal**
**Space: O(d) → O(n) worst case, where d is tree depth (recursion stack + level arrays)**

```python
def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    # DFS approach - collect level sums and counts, then calculate averages
    if not root:
        return []
    
    level_sums = []
    level_counts = []
    
    def dfs(node, depth):
        if not node:
            return
        
        # Expand arrays if we reach a new depth
        if depth >= len(level_sums):
            level_sums.append(0)
            level_counts.append(0)
        
        # Add current node to its level's sum and count
        level_sums[depth] += node.val
        level_counts[depth] += 1
        
        # Recurse on children
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    
    dfs(root, 0)
    
    # Calculate averages from sums and counts
    return [level_sums[i] / level_counts[i] for i in range(len(level_sums))]
```

### Solution 3: DFS with Level Value Storage (Advanced Solution)

**Time: O(n) → Visit each node once, final average calculation also O(n) for all levels**
**Space: O(n) → Store all node values in level_map plus recursion stack O(d)**

```python
def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    # DFS with level mapping approach - store all values per level
    if not root:
        return []
    
    level_map = {}
    
    def dfs(node, depth):
        if not node:
            return
        
        # Initialize list for new level
        if depth not in level_map:
            level_map[depth] = []
        
        # Add node value to its level
        level_map[depth].append(node.val)
        
        # Recurse on children
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    
    dfs(root, 0)
    
    # Calculate averages from stored values
    return [sum(level_map[i]) / len(level_map[i]) for i in range(len(level_map))]
```

## ☀️ Notes

**Key Algorithm Components:**
- Level-by-level processing to maintain calculation boundaries
- Sum and count tracking for accurate average computation
- Proper float division to ensure decimal results

**Critical Insight:**
This problem demonstrates why BFS is often preferred for level-based aggregate calculations. The natural level boundaries in BFS make it easy to compute statistics for complete levels without additional bookkeeping.

## ☀️ Coding Walkthrough Script

"I need to calculate the average value for each level of the binary tree. This requires processing nodes level by level and computing the arithmetic mean for each level separately.

I'll use BFS to process the tree level by level. For each level, I'll maintain a running sum and count of all nodes at that level. After processing all nodes in a level, I can calculate the average by dividing the sum by the count.

For time complexity, I visit each node exactly once during the BFS traversal, giving me O(n). For space complexity, my queue stores at most one complete level of nodes. In a complete binary tree, the widest level contains up to n/2 nodes, so worst case space complexity is O(w) where w can be up to n, making it O(n) worst case.

The key advantage of BFS here is that it naturally processes complete levels, which aligns perfectly with the requirement to calculate per-level statistics. I don't need additional bookkeeping to track level boundaries since BFS inherently provides this structure."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| BFS Level Processing | O(n) | O(w) → O(n) | Direct level-by-level calculation | **Recommended** |
| DFS Sum/Count Arrays | O(n) | O(d) → O(n) | Collect statistics, then calculate | Space efficient |
| DFS Value Storage | O(n) | O(n) | Store all values, then calculate | Most memory usage |

## ☀️ Tree Level Statistics Insights

- Level-based aggregate calculations naturally favor BFS approaches
- Average computation requires both sum and count for accuracy
- Integer overflow considerations become important with large trees
- Level boundaries are crucial for maintaining calculation integrity

**Mathematical Guarantee:** The average of a level equals the sum of all node values at that level divided by the count of nodes at that level.

**Note:** Solution 1 is recommended because it directly matches the problem structure with BFS level processing, provides immediate average calculation, and is the most intuitive approach for level-based statistics problems.
