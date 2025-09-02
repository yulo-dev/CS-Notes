# Leetcode 572 - Subtree of Another Tree

## ☀️ UMPIRE

**Understand:** Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot. A subtree includes a node and all of its descendants.

**Key Clarification Questions to Ask Interviewer:**
1. "Should I consider the entire subRoot as a unit, or could it be split across different branches of root?"
2. "Is it acceptable to use string serialization, or do you prefer tree traversal approaches?"
3. "Are there constraints on tree size that would affect the approach choice between BFS and DFS?"
4. "Should I optimize for the case where subRoot appears early in the traversal, or focus on worst-case performance?"

**Match:** This is a tree traversal problem combined with tree structure comparison, requiring the Two-Tree Comparison Pattern.

"When I see 'subtree with same structure and values', I recognize this as a combination of tree traversal and tree comparison. I need to find every possible starting node in the main tree, then check if the subtree rooted at that node exactly matches the target subtree.

This suggests using a two-phase approach: first traverse all nodes in the main tree, then for each candidate node, use the Two-Tree Comparison Pattern to check if it matches the target subtree exactly.

I can solve this with either BFS or DFS for the outer traversal. DFS is more natural because subtree checking is inherently recursive, and I can leverage the same recursive pattern for both the traversal and comparison phases."

**Plan:**
1. Handle edge cases: empty subRoot returns true, empty root with non-empty subRoot returns false
2. Traverse every node in root as potential subtree starting points
3. For each node, check if it forms an identical subtree to subRoot using Two-Tree Comparison Pattern
4. Return true as soon as a match is found, false if no matches exist

**Implement:** See the code section below.

**Review:**
- Edge case: Empty subRoot should return true (any tree contains empty subtree)
- Edge case: Empty root with non-empty subRoot should return false
- Identical match: Structure and values must match exactly, not just similar
- Efficiency: Early termination when match is found

**Evaluate:**
- Time: O(m * n) - For each of m nodes, potentially compare with n nodes
- Space: BFS O(m + n), DFS O(h) where h is tree height

## ☀️ Why This Is a Tree Traversal + Comparison Problem

Subtree detection requires two distinct operations: finding candidate starting points and verifying exact matches. This naturally combines tree traversal techniques with the Two-Tree Comparison Pattern.

Key insights:
- Every node in the main tree is a potential subtree root
- Subtree matching requires exact structural and value correspondence
- Two-Tree Comparison Pattern provides the verification mechanism
- Choice between BFS/DFS affects space complexity but not time complexity

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root=null, subRoot=any` | Empty main tree | `false` |
| `root=any, subRoot=null` | Empty subtree | `true` |
| `root=[3,4,5,1,2], subRoot=[4,1,2]` | Exact subtree match | `true` |
| `root=[3,4,5,1,2,null,null,null,null,0], subRoot=[4,1,2]` | Extra nodes in main tree | `false` |

These test:
- Null input boundary conditions
- Standard subtree detection
- False positive prevention (extra nodes break exact match)

## ☀️ Code

### Solution 1: BFS Traversal with BFS Comparison (Alternative Solution)

**Time: O(m * n) → For each of m nodes in root, potentially compare with n nodes in subRoot**
**Space: O(W(root) + W(subRoot)) → O(m + n) worst case, outer and inner BFS queues combined**

```python
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # BFS approach - check each node in root as potential subtree match
    if not subRoot:
        return True
    if not root:
        return False

    def same_bfs(a, b):
        # BFS comparison of two trees for identical structure and values
        q = deque([(a, b)])
        while q:
            x, y = q.popleft()
            if not x and not y:  # Both null - continue
                continue
            if not x or not y:   # One null, one not - not same
                return False
            if x.val != y.val:   # Different values - not same
                return False
            q.append((x.left, y.left))
            q.append((x.right, y.right))
        return True

    # Outer BFS: scan all nodes in root
    q = deque([root])
    target = subRoot.val
    while q:
        node = q.popleft()
        # Only check nodes with matching root value for efficiency
        if node.val == target and same_bfs(node, subRoot):
            return True
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return False
```

### Solution 2: DFS Traversal with Two-Tree Comparison (Classic Solution)

**Time: O(m * n) → For each of m nodes in root, potentially compare with n nodes in subRoot**
**Space: O(H(root) + H(subRoot)) → O(m + n) worst case, recursion stack for both functions**

```python
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # DFS recursive approach - natural tree traversal with same tree check
    if not subRoot:
        return True
    if not root:
        return False
    if self.same(root, subRoot):
        return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

def same(self, a, b):
    # Two-Tree Comparison Pattern for identical tree check
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a.val != b.val:
        return False
    return self.same(a.left, b.left) and self.same(a.right, b.right)
```

### Solution 3: String Serialization Matching (Advanced Solution)

**Time: O(m + n) if using KMP for substring search → O(m * n) worst case for naive substring search**
**Space: O(m + n) → Store serialized strings for both trees**

```python
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # String serialization approach - convert trees to strings and use substring matching
    def serialize(node):
        if not node:
            return "null"
        return f"#{node.val}#,{serialize(node.left)},{serialize(node.right)}"
    
    root_str = serialize(root)
    sub_str = serialize(subRoot)
    
    return sub_str in root_str
```

## ☀️ Notes

**Key Algorithm Components:**
- Tree traversal to find candidate starting points
- Two-Tree Comparison Pattern for exact structure verification
- Early optimization by checking root value before full comparison

**Critical Insight:**
This problem demonstrates the power of combining traversal patterns with comparison patterns. The key is recognizing that subtree detection = traversal + Two-Tree Comparison Pattern.

## ☀️ Coding Walkthrough Script

"I need to determine if subRoot appears as an exact subtree anywhere within root. This requires two operations: finding potential starting points and verifying exact matches.

My approach uses DFS to traverse every node in the main tree as a potential subtree root. For each candidate node, I use the Two-Tree Comparison Pattern to check if the subtree rooted at that node exactly matches the target subtree.

For time complexity, in the worst case I might check every node in the main tree (m nodes) and for each check, compare against every node in the subtree (n nodes), giving me O(m * n). For space complexity, I'm using recursion for both the traversal and comparison functions. The maximum recursion depth is the sum of the heights of both trees, giving me O(H(root) + H(subRoot)), which can be O(m + n) in the worst case of completely unbalanced trees.

The key optimization is that I only perform the expensive Two-Tree Comparison when the root values match, which helps in many practical cases. The recursive DFS approach is preferred because it naturally matches the problem structure and uses the proven Two-Tree Comparison Pattern."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| BFS + BFS Comparison | O(m * n) | O(W(root) + W(subRoot)) | Level-by-level with queue comparison | Alternative approach |
| DFS + Two-Tree Comparison | O(m * n) | O(H(root) + H(subRoot)) | Natural recursive pattern | **Recommended** |
| String Serialization | O(m + n) to O(m * n) | O(m + n) | Creative string matching approach | Depends on substring algorithm |

## ☀️ Tree Traversal + Comparison Insights

- Subtree problems often combine traversal with structure verification
- Two-Tree Comparison Pattern is essential for exact tree matching
- Early termination optimizations can significantly improve average case performance
- Choice of traversal method (BFS/DFS) affects space complexity but not time complexity asymptotically

**Mathematical Guarantee:** A subtree match requires identical structure and values at every corresponding position, which the Two-Tree Comparison Pattern verifies systematically.

**Note:** Solution 2 is recommended because it uses natural recursive patterns, clearly separates traversal from comparison logic, and demonstrates mastery of the Two-Tree Comparison Pattern.
