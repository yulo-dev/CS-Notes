# Leetcode 0235 - Lowest Common Ancestor of a Binary Search Tree

## ☀️ UMPIRE

**Understand:** Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. The LCA is defined as the lowest node in the tree that has both nodes as descendants (where we allow a node to be a descendant of itself).

**Match:** This is a Tree Traversal problem that leverages BST properties using DFS (Depth-First Search). The key insight is that BST ordering allows us to determine which subtree contains the LCA without exploring both sides, making this more efficient than the generic binary tree LCA problem.

**Plan:**
1. Use BST property: left subtree < root < right subtree
2. Compare target node values with current node value
3. If both targets are smaller, search left subtree
4. If both targets are larger, search right subtree  
5. If targets are on different sides (or one equals current), current node is LCA

**Implement:** See the code section below.

**Review:**
- Ensure we leverage BST property for efficient search direction
- Verify that we handle cases where one node is ancestor of another
- Check that we don't unnecessarily explore both subtrees
- Confirm that we handle edge cases like equal values correctly

**Evaluate:**
- Time: O(h) - best case O(log n) for balanced BST, worst case O(n) for skewed
- Space: O(h) where h is tree height - recursion stack depth

## ☀️ Why This Is a BST Property Optimization Problem

BST structure provides additional information that generic binary trees lack:
- **Value ordering eliminates unnecessary searches** - we can determine search direction
- **Single path traversal** instead of exploring multiple subtrees
- **Natural split point identification** - when nodes diverge to different sides
- **Optimal for balanced trees** - logarithmic performance vs linear for generic trees

Key insights:
- Generic binary tree LCA requires exploring both subtrees potentially
- BST allows us to eliminate entire subtrees based on value comparisons
- The first node where p and q diverge to different sides is automatically the LCA
- No need to perform exhaustive search when tree structure provides guidance

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8` | Nodes in different subtrees | `6` |
| `root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4` | One node is ancestor of other | `2` |
| `root = [2,1,3], p = 1, q = 3` | Root is LCA | `2` |
| `root = [5,3,6,2,4], p = 2, q = 4` | LCA in subtree | `3` |
| `root = [1], p = 1, q = 1` | Same node | `1` |

These test:
- Standard BST LCA where nodes are in different subtrees  
- Cases where one node is direct ancestor of another
- Root being the LCA
- LCA located in subtrees rather than root
- Single node and identical node cases

## ☀️ Code

### Solution 1: Generic Binary Tree Approach (Brute Force)
**Time: O(n) → May visit all nodes ignoring BST property**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Use the same algorithm as generic binary tree LCA (ignoring BST property)"""
        # Base case: if current node is None, p, or q, return it
        if not root or root == p or root == q:
            return root
        
        # Search for p and q in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right return non-None, current node is LCA
        if left and right:
            return root
        
        # Otherwise, return whichever subtree found a target node
        return left if left else right
```

### Solution 2: BST Property Three-Way Decision (Classic Solution)
**Time: O(h) → Best case O(log n), worst case O(n) for skewed tree**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If both target nodes are smaller than the current node,
        # that means they must be in the left subtree.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If both target nodes are greater than the current node,
        # they must be in the right subtree.
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are on different sides of the current node (or one is equal to root),
        # then the current node is their lowest common ancestor.
        else:
            return root
```

### Solution 3: Iterative BST Approach (Advanced Solution)
**Time: O(h) → Best case O(log n), worst case O(n) for skewed tree**  
**Space: O(1) → No recursion, only constant extra space**

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        
        while current:
            # If both nodes are smaller, go left
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If both nodes are larger, go right
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # If nodes are on different sides or one equals current, found LCA
            else:
                return current
        
        return None  # Should never reach here for valid input
```

## ☀️ Notes

**Key Algorithm Components:**
- Three-way decision logic based on BST value comparisons
- Single-path traversal leveraging BST ordering property
- Natural handling of divergence points and ancestor relationships
- Elimination of unnecessary subtree exploration

**Critical Insight:**
The power of this BST-specific solution lies in its ability to make definitive decisions about search direction. Unlike generic binary trees where we must explore both subtrees, BST ordering tells us exactly which direction contains our answer, leading to optimal performance.

## ☀️ Coding Walkthrough Script

I'll solve this by leveraging the fundamental BST property: values in left subtree are smaller, values in right subtree are larger.
My approach uses a three-way decision structure. At each node, I compare both target values with the current node's value.
If both p and q are smaller than the current node, I know they must both be in the left subtree, so I recurse left.
If both p and q are larger than the current node, they must both be in the right subtree, so I recurse right.
The key insight is the else case: if p and q are on different sides of the current node, or if one of them equals the current node, then the current node is their LCA. This is because it's the first point where their paths diverge.
This approach is much more efficient than the generic binary tree LCA algorithm because I only traverse a single path from root to LCA, rather than potentially exploring multiple subtrees.
The time complexity is O(h) where h is the tree height, giving us O(log n) performance for balanced BSTs, which is a significant improvement over O(n) for generic approaches."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Generic Tree LCA | O(n) | O(h) | Explore both subtrees | Ignores BST property |
| BST Three-Way Decision | O(h) | O(h) | Value-based direction choice | **Recommended**; optimal for BST |
| BST Iterative | O(h) | O(1) | Iterative single-path traversal | Space-optimal alternative |

## ☀️ BST LCA Optimization Insights

- **BST advantage:** Value ordering provides search direction guidance
- **Single path efficiency:** No need to explore multiple subtrees simultaneously
- **Natural divergence detection:** First node where paths split is automatically LCA
- **Logarithmic performance:** O(log n) for balanced trees vs O(n) for generic approach
- **Three-way logic:** Both left, both right, or divergence point

**Mathematical Guarantee:** Since BST maintains the property that left < root < right, the first node encountered where p and q fall on different sides (or one equals the node) is mathematically guaranteed to be their lowest common ancestor.

**Note:** Solution 2 (BST Three-Way Decision) is the most recommended approach for interviews due to its optimal BST-specific performance, intuitive decision logic, and clean three-case structure. This solution perfectly demonstrates understanding of how to leverage data structure properties for algorithmic optimization. The three-way decision pattern (both left, both right, divergence) is natural and easy to explain during interviews.
