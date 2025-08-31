# LeetCode 100: Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same

from typing import Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) → Visit each node once to compare with corresponding node
# Space: O(w) → O(n) worst case, where w is max width of tree level
class Solution:
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

# Time: O(n) → Visit each node once in recursive calls
# Space: O(h) → O(n) worst case, where h is height of tree (balanced O(log n), skewed O(n))

class Solution2:
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

# Time: O(n) → Visit each node once using preorder traversal
# Space: O(h) → O(n) worst case, where h is recursion stack depth
class Solution3:
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

# Test function
def test_solutions():
    # Create test case: [1,2,3] and [1,2,3] - same trees
    # Expected: True
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)
    
    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"BFS Queue: {sol1.isSameTree(p1, q1)}")       # Expected: True
    print(f"DFS Recursion: {sol2.isSameTree(p1, q1)}")   # Expected: True
    print(f"DFS Helper: {sol3.isSameTree(p1, q1)}")      # Expected: True
    
    # Test different trees: [1,2] and [1,null,2]
    # Expected: False
    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    
    q2 = TreeNode(1)
    q2.right = TreeNode(2)
    
    print(f"Different structure - BFS: {sol1.isSameTree(p2, q2)}")       # Expected: False
    print(f"Different structure - DFS: {sol2.isSameTree(p2, q2)}")       # Expected: False
    print(f"Different structure - Helper: {sol3.isSameTree(p2, q2)}")    # Expected: False
    
    # Test different values: [1,2,1] and [1,1,2]
    # Expected: False
    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)
    
    q3 = TreeNode(1)
    q3.left = TreeNode(1)
    q3.right = TreeNode(2)
    
    print(f"Different values - DFS: {sol2.isSameTree(p3, q3)}")          # Expected: False
    
    # Test edge cases
    print(f"Both null - DFS: {sol2.isSameTree(None, None)}")             # Expected: True
    print(f"One null - DFS: {sol2.isSameTree(TreeNode(1), None)}")       # Expected: False

# Strategy:
# 1. Start with Solution 1 (BFS queue approach) 
# 2. Optimize to Solution 2 (DFS recursion) 
# 3. If time permits, mention Solution 3 (DFS with helper) 
#
# Key insight: Same tree comparison uses Two-Tree Comparison Pattern with direct position mapping
