# LeetCode 110: Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Brute Force - Calculate Height for Each Node
# Time: O(n²) → For each node O(n), calculate height O(n)
# Space: O(n) → Recursion stack for both traversal and height calculation
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            """Calculate height of tree rooted at node"""
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        
        def check_balanced(node):
            """Check if tree rooted at node is balanced"""
            if not node:
                return True
            
            # Calculate heights of left and right subtrees
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return False
            
            # Recursively check if left and right subtrees are balanced
            return check_balanced(node.left) and check_balanced(node.right)
        
        return check_balanced(root)

# Solution 2: Optimized DFS - Calculate Height and Check Balance in One Pass
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Recursion stack depth equals tree height
# ★ This is the classic interview solution ★
class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            """Returns height if balanced, -1 if not balanced"""
            # Base case: empty node is balanced with height 0
            if not node:
                return 0
            
            # Get height of left subtree
            left_height = dfs(node.left)
            if left_height == -1:  # Left subtree is not balanced
                return -1
            
            # Get height of right subtree
            right_height = dfs(node.right)
            if right_height == -1:  # Right subtree is not balanced
                return -1
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return height of current subtree
            return max(left_height, right_height) + 1
        
        return dfs(root) != -1

# Solution 3: Advanced - Using Tuple Return for Clean Code
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Recursion stack depth equals tree height
class Solution3:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            """Returns (is_balanced, height)"""
            # Base case: empty node is balanced with height 0
            if not node:
                return True, 0
            
            # Check left subtree
            left_balanced, left_height = dfs(node.left)
            if not left_balanced:
                return False, 0
            
            # Check right subtree
            right_balanced, right_height = dfs(node.right)
            if not right_balanced:
                return False, 0
            
            # Check if current node is balanced
            is_balanced = abs(left_height - right_height) <= 1
            height = max(left_height, right_height) + 1
            
            return is_balanced, height
        
        return dfs(root)[0]

# Test function
def test_solutions():
    # Create test tree:      3
    #                       / \
    #                      9   20
    #                         /  \
    #                        15   7
    # Expected: True (balanced)
    
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    # Create unbalanced tree:  1
    #                         / \
    #                        2   2
    #                       / \
    #                      3   3
    #                     / \
    #                    4   4
    # Expected: False (not balanced)
    
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"Brute Force - Balanced Tree: {sol1.isBalanced(root1)}")      # Expected: True
    print(f"Optimized DFS - Balanced Tree: {sol2.isBalanced(root1)}")    # Expected: True
    print(f"Advanced - Balanced Tree: {sol3.isBalanced(root1)}")         # Expected: True
    
    print(f"Brute Force - Unbalanced Tree: {sol1.isBalanced(root2)}")    # Expected: False
    print(f"Optimized DFS - Unbalanced Tree: {sol2.isBalanced(root2)}")  # Expected: False
    print(f"Advanced - Unbalanced Tree: {sol3.isBalanced(root2)}")       # Expected: False
    
    # Test edge case: empty tree
    print(f"Empty tree: {sol2.isBalanced(None)}")                        # Expected: True
    
    # Test single node
    single_node = TreeNode(1)
    print(f"Single node: {sol2.isBalanced(single_node)}")                # Expected: True

# Strategy:
# 1. Start with Solution 1 (Brute Force) - shows you understand the problem definition
# 2. Optimize to Solution 2 (Optimized DFS) - this is what they want to see most
# 3. If time permits, mention Solution 3 (Tuple Return) as cleaner alternative
#
# Key insight: A tree is balanced if every node's left and right subtrees differ in height by at most 1
# Why Solution 2 is preferred:
# - Single pass algorithm combining height calculation with balance check
# - Early termination when imbalance is detected (-1 return value)
# - Optimal O(n) time complexity with minimal space usage
# - Clean and efficient implementation using sentinel value pattern
