# LeetCode 226: Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.
# Inverting a binary tree means swapping the left and right children of every node in the tree.

from typing import Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Brute Force - Level Order Traversal with Queue
# Time: O(n) → Visit each node exactly once
# Space: O(w) → Where w is maximum width of tree (queue storage)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Handle empty tree
        if not root:
            return None
        
        # Use BFS to traverse level by level and swap children
        queue = deque([root])
        
        while queue:
            # Process current level
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # Swap left and right children
                node.left, node.right = node.right, node.left
                
                # Add children to queue for next level processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root

# Solution 2: Recursive DFS - Post Order Approach (Classic Interview Solution)
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Recursion stack depth equals tree height
# ★ This is the classic interview solution ★
class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: If the current node is None, nothing to invert
        if not root:
            return None

        # Recursively invert the left and right subtrees first
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # After both subtrees are processed, swap them
        root.left = right
        root.right = left

        # Return the root with its left and right subtrees inverted
        return root

# Solution 3: Advanced - Alternative Recursive Style (Pre-order)
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Recursion stack depth equals tree height
class Solution3:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: empty node needs no inversion
        if not root:
            return None
        
        # Swap the left and right children first (pre-order)
        root.left, root.right = root.right, root.left
        
        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

# Helper function for testing
def print_tree_inorder(root):
    """Print tree in inorder traversal for verification"""
    if not root:
        return []
    result = []
    result.extend(print_tree_inorder(root.left))
    result.append(root.val)
    result.extend(print_tree_inorder(root.right))
    return result

def print_tree_levelorder(root):
    """Print tree in level order for better visualization"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    
    return result

# Test function
def test_solutions():
    # Create test tree:      4
    #                       / \
    #                      2   7
    #                     / \ / \
    #                    1  3 6  9
    # Expected inverted: [4,7,2,9,6,3,1] (level order)
    
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    
    print("Original tree (level order):", print_tree_levelorder(root))
    
    # Test Solution 2 (make a copy for testing)
    root_copy = TreeNode(4)
    root_copy.left = TreeNode(2)
    root_copy.right = TreeNode(7)
    root_copy.left.left = TreeNode(1)
    root_copy.left.right = TreeNode(3)
    root_copy.right.left = TreeNode(6)
    root_copy.right.right = TreeNode(9)
    
    sol2 = Solution2()
    inverted = sol2.invertTree(root_copy)
    print("Inverted tree (level order):", print_tree_levelorder(inverted))
    
    # Test edge cases
    sol1 = Solution()
    sol3 = Solution3()
    
    # Empty tree
    print(f"Empty tree: {sol2.invertTree(None)}")  # Expected: None
    
    # Single node
    single_node = TreeNode(1)
    result = sol2.invertTree(single_node)
    print(f"Single node: {print_tree_levelorder(result)}")  # Expected: [1]

# Strategy:
# 1. Start with Solution 1 (BFS Level Order) - shows you understand tree traversal
# 2. Optimize to Solution 2 (Post-order DFS) - this is the most elegant recursive solution
# 3. If time permits, mention Solution 3 (Pre-order DFS) as alternative recursive style
#
# Key insight: Tree inversion means swapping left and right children for every node
# Why Solution 2 (your approach) is preferred:
# - Post-order traversal: process children first, then current node
# - More explicit variable assignment shows clear thinking process
# - Natural bottom-up approach that's easy to trace and debug
# - Clean separation between recursive calls and swapping logic
