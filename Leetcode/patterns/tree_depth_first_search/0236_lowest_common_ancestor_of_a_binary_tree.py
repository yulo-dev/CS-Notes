# LeetCode 236: Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined 
# between two nodes p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself)."

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Brute Force - Store Paths and Find Divergence Point
# Time: O(n) → Visit each node to find paths, then compare paths
# Space: O(n) → Store complete paths from root to target nodes
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

# Solution 2: Recursive DFS - Bottom-up Approach (Classic Interview Solution)
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Recursion stack depth equals tree height
# ★ This is the classic interview solution ★
class Solution2:
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

# Solution 3: Advanced - Iterative with Parent Pointers
# Time: O(n) → Visit nodes to build parent map and traverse ancestors
# Space: O(n) → Store parent pointers and ancestor set
class Solution3:
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

# Test function
def test_solutions():
    # Create test tree:       3
    #                       /   \
    #                      5     1
    #                     / \   / \
    #                    6   2 0   8
    #                       / \
    #                      7   4
    
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    # Get node references for testing
    node_5 = root.left
    node_1 = root.right
    node_4 = root.left.right.right
    node_6 = root.left.left
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    # Test case 1: LCA(5, 1) should be 3
    result1 = sol1.lowestCommonAncestor(root, node_5, node_1)
    result2 = sol2.lowestCommonAncestor(root, node_5, node_1)
    result3 = sol3.lowestCommonAncestor(root, node_5, node_1)
    
    print(f"LCA(5, 1): Brute Force={result1.val}, Recursive={result2.val}, Iterative={result3.val}")
    
    # Test case 2: LCA(5, 4) should be 5
    result1 = sol1.lowestCommonAncestor(root, node_5, node_4)
    result2 = sol2.lowestCommonAncestor(root, node_5, node_4)
    result3 = sol3.lowestCommonAncestor(root, node_5, node_4)
    
    print(f"LCA(5, 4): Brute Force={result1.val}, Recursive={result2.val}, Iterative={result3.val}")
    
    # Test case 3: LCA(6, 4) should be 5
    result2 = sol2.lowestCommonAncestor(root, node_6, node_4)
    print(f"LCA(6, 4): {result2.val}")  # Expected: 5

# Strategy:
# 1. Start with Solution 1 (Brute Force)
# 2. Optimize to Solution 2 (Recursive DFS) 
# 3. If time permits, mention Solution 3 (Parent Pointers) as alternative approach
#
# Key insight: LCA is the first node encountered where p and q diverge into different subtrees
# Why Solution 2 is preferred:
# - Elegant recursive solution that directly implements LCA definition
# - Single pass through the tree with optimal time complexity
# - Clean logic: if both subtrees return non-null, current node is LCA
# - Natural divide-and-conquer approach that's easy to explain
# - Handles edge cases naturally (node being ancestor of itself)
