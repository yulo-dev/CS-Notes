# Leetcode 100 - Same Tree

## ☀️ UMPIRE

**Understand:** Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

**Key Clarification Questions to Ask Interviewer:**
1. "Should I return true if both trees are null (empty)?"
2. "Do I need to check both structure and values, or is structural similarity sufficient?"
3. "Are there any constraints on the tree size or node values I should consider?"
4. "Is there a preference between recursive and iterative solutions for this problem?"

**Match:** This is a tree structural comparison problem using the Two-Tree Comparison Pattern.

"When I see 'check if two trees are the same', I immediately recognize this as the fundamental Two-Tree Comparison Pattern. Unlike traversal problems where I collect or process values, this is about comparing two tree structures simultaneously at corresponding positions.

The Two-Tree Comparison Pattern is perfect for this problem because:
- I need to compare nodes at exactly the same positions in both trees
- The problem naturally decomposes into smaller subproblems (compare subtrees)
- Each comparison involves two nodes that must be checked simultaneously
- The recursive structure directly mirrors the tree structure

My plan is to use DFS recursion to compare corresponding nodes, where I compare p's left subtree with q's left subtree, and p's right subtree with q's right subtree. This maintains the exact positional correspondence needed."

**Plan:**
1. Handle base cases where one or both trees are null
2. Compare current node values of p and q
3. If values match, recursively compare left subtrees
4. If left subtrees match, recursively compare right subtrees
5. Return true only if all comparisons pass

**Implement:** See the code section below.

**Review:**
- Edge case: Both trees null should return true
- Edge case: One tree null, other non-null should return false
- Value comparison: Nodes at same position must have equal values
- Structure comparison: Subtree structures must be identical

**Evaluate:**
- Time: O(n) - Visit each node once for comparison
- Space: O(h) - Recursion stack depth equals tree height

## ☀️ Why This Is a Tree Structural Comparison Problem

Same tree checking is the archetypal example of tree structural comparison. We need to verify that two trees have identical structure and identical values at corresponding positions. This requires simultaneous traversal of both trees with exact position matching.

Key insights:
- Problem requires comparing two trees with direct position correspondence
- Each node in tree p must match the corresponding node in tree q
- Corresponding positions: p.left ↔ q.left, p.right ↔ q.right
- Success depends on all corresponding positions having matching values and structures

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `null, null` | Both trees empty | `true` |
| `TreeNode(1), null` | One empty, one non-empty | `false` |
| `[1,2,3], [1,2,3]` | Identical trees | `true` |
| `[1,2], [1,null,2]` | Same values, different structure | `false` |

These test:
- Both null boundary condition
- Asymmetric null cases
- Perfect structural and value match
- Structure difference with same node values

## ☀️ Code

### Solution 1: BFS with Pair Queue (Brute Force)

**Time: O(n) → Visit each node once to compare with corresponding node**
**Space: O(w) → O(n) worst case, where w is max width of tree level**

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Iterative BFS approach using queue to store node pairs
    queue = deque([(p, q)])
    
    while queue:
        n1, n2 = queue.popleft()
        
        # Both nodes are null - continue to next pair
        if not n1 and not n2:
            continue
            
        # One node is null, other is not - trees are different
        if not n1 or not n2:
            return False
            
        # Values don't match - trees are different
        if n1.val != n2.val:
            return False
        
        # Add corresponding child pairs for next iteration
        queue.append((n1.left, n2.left))      # Left children
        queue.append((n1.right, n2.right))    # Right children
    
    return True
```

### Solution 2: DFS with Two-Tree Comparison Pattern (Classic Solution)

**Time: O(n) → Visit each node once in recursive calls**
**Space: O(h) → O(n) worst case, where h is height of tree (balanced O(log n), skewed O(n))**

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Two-Tree Comparison Pattern using DFS recursion
    # Base case: both are null
    if not p and not q:
        return True
    
    # One is null, the other is not
    if not p or not q:
        return False
    
    # Both exist: compare value, then recurse on children
    if p.val != q.val:
        return False
        
    return (self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right))
```

### Solution 3: DFS with Helper Function (Advanced Solution)

**Time: O(n) → Visit each node once using preorder traversal**
**Space: O(h) → O(n) worst case, where h is recursion stack depth**

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Alternative DFS approach with explicit value comparison first
    def dfs(node1, node2):
        # Base cases
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        
        # Compare current nodes and recurse
        return (node1.val == node2.val and
                dfs(node1.left, node2.left) and
                dfs(node1.right, node2.right))
    
    return dfs(p, q)
```

## ☀️ Notes

**Key Algorithm Components:**
- Two-Tree Comparison Pattern for exact position matching
- Base case handling for null node combinations
- Value equality checking at corresponding positions

**Critical Insight:**
This is the fundamental example of the Two-Tree Comparison Pattern. Unlike LeetCode 101 which uses mirror positions, this problem uses direct position correspondence, making it the simpler and more intuitive version of the pattern.

## ☀️ Coding Walkthrough Script

"I recognize this as the classic Two-Tree Comparison problem. I need to check if two trees have identical structure and values at corresponding positions. This is a perfect case for DFS recursion using the Two-Tree Comparison Pattern.

My approach has three main cases: First, if both nodes are null, they match. Second, if one is null and the other isn't, they don't match. Third, if both exist, I need to check that their values are equal AND that their left subtrees are identical AND their right subtrees are identical.

For time complexity, I visit each node exactly once during the comparison process, giving me O(n) where n is the number of nodes. For space complexity, I'm using recursion, so the space is determined by the recursion stack depth, which equals the height of the tree. This gives me O(h) space complexity, where h ranges from O(log n) in a balanced tree to O(n) in a skewed tree, so worst case space complexity is O(n).

The recursive approach is natural because tree equality can be decomposed into smaller subproblems - if the current nodes match and both subtrees match, then the entire trees match."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| BFS Pair Queue | O(n) | O(n) | Iterative position comparison | Queue-based approach |
| DFS Recursion | O(n) | O(h) | Two-Tree Comparison Pattern | **Recommended** |
| DFS Helper | O(n) | O(h) | Explicit helper function | Clean organization |

## ☀️ Tree Structural Comparison Insights

- Same tree problems are the foundation of Two-Tree Comparison Pattern
- Direct position correspondence (left-left, right-right) is simpler than mirror correspondence
- Two-Tree Comparison Pattern applies to many tree problems (Same Tree, Symmetric Tree, etc.)
- Base case handling is crucial for correctness

**Mathematical Guarantee:** Two trees are identical if and only if corresponding nodes at the same positions have equal values and their subtrees are also identical.

**Note:** Solution 2 is recommended for interviews because it demonstrates the classic Two-Tree Comparison Pattern clearly, has optimal space complexity O(h), and is the most intuitive approach for this fundamental tree comparison problem.
