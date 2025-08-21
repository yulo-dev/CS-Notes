# LeetCode 199: Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

from typing import Optional, List
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Brute Force - Level Order Traversal with Full Level Storage
# Time: O(n) → Visit each node exactly once
# Space: O(w) → Where w is maximum width of tree (queue + level storage)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes at current level
            for i in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Take the rightmost node from current level
            result.append(current_level[-1])
        
        return result

# Solution 2: Optimized BFS - Track Only Rightmost Node per Level (Classic Interview Solution)
# Time: O(n) → Visit each node exactly once
# Space: O(w) → Where w is maximum width of tree (queue storage only)
# ★ This is the classic interview solution ★
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            # Process all nodes at current level
            for i in range(level_size):
                node = queue.popleft()
                
                # If this is the last node in current level, add to result
                if i == level_size - 1:
                    result.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

# Solution 3: Advanced - DFS with Level Tracking (Space Optimized)
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Recursion stack depth equals tree height
class Solution3:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return

            # If this is the first time we visit this depth level,
            # this node is the rightmost so far (due to right-first traversal)
            if depth == len(res):
                res.append(node.val)
            
            # Traverse right first, then left (to ensure rightmost is captured first)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res

# Alternative Solution 3: DFS with Reverse Level Order
class Solution3_Alternative:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, level):
            if not node:
                return
            
            # Extend result list if we reach a new level
            if level >= len(self.result):
                self.result.append(node.val)
            
            # Visit right subtree first to capture rightmost node
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        self.result = []
        dfs(root, 0)
        return self.result

# Test function
def test_solutions():
    # Create test tree:      1
    #                       / \
    #                      2   3
    #                       \   \
    #                        5   4
    # Expected right side view: [1, 3, 4]
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"Brute Force BFS: {sol1.rightSideView(root)}")        # Expected: [1, 3, 4]
    print(f"Optimized BFS: {sol2.rightSideView(root)}")          # Expected: [1, 3, 4]
    print(f"DFS with Level Tracking: {sol3.rightSideView(root)}")# Expected: [1, 3, 4]
    
    # Test edge cases
    print(f"Empty tree: {sol2.rightSideView(None)}")             # Expected: []
    
    # Test single node
    single_node = TreeNode(1)
    print(f"Single node: {sol2.rightSideView(single_node)}")     # Expected: [1]
    
    # Test left-heavy tree:  1
    #                       /
    #                      2
    #                     /
    #                    3
    # Expected: [1, 2, 3]
    left_heavy = TreeNode(1)
    left_heavy.left = TreeNode(2)
    left_heavy.left.left = TreeNode(3)
    print(f"Left-heavy tree: {sol2.rightSideView(left_heavy)}")  # Expected: [1, 2, 3]

# Strategy:
# 1. Start with Solution 1 (Brute Force BFS) - shows you understand the problem clearly
# 2. Optimize to Solution 2 (Optimized BFS) - this is the most common interview solution
# 3. If time permits, mention Solution 3 (DFS) - this elegant approach shows advanced thinking
#
# Key insight: Right side view = rightmost node at each level
# Why Solution 3 (DFS approach) is also excellent:
# - Better space complexity: O(h) instead of O(w) for BFS
# - Elegant use of closure to avoid passing result parameter
# - Right-first traversal ensures we capture rightmost node at each depth
# - Clean and concise implementation that's easy to understand
