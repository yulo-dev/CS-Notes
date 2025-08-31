# Leetcode 104 - Maximum Depth of Binary Tree

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Key Clarification Questions to Ask Interviewer:**
1. "Should I return 0 for an empty tree (null root)?"
2. "Could the tree be highly skewed or very deep? If so I'll avoid recursion and use BFS."
3. "Do you prefer a recursive DFS or an iterative approach?"
4. "Is O(h) space complexity acceptable for recursion, where h is the tree height?"

**Match:** This is a classic tree depth problem that naturally maps to recursive DFS, though BFS level counting is also viable.

"When I see 'maximum depth', I immediately think of recursive DFS because tree depth has a natural recursive definition: the depth of a tree is 1 plus the maximum depth of its subtrees. This recursive structure makes DFS the most elegant solution.

DFS is optimal here because:
- The problem has a natural recursive decomposition
- Maximum depth = 1 + max(left_depth, right_depth)
- Space complexity is O(h) rather than O(w) for BFS
- Code is concise and matches the mathematical definition

My plan is to use recursive DFS where I compute the maximum depth of left and right subtrees, then return 1 plus the larger of the two. This directly implements the recursive definition of tree height."

**Plan:**
1. Handle null root base case by returning 0
2. Recursively calculate maximum depth of left subtree
3. Recursively calculate maximum depth of right subtree
4. Return 1 plus the maximum of the two subtree depths
5. Recursion naturally handles the tree traversal

**Implement:** See the code section below.

**Review:**
- Edge case: Empty tree returns 0
- Edge case: Single node returns 1
- Recursion base case: Null nodes contribute 0 to depth
- Mathematical correctness: 1 + max(left, right) gives correct depth

**Evaluate:**
- Time: O(n) - Visit each node exactly once
- Space: O(h) → O(n) worst case, where h is height of tree

## ☀️ Why This Is a Tree Depth/Height Problem

Maximum depth is fundamentally about measuring tree height, which has a natural recursive definition. The depth of any tree equals 1 (for the current node) plus the maximum depth of its subtrees. This recursive structure makes DFS the most natural approach.

Key insights:
- Tree depth follows recursive structure: depth(tree) = 1 + max(depth(left), depth(right))
- Each recursive call reduces the problem size by exploring subtrees
- Base case naturally occurs at null nodes (depth 0)
- No need to track levels explicitly - recursion handles the depth calculation

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `null` | Empty tree | `0` |
| `TreeNode(1)` | Single node | `1` |
| `[3,9,20,null,null,15,7]` | Balanced tree | `3` |
| `[1,2,null,3,null,4]` | Skewed tree | `4` |

These test:
- Null input boundary condition
- Minimum valid tree depth
- Standard balanced tree depth calculation
- Deep skewed tree handling (recursion depth consideration)

## ☀️ Code

### Solution 1: BFS Level-by-Level Counting (Brute Force)

**Time: O(n) → Visit each node once in level order traversal**
**Space: O(w) → O(n) worst case, where w is max width of tree level**

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    # BFS level-by-level approach - count levels until no more nodes
    if not root:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        depth += 1

    return depth
```

### Solution 2: BFS with Node-Depth Tracking (Alternative Solution)

**Time: O(n) → Visit each node once with depth tracking**
**Space: O(w) → O(n) worst case, where w is max width of tree level**

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    # BFS with (node, depth) pairs - track depth with each node
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    max_depth = 0
    
    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        
        # Add children with incremented depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_depth
```

### Solution 3: DFS Recursive Approach (Classic Solution)

**Time: O(n) → Visit each node once in recursive calls**
**Space: O(h) → O(n) worst case, where h is height of tree (balanced O(log n), skewed O(n))**

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    # DFS recursive approach - natural tree depth calculation
    if not root:
        return 0
    
    # Maximum depth is 1 + max depth of subtrees
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)
    
    return 1 + max(left_depth, right_depth)
```

## ☀️ Notes

**Key Algorithm Components:**
- Recursive decomposition of tree depth calculation
- Base case handling for null nodes
- Maximum operation to select deeper subtree

**Critical Insight:**
Maximum depth problems have natural recursive solutions because tree height follows a recursive definition. The elegance of the recursive solution makes it preferable to iterative approaches for this specific problem.

## ☀️ Coding Walkthrough Script

"I need to find the maximum depth of the binary tree. This problem has a natural recursive structure: the depth of any tree equals 1 plus the maximum depth of its subtrees.

I'll use recursive DFS where my base case is a null node returning 0. For any non-null node, I recursively calculate the maximum depth of both the left and right subtrees, then return 1 plus the larger of these two values.

For time complexity, I visit each node exactly once during the recursive traversal, giving me O(n). For space complexity, I'm using recursion, so the space is determined by the recursion stack depth, which equals the height of the tree. In a balanced tree this is O(log n), and in a completely skewed tree it's O(n), so worst case space complexity is O(h) where h can be up to n.

The recursive approach is preferred here because it directly implements the mathematical definition of tree height and results in very clean, intuitive code."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| BFS Level Count | O(n) | O(w) → O(n) | Count levels iteratively | Clear but more complex |
| BFS Depth Track | O(n) | O(w) → O(n) | Track depth per node | Alternative BFS approach |
| DFS Recursive | O(n) | O(h) → O(n) | Natural recursive definition | **Recommended** |

## ☀️ Tree Depth Calculation Insights

- Maximum depth problems naturally favor recursive solutions
- Tree height has elegant recursive definition: height = 1 + max(left_height, right_height)
- Recursive approach often has better space complexity for balanced trees
- Mathematical simplicity of recursive solution makes it interview-preferred

**Mathematical Guarantee:** The maximum depth of a binary tree equals 1 plus the maximum depth of its deepest subtree.

**Note:** Solution 3 is recommended because it directly implements the recursive definition of tree height, has optimal space complexity for balanced trees O(log n), and produces the most elegant and intuitive code.
