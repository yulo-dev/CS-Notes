# LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA: "The lowest common ancestor is defined between two nodes 
# p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself)."

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Brute Force - Use Generic Binary Tree LCA Algorithm
# Time: O(n) → May visit all nodes in worst case
# Space: O(h) → Recursion stack depth equals tree height
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

# Solution 2: Iterative BST Three-Way Decision (Classic Solution)
# Time: O(h) → Best case O(log n), worst case O(n) for skewed tree
# Space: O(1) → No recursion, only constant extra space

class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        
        while current:
            # If both target nodes are smaller than the current node,
            # that means they must be in the left subtree.
            if p.val < current.val and q.val < current.val:
                current = current.left
            
            # If both target nodes are greater than the current node,
            # they must be in the right subtree.
            elif p.val > current.val and q.val > current.val:
                current = current.right
            
            # If p and q are on different sides of the current node (or one is equal to current),
            # then the current node is their lowest common ancestor.
            else:
                return current
        
        return None  # Should never reach here for valid input

# Solution 3: Recursive BST Approach (Advanced Solution)
# Time: O(h) → Best case O(log n), worst case O(n) for skewed tree
# Space: O(h) → Recursion stack depth equals tree height
class Solution3:
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

# Alternative Solution 2: Using Range-Based Logic
class Solution2_Alternative:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Ensure p has smaller value than q for easier logic
        if p.val > q.val:
            p, q = q, p
        
        # Base case: if current node is between p and q (inclusive), it's the LCA
        if p.val <= root.val <= q.val:
            return root
        
        # If both nodes are smaller, LCA must be in left subtree
        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If both nodes are larger, LCA must be in right subtree
        return self.lowestCommonAncestor(root.right, p, q)

# Test function
def test_solutions():
    # Create test BST:      6
    #                     /   \
    #                    2     8
    #                   / \   / \
    #                  0   4 7   9
    #                     / \
    #                    3   5
    
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    
    # Get node references for testing
    node_2 = root.left
    node_8 = root.right
    node_4 = root.left.right
    node_0 = root.left.left
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    # Test case 1: LCA(2, 8) should be 6
    result1 = sol1.lowestCommonAncestor(root, node_2, node_8)
    result2 = sol2.lowestCommonAncestor(root, node_2, node_8)
    result3 = sol3.lowestCommonAncestor(root, node_2, node_8)
    
    print(f"LCA(2, 8): Brute Force={result1.val}, BST Recursive={result2.val}, BST Iterative={result3.val}")
    
    # Test case 2: LCA(2, 4) should be 2
    result1 = sol1.lowestCommonAncestor(root, node_2, node_4)
    result2 = sol2.lowestCommonAncestor(root, node_2, node_4)
    result3 = sol3.lowestCommonAncestor(root, node_2, node_4)
    
    print(f"LCA(2, 4): Brute Force={result1.val}, BST Recursive={result2.val}, BST Iterative={result3.val}")
    
    # Test case 3: LCA(0, 5) should be 2
    node_5 = root.left.right.right
    result2 = sol2.lowestCommonAncestor(root, node_0, node_5)
    print(f"LCA(0, 5): {result2.val}")  # Expected: 2
    
    # Test edge case: same node
    result2 = sol2.lowestCommonAncestor(root, node_4, node_4)
    print(f"LCA(4, 4): {result2.val}")  # Expected: 4

# Strategy:
# 1. Start with Solution 1 (Brute Force) - shows you understand generic LCA problem
# 2. Optimize to Solution 2 (Iterative BST) - this is what they want to see most
# 3. If time permits, mention Solution 3 (Recursive BST) as alternative approach
#
# Key insight: BST property allows us to determine search direction without exploring both subtrees
# Solution 2 (iterative approach) is preferred:
# - Optimal O(1) space complexity with no recursion overhead
# - Direct and intuitive three-way decision logic based on value comparisons
# - Clear single-path traversal that's easy to trace and debug
# - Leverages BST property to reduce search space significantly
# - Shows understanding of when recursion is unnecessary for predictable paths
