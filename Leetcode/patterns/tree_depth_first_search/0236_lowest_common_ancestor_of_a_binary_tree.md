# Leetcode 0236 - Lowest Common Ancestor of a Binary Tree

## ☀️ UMPIRE

**Understand:** Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. The LCA is defined as the lowest node in the tree that has both nodes as descendants (where we allow a node to be a descendant of itself).

**Match:** This is a Tree Traversal problem using DFS (Depth-First Search) with a bottom-up approach. The key insight is that the LCA is the first node we encounter (when traversing bottom-up) where the two target nodes diverge into different subtrees, or where one target node is an ancestor of the other.

**Plan:**
1. Use post-order DFS traversal (process children before parent)
2. For each node, check if it's one of the target nodes
3. Recursively search left and right subtrees
4. If both subtrees return non-null, current node is LCA
5. Otherwise, return whichever subtree found a target node

**Implement:** See the code section below.

**Review:**
- Ensure we handle the case where one node is ancestor of another
- Verify that we return the correct node when both targets are found
- Check edge cases like target nodes being the root or leaf nodes
- Confirm that we traverse the tree efficiently in a single pass

**Evaluate:**
- Time: O(n) - visit each node at most once
- Space: O(h) where h is tree height - recursion stack depth

## ☀️ Why This Is a Tree DFS Bottom-Up Problem

LCA requires understanding the relationship between nodes across different levels:
- **Bottom-up approach is natural** because LCA is determined by what we find in subtrees
- **Post-order traversal pattern** (children first, then parent) fits the logic perfectly
- **Divide and conquer strategy** where each subtree's result informs the parent's decision
- **Single pass efficiency** by combining search and LCA determination

Key insights:
- We need information from both subtrees before making a decision about current node
- The moment both subtrees return non-null results, we've found our LCA
- Post-order traversal ensures we have all necessary information when processing each node
- The recursive structure naturally handles the "lowest" requirement of LCA

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1` | Nodes in different subtrees | `3` |
| `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4` | One node is ancestor of other | `5` |
| `root = [1,2], p = 1, q = 2` | Root and child | `1` |
| `root = [2,1], p = 2, q = 1` | Root and child (left) | `2` |
| `root = [1], p = 1, q = 1` | Same node | `1` |

These test:
- Standard LCA cases where nodes are in different subtrees
- Cases where one node is ancestor of another
- Root being one of the target nodes
- Single node tree edge case
- Various tree structures and positions

## ☀️ Code

### Solution 1: Brute Force - Find Paths and Compare (Brute Force)
**Time: O(n) → Visit each node to find paths, then compare paths**  
**Space: O(n) → Store complete paths from root to target nodes**

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(node, target, path):
            """Find path from root to target node"""
            if not node:
                return False
            
            # Add current node to path
            path.append(node)
            
            # Check if current node is the target
            if node == target:
                return True
            
            # Search in left and right subtrees
            if (find_path(node.left, target, path) or 
                find_path(node.right, target, path)):
                return True
            
            # If target not found in this subtree, backtrack
            path.pop()
            return False
        
        # Find paths to both nodes
        path_p = []
        path_q = []
        
        find_path(root, p, path_p)
        find_path(root, q, path_q)
        
        # Find the last common node in both paths
        lca = None
        min_len = min(len(path_p), len(path_q))
        
        for i in range(min_len):
            if path_p[i] == path_q[i]:
                lca = path_p[i]
            else:
                break
        
        return lca
```

### Solution 2: Recursive DFS Bottom-Up (Classic Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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

### Solution 3: Iterative with Parent Pointers (Advanced Solution)
**Time: O(n) → Visit nodes to build parent map and traverse ancestors**  
**Space: O(n) → Store parent pointers and ancestor set**

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Build parent pointer map using BFS/DFS
        parent = {root: None}
        stack = [root]
        
        # Continue until both p and q are found
        while p not in parent or q not in parent:
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        # Collect all ancestors of p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        
        # Find first common ancestor by traversing q's ancestors
        while q not in ancestors:
            q = parent[q]
        
        return q
```

## ☀️ Notes

**Key Algorithm Components:**
- Base case handling: return node if it's null or one of the targets
- Recursive search in both subtrees to gather information
- Decision logic: if both subtrees return non-null, current node is LCA
- Propagation: return found node up the recursion chain

**Critical Insight:**
The elegant recursive solution works because of the post-order nature of the logic. We first gather information from children (what did left and right subtrees find?), then make a decision about the current node. This bottom-up approach naturally identifies the lowest common ancestor.

## ☀️ Coding Walkthrough Script

I'll solve this using a recursive bottom-up approach that leverages the definition of LCA.
The base case is straightforward: if the current node is null or matches either target node, I return it immediately.
For each node, I recursively search both left and right subtrees to see what they return. Each recursive call returns either null (target not found in that subtree) or a node (either a target node or the LCA).
The key insight is in the decision logic: if both left and right subtrees return non-null values, it means I found one target in each subtree, making the current node their LCA.
If only one subtree returns a non-null value, I propagate that result upward, since it means either both targets are in that subtree (and the result is their LCA), or only one target is in that subtree (and the result is that target).
This approach is elegant because it handles all cases naturally: nodes in different subtrees, one node being ancestor of another, and even the case where both nodes are the same.
The time complexity is O(n) since I visit each node at most once, and space complexity is O(h) for the recursion stack.

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Path Finding | O(n) | O(n) | Store and compare complete paths | Simple but memory inefficient |
| Recursive Bottom-Up | O(n) | O(h) | Post-order decision making | **Recommended**; elegant and optimal |
| Parent Pointers | O(n) | O(n) | Build parent map, traverse ancestors | Good iterative alternative |

## ☀️ LCA Problem Insights

- **Bottom-up nature:** LCA is determined by information from subtrees
- **Post-order pattern:** Process children before making decision about parent  
- **Divide and conquer:** Each subtree solves a smaller version of the problem
- **Edge case handling:** One node being ancestor of another is handled naturally
- **Efficiency:** Single traversal combines search and LCA determination

**Mathematical Guarantee:** Since we use post-order traversal and the LCA is by definition the lowest node that has both targets as descendants, our bottom-up approach will encounter the LCA before any of its ancestors, ensuring we find the correct (lowest) result.
