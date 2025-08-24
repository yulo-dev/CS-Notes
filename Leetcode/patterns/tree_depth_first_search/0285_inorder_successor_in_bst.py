# LeetCode 285: Inorder Successor in BST
# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST.
# If the given node has no in-order successor in the tree, return null.
# The successor of a node p is the node with the smallest key greater than p.val.

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Brute Force - Inorder Traversal and Find Next
# Time: O(n) → Must traverse entire tree to build inorder list
# Space: O(n) → Store all node values in list
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def inorder(node):
            """Collect all nodes using inorder traversal"""
            if not node:
                return []
            
            result = []
            result.extend(inorder(node.left))   # Left subtree
            result.append(node)                 # Current node
            result.extend(inorder(node.right))  # Right subtree
            
            return result
        
        # Get all nodes in sorted order
        nodes = inorder(root)
        
        # Find p and return next node
        for i in range(len(nodes)):
            if nodes[i] == p:
                return nodes[i + 1] if i + 1 < len(nodes) else None
        
        return None

# Solution 2: BST Property with Iterative Search (Classic Solution)
# Time: O(h) → Best case O(log n), worst case O(n) for skewed tree
# Space: O(1) → Only constant extra space
class Solution2:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        current = root
        
        while current:
            # If current value is greater than p's value,
            # it could be a potential successor
            if current.val > p.val:
                successor = current  # Update potential successor
                current = current.left  # Look for smaller successor in left subtree
            else:
                # If current value is <= p's value, successor must be in right subtree
                current = current.right
        
        return successor

# Solution 3: Advanced - Two-Case BST Logic
# Time: O(h) → Best case O(log n), worst case O(n) for skewed tree
# Space: O(1) → Only constant extra space
class Solution3:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # Case 1: p has right subtree - successor is leftmost node in right subtree
        if p.right:
            current = p.right
            while current.left:
                current = current.left
            return current
        
        # Case 2: p has no right subtree - find ancestor where p is in left subtree
        successor = None
        current = root
        
        while current:
            if p.val < current.val:
                successor = current  # current could be the successor
                current = current.left
            elif p.val > current.val:
                current = current.right
            else:
                # Found p, but it has no right subtree (handled in case 1)
                break
        
        return successor

# Alternative Solution: Using Stack for Iterative Inorder
class Solution3_Alternative:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """Iterative inorder traversal until we find successor"""
        stack = []
        current = root
        found_p = False
        
        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node
            current = stack.pop()
            
            # If we found p in previous iteration, current is the successor
            if found_p:
                return current
            
            # Mark that we found p
            if current == p:
                found_p = True
            
            # Move to right subtree
            current = current.right
        
        return None  # No successor found

# Test function
def test_solutions():
    # Create test BST:      2
    #                      / \
    #                     1   3
    # Test cases: successor of 1 should be 2, successor of 2 should be 3, successor of 3 should be None
    
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    node_1 = root.left
    node_2 = root
    node_3 = root.right
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    # Test successor of 1
    result1 = sol1.inorderSuccessor(root, node_1)
    result2 = sol2.inorderSuccessor(root, node_1)
    result3 = sol3.inorderSuccessor(root, node_1)
    
    print(f"Successor of 1: Brute Force={result1.val if result1 else None}, "
          f"BST Iterative={result2.val if result2 else None}, "
          f"Two-Case={result3.val if result3 else None}")
    
    # Test successor of 2
    result2_2 = sol2.inorderSuccessor(root, node_2)
    print(f"Successor of 2: {result2_2.val if result2_2 else None}")  # Expected: 3
    
    # Test successor of 3 (should be None)
    result2_3 = sol2.inorderSuccessor(root, node_3)
    print(f"Successor of 3: {result2_3.val if result2_3 else None}")  # Expected: None
    
    # Test larger BST:      5
    #                      / \
    #                     3   6
    #                    / \   \
    #                   2   4   7
    #                  /
    #                 1
    
    larger_root = TreeNode(5)
    larger_root.left = TreeNode(3)
    larger_root.right = TreeNode(6)
    larger_root.left.left = TreeNode(2)
    larger_root.left.right = TreeNode(4)
    larger_root.right.right = TreeNode(7)
    larger_root.left.left.left = TreeNode(1)
    
    node_3_large = larger_root.left
    result_3_large = sol2.inorderSuccessor(larger_root, node_3_large)
    print(f"Successor of 3 in larger BST: {result_3_large.val if result_3_large else None}")  # Expected: 4

# Strategy:
# 1. Start with Solution 1 (Brute Force)
# 2. Optimize to Solution 2 (BST Iterative) 
# 3. If time permits, mention Solution 3 (Two-Case Logic) as comprehensive approach
#
# Key insight: Successor is the smallest node greater than p.val, leveraging BST property
# Solution 2 is preferred:
# - Leverages BST property for O(h) time complexity instead of O(n)
# - Simple iterative approach with O(1) space complexity
# - Clean logic: if current > p.val, it's a candidate; otherwise search right
# - No need to handle special cases separately
# - Easy to explain and implement under pressure
