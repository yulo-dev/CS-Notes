# LeetCode 102: Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values

from typing import List, Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) → Visit each node exactly once
# Space: O(w) → Queue stores at most the width of the tree (maximum nodes at any level)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        # Process each level
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result

# Time: O(n) → Visit each node exactly once using BFS approach
# Space: O(n) → Queue stores up to n/2 nodes in worst case (complete binary tree last level)
class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS with level tracking - most common interview approach
        if not root:
            return []
        
        result = []
        current_level = [root]
        
        # Process level by level
        while current_level:
            level_values = []
            next_level = []
            
            # Process all nodes in current level
            for node in current_level:
                level_values.append(node.val)
                
                # Collect children for next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            result.append(level_values)
            current_level = next_level
        
        return result

# Time: O(n) → DFS visits each node once, list operations are O(1) amortized
# Space: O(h + w) → Recursion stack height + result storage
class Solution3:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS approach with level tracking - demonstrates depth-first alternative
        if not root:
            return []
        
        result = []
        
        def dfs(node, level):
            if not node:
                return
            
            # Expand result if we reach a new level
            if level >= len(result):
                result.append([])
            
            # Add current node to its level
            result[level].append(node.val)
            
            # Recursively process children at next level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return result

# Test function
def test_solutions():
    # Create test case: [3,9,20,null,null,15,7]
    # Expected: [[3],[9,20],[15,7]]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"Brute Force: {sol1.levelOrder(root)}")  # Expected: [[3],[9,20],[15,7]]
    print(f"Classic: {sol2.levelOrder(root)}")      # Expected: [[3],[9,20],[15,7]]
    print(f"Advanced: {sol3.levelOrder(root)}")     # Expected: [[3],[9,20],[15,7]]
    
    # Test edge case: empty tree
    print(f"Empty tree - Brute Force: {sol1.levelOrder(None)}")  # Expected: []
    print(f"Empty tree - Classic: {sol2.levelOrder(None)}")      # Expected: []
    print(f"Empty tree - Advanced: {sol3.levelOrder(None)}")     # Expected: []
    
    # Test single node
    single = TreeNode(1)
    print(f"Single node - Classic: {sol2.levelOrder(single)}")   # Expected: [[1]]

# Strategy:
# 1. Start with Solution 1 (BFS with deque) 
# 2. Optimize to Solution 2 (BFS with lists) 
# 3. If time permits, mention Solution 3 (DFS approach) - shows algorithmic flexibility
#
# Key insight: Level order traversal is naturally a BFS problem - process nodes level by level
# Why Solution 2 is preferred: Clean, readable BFS implementation that's easy to explain and debug

if __name__ == "__main__":
    test_solutions()
