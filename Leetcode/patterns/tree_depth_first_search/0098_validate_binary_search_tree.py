# LeetCode 98: Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# - The left subtree of a node contains only nodes with keys less than the node's key.
# - The right subtree of a node contains only nodes with keys greater than the node's key.
# - Both the left and right subtrees must also be binary search trees.

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Brute Force - Check Each Node Against All Ancestors
# Time: O(n²) → For each node, potentially check against all ancestors
# Space: O(h) → Recursion stack depth equals tree height
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def get_min_max(node):
            """Get minimum and maximum values in subtree"""
            if not node:
                return float('inf'), float('-inf')
            
            if not node.left and not node.right:
                return node.val, node.val
            
            left_min, left_max = get_min_max(node.left)
            right_min, right_max = get_min_max(node.right)
            
            subtree_min = min(node.val, left_min, right_min)
            subtree_max = max(node.val, left_max, right_max)
            
            return subtree_min, subtree_max
        
        def validate(node):
            """Check if subtree rooted at node is valid BST"""
            if not node:
                return True
            
            # Check if left and right subtrees are valid BSTs
            if not validate(node.left) or not validate(node.right):
                return False
            
            # Check BST property for current node
            if node.left:
                _, left_max = get_min_max(node.left)
                if left_max >= node.val:
                    return False
            
            if node.right:
                right_min, _ = get_min_max(node.right)
                if right_min <= node.val:
                    return False
            
            return True
        
        return validate(root)

# Solution 2: DFS with Min/Max Bounds (Classic Interview Solution)
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Recursion stack depth equals tree height
# ★ This is the classic interview solution ★
class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function that checks whether the current node is within a valid range
        def dfs(node, lower, upper):
            # Base case: empty node is valid by default
            if not node:
                return True
            
            # If the current value violates the BST property, return False
            if not (lower < node.val < upper):
                return False
            
            # Recursively validate the left subtree with updated upper bound
            if not dfs(node.left, lower, node.val):
                return False
            
            # Recursively validate the right subtree with updated lower bound
            if not dfs(node.right, node.val, upper):
                return False
            
            # Current node and subtrees are valid
            return True
        
        # Start recursion with the full valid range
        return dfs(root, float('-inf'), float('inf'))

# Solution 3: Advanced - Inorder Traversal with Previous Value Tracking
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Recursion stack depth equals tree height
class Solution3:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            """Inorder traversal: left -> root -> right"""
            if not node:
                return True
            
            # Traverse left subtree
            if not inorder(node.left):
                return False
            
            # Check current node against previous value
            # In valid BST, inorder traversal gives strictly increasing sequence
            if node.val <= self.prev_val:
                return False
            self.prev_val = node.val
            
            # Traverse right subtree
            return inorder(node.right)
        
        self.prev_val = float('-inf')
        return inorder(root)

# Alternative Solution 3: Iterative Inorder Traversal
class Solution3_Alternative:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Iterative inorder traversal using stack"""
        stack = []
        prev_val = float('-inf')
        current = root
        
        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node
            current = stack.pop()
            
            # Check BST property: current value should be > previous
            if current.val <= prev_val:
                return False
            prev_val = current.val
            
            # Move to right subtree
            current = current.right
        
        return True

# Test function
def test_solutions():
    # Create valid BST:      2
    #                       / \
    #                      1   3
    # Expected: True
    
    valid_bst = TreeNode(2)
    valid_bst.left = TreeNode(1)
    valid_bst.right = TreeNode(3)
    
    # Create invalid BST:    5
    #                       / \
    #                      1   4
    #                         / \
    #                        3   6
    # Expected: False (3 < 5 but in right subtree)
    
    invalid_bst = TreeNode(5)
    invalid_bst.left = TreeNode(1)
    invalid_bst.right = TreeNode(4)
    invalid_bst.right.left = TreeNode(3)
    invalid_bst.right.right = TreeNode(6)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"Brute Force - Valid BST: {sol1.isValidBST(valid_bst)}")         # Expected: True
    print(f"Min/Max Bounds - Valid BST: {sol2.isValidBST(valid_bst)}")      # Expected: True
    print(f"Inorder Traversal - Valid BST: {sol3.isValidBST(valid_bst)}")   # Expected: True
    
    # Reset for testing invalid BST
    sol3 = Solution3()  # Reset prev_val
    print(f"Brute Force - Invalid BST: {sol1.isValidBST(invalid_bst)}")     # Expected: False
    print(f"Min/Max Bounds - Invalid BST: {sol2.isValidBST(invalid_bst)}")  # Expected: False
    print(f"Inorder Traversal - Invalid BST: {sol3.isValidBST(invalid_bst)}")# Expected: False
    
    # Test edge cases
    print(f"Empty tree: {sol2.isValidBST(None)}")                          # Expected: True
    
    # Single node
    single_node = TreeNode(1)
    print(f"Single node: {sol2.isValidBST(single_node)}")                  # Expected: True
    
    # Edge case: duplicate values
    duplicate = TreeNode(1)
    duplicate.left = TreeNode(1)
    print(f"Duplicate values: {sol2.isValidBST(duplicate)}")               # Expected: False

# Strategy:
# 1. Start with Solution 1 (Brute Force) - shows you understand BST properties
# 2. Optimize to Solution 2 (Min/Max Bounds) 
# 3. If time permits, mention Solution 3 (Inorder) as elegant alternative
#
# Key insight: BST property must hold globally, not just locally
# Solution 2 is preferred:
# - Clear step-by-step validation with explicit early returns
# - Easy to trace through the logic during interviews
# - Readable range checking with (lower < node.val < upper)
# - Handles all edge cases naturally including duplicates
# - Clean separation of concerns with helper function
