# LeetCode 104: Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node.

from typing import Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Brute Force - Level by Level Traversal
# Time: O(n) → Visit each node exactly once
# Space: O(w) → Where w is maximum width of tree (for queue storage)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Handle empty tree
        if not root:
            return 0
        
        # Use BFS to traverse level by level
        queue = deque([root])
        depth = 0
        
        while queue:
            # Process all nodes at current level
            level_size = len(queue)
            depth += 1
            
            # Process each node in current level
            for _ in range(level_size):
                node = queue.popleft()
                
                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth

# Solution 2: Recursive DFS - Top Down Approach (Classic Interview Solution)
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Recursion stack depth equals tree height
# ★ This is the classic interview solution ★
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: empty node has depth 0
        if not root:
            return 0
        
        # Recursively find depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Current depth is 1 + maximum of left and right depths
        return max(left_depth, right_depth) + 1

# Solution 3: Advanced - Iterative DFS with Stack
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Stack storage for DFS traversal
class Solution3:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Handle empty tree
        if not root:
            return 0
        
        # Use stack to store (node, current_depth) pairs
        stack = [(root, 1)]
        max_depth = 0
        
        while stack:
            node, current_depth = stack.pop()
            
            # Update maximum depth seen so far
            max_depth = max(max_depth, current_depth)
            
            # Add children to stack with incremented depth
            if node.left:
                stack.append((node.left, current_depth + 1))
            if node.right:
                stack.append((node.right, current_depth + 1))
        
        return max_depth

# Test function
def test_solutions():
    # Create test tree:      3
    #                       / \
    #                      9   20
    #                         /  \
    #                        15   7
    # Expected depth: 3
    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"BFS Level Order: {sol1.maxDepth(root)}")      # Expected: 3
    print(f"Recursive DFS: {sol2.maxDepth(root)}")        # Expected: 3
    print(f"Iterative DFS: {sol3.maxDepth(root)}")        # Expected: 3
    
    # Test edge case: empty tree
    print(f"Empty tree: {sol2.maxDepth(None)}")           # Expected: 0
    
    # Test single node
    single_node = TreeNode(1)
    print(f"Single node: {sol2.maxDepth(single_node)}")   # Expected: 1

# Strategy:
# 1. Start with Solution 1 (BFS Level Order) - shows you understand the problem clearly
# 2. Optimize to Solution 2 (Recursive DFS) - this is what they want to see most
# 3. If time permits, mention Solution 3 (Iterative DFS) as space-efficient alternative
#
# Key insight: Tree depth = 1 + maximum depth of left and right subtrees
# Why Solution 2 is preferred:
# - Most intuitive and clean recursive approach
# - Directly matches the mathematical definition of tree depth
# - Easy to explain and implement under pressure
# - Optimal time complexity with minimal space usage
