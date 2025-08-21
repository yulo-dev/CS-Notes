# LeetCode 543: Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Brute Force - Calculate diameter for each node
# Time: O(n²) → For each node O(n), calculate height O(n) 
# Space: O(n) → Recursion stack for both traversal and height calculation
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def get_height(node):
            """Get height of tree rooted at node"""
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        
        def get_all_diameters(node):
            """Get maximum diameter in tree rooted at node"""
            if not node:
                return 0
            
            # Diameter through current node
            left_height = get_height(node.left)
            right_height = get_height(node.right) 
            diameter_through_node = left_height + right_height
            
            # Maximum diameter in left and right subtrees
            left_diameter = get_all_diameters(node.left)
            right_diameter = get_all_diameters(node.right)
            
            return max(diameter_through_node, left_diameter, right_diameter)
        
        return get_all_diameters(root)

# Solution 2: Optimized DFS - Calculate height and diameter in one pass
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Recursion stack depth equals tree height
# ★ This is the classic interview solution ★
class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def dfs(node):
            """Returns height of subtree, updates global max_diameter"""
            if not node:
                return 0
            
            # Get height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update global maximum diameter
            # Diameter through current node = left_height + right_height
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return height of current subtree
            return max(left_height, right_height) + 1
        
        dfs(root)
        return self.max_diameter

# Solution 3: Advanced - No global variable (cleaner but harder to explain)
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Recursion stack depth equals tree height
class Solution3:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            """Returns (height, max_diameter_in_subtree)"""
            if not node:
                return 0, 0
            
            left_height, left_max = dfs(node.left)
            right_height, right_max = dfs(node.right)
            
            current_height = max(left_height, right_height) + 1
            current_diameter = left_height + right_height
            max_diameter = max(current_diameter, left_max, right_max)
            
            return current_height, max_diameter
        
        return dfs(root)[1]

# Test function
def test_solutions():
    # Create test tree:      1
    #                       / \
    #                      2   3
    #                     / \
    #                    4   5
    # Expected diameter: 3 (path: 4-2-1-3 or 5-2-1-3)
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"Brute Force: {sol1.diameterOfBinaryTree(root)}")      # Expected: 3
    print(f"Classic DFS: {sol2.diameterOfBinaryTree(root)}")      # Expected: 3
    print(f"Advanced: {sol3.diameterOfBinaryTree(root)}")         # Expected: 3


# 1. Start with Solution 1 (Brute Force) - shows you understand the problem
# 2. Optimize to Solution 2 (Classic DFS) - this is what they want to see
# 3. If asked for improvements, mention Solution 3 but stick with Solution 2
# 
# Key insight: Diameter through a node = left_subtree_height + right_subtree_height
# We need to check this for every node and take the maximum
