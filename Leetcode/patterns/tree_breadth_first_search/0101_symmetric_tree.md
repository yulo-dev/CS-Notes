# Leetcode 101 - Symmetric Tree

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, check whether it is a mirror of itself (symmetric around its center). A tree is symmetric if the left subtree is a mirror reflection of the right subtree.

**Key Clarification Questions to Ask Interviewer:**
1. "Should I return true for an empty tree (null root)?"
2. "For symmetric comparison, do I need to check both structure and values, or just structure?"
3. "Are there performance preferences between recursive and iterative approaches for this problem?"
4. "Should I optimize for space complexity or code clarity?"

**Match:** This is a tree structural comparison problem using the Two-Tree Comparison Pattern.

"When I see 'symmetric tree', I recognize this as a structural comparison problem where I need to compare two subtrees simultaneously in mirror fashion. This isn't a traversal problem where I collect values - it's about comparing tree shapes and values in a specific pattern.

The Two-Tree Comparison Pattern is perfect here because:
- I need to compare nodes at symmetric positions
- The problem naturally decomposes into smaller mirror comparison subproblems
- Each comparison involves two nodes that must be checked simultaneously
- Recursive structure matches the tree structure perfectly

My plan is to use DFS recursion to compare the left and right subtrees of the root, but with a twist - when I go left in one subtree, I go right in the other subtree to maintain the mirror relationship."

**Plan:**
1. Handle null root edge case (empty tree is symmetric)
2. Compare root's left subtree with root's right subtree using mirror logic
3. For mirror comparison: check if current nodes have equal values
4. Recursively compare left.left with right.right (outer positions)
5. Recursively compare left.right with right.left (inner positions)
6. Return true only if all comparisons pass

**Implement:** See the code section below.

**Review:**
- Edge case: Empty tree is symmetric by definition
- Edge case: Single node tree is symmetric
- Mirror logic: Outer and inner positions must match correctly
- Base cases: Handle null node pairs properly

**Evaluate:**
- Time: O(n) - Visit each node once in comparison process
- Space: O(h) - Recursion stack depth equals tree height

## ☀️ Why This Is a Tree Structural Comparison Problem

Symmetric tree checking is fundamentally about comparing tree structures, not about traversal patterns. We need to verify that two subtrees are mirror images of each other, which requires simultaneous comparison of corresponding positions.

Key insights:
- Problem requires comparing two subtrees with mirror relationship
- Symmetric positions: left.left ↔ right.right, left.right ↔ right.left
- Each comparison is independent and can be decomposed recursively
- Success depends on all symmetric positions having matching values and structures

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `null` | Empty tree | `true` |
| `TreeNode(1)` | Single node | `true` |
| `[1,2,2,3,4,4,3]` | Perfect symmetric tree | `true` |
| `[1,2,2,null,3,null,3]` | Asymmetric structure | `false` |

These test:
- Null input boundary condition
- Trivial symmetric case
- Standard multi-level symmetric structure
- Asymmetric structure with same values but wrong positions

## ☀️ Code

### Solution 1: BFS with Pair Queue 

**Time: O(n) → Visit each node once to check mirror relationship**
**Space: O(n) → Queue stores node pairs, up to O(w) pairs where w is max width**

```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    # Iterative BFS approach - using queue to simulate recursion
    if not root:
        return True
    
    queue = deque([(root.left, root.right)])
    
    while queue:
        left, right = queue.popleft()
        
        # Both nodes are null - continue to next pair
        if not left and not right:
            continue
            
        # One node is null, other is not - not symmetric
        if not left or not right:
            return False
            
        # Values don't match - not symmetric
        if left.val != right.val:
            return False
        
        # Add symmetric pairs for next iteration
        queue.append((left.left, right.right))    # Outer pair
        queue.append((left.right, right.left))    # Inner pair
    
    return True
```

### Solution 2: DFS with Two-Tree Comparison Pattern (Classic Solution)

**Time: O(n) → Visit each node once in recursive calls**
**Space: O(h) → Recursion stack depth equals height of tree (O(log n) to O(n))**

```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    # Two-Tree Comparison Pattern using DFS recursion
    if not root:
        return True

    def isMirror(t1, t2):
        # Base case: both nodes are null - symmetric
        if not t1 and not t2:
            return True
        
        # Base case: one null, one non-null - not symmetric
        if not t1 or not t2:
            return False
        
        # Recursive case: current values equal AND subtrees are mirror
        return (t1.val == t2.val and
                isMirror(t1.left, t2.right) and  # Outer symmetry
                isMirror(t1.right, t2.left))     # Inner symmetry

    return isMirror(root.left, root.right)
```

### Solution 3: Level-by-Level Palindrome Check (Advanced Solution)

**Time: O(n) → Visit each node once, compare level by level**
**Space: O(n) → Store maximum width of tree level (up to n/2 nodes)**

```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    # Level-by-level comparison approach
    if not root:
        return True
    
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_values = []
        next_level = []
        
        # Collect current level values and nodes
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val if node else None)
            
            if node:
                next_level.append(node.left)
                next_level.append(node.right)
        
        # Check if current level is palindrome
        if level_values != level_values[::-1]:
            return False
        
        # Add next level nodes to queue if any non-null exist
        if any(node for node in next_level):
            queue.extend(next_level)
    
    return True
```

## ☀️ Notes

**Key Algorithm Components:**
- Two-Tree Comparison Pattern for structural comparison
- Mirror relationship logic (left.left ↔ right.right, left.right ↔ right.left)
- Base case handling for null node combinations

**Critical Insight:**
This problem demonstrates the Two-Tree Comparison Pattern, where we simultaneously traverse two subtrees with different rules. The key insight is recognizing this as a structural comparison rather than a traversal problem.

## ☀️ Coding Walkthrough Script

"I recognize this as a tree structural comparison problem. I need to check if the left and right subtrees of the root are mirror images of each other. This suggests using the Two-Tree Comparison Pattern.

I'll create a helper function that compares two nodes in mirror fashion. The base cases are: if both nodes are null, they're symmetric; if one is null and one isn't, they're not symmetric. For the recursive case, the nodes must have equal values AND their subtrees must be mirrors - specifically, the left node's left child should mirror the right node's right child, and the left node's right child should mirror the right node's left child.

For time complexity, I visit each node exactly once during the comparison process, giving me O(n). For space complexity, I'm using recursion, so the space is determined by the recursion stack depth, which equals the height of the tree. In a balanced tree this is O(log n), and in a skewed tree it's O(n), so worst case is O(h) where h can be up to n.

The recursive approach is natural because tree symmetry can be decomposed into smaller mirror comparison problems, which is exactly what the Two-Tree Comparison Pattern handles elegantly."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| BFS Pair Queue | O(n) | O(n) | Iterative mirror comparison | Queue-based approach |
| DFS Recursion | O(n) | O(h) | Two-Tree Comparison Pattern | **Recommended** |
| Level Palindrome | O(n) | O(n) | Level-by-level symmetry check | Alternative perspective |

## ☀️ Tree Structural Comparison Insights

- Symmetric tree problems use simultaneous dual-tree traversal
- Two-Tree Comparison Pattern is the standard template for structural comparisons
- Mirror relationships require careful coordination of left/right child access
- Recursive decomposition naturally matches tree structure hierarchy

**Mathematical Guarantee:** Two trees are mirror images if and only if corresponding nodes at mirror positions have equal values and their subtrees are also mirror images.
