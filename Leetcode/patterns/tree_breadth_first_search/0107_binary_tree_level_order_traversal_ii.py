# LeetCode 107: Binary Tree Level Order Traversal II
# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values

from typing import List, Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) → Visit each node exactly once
# Space: O(n) → Queue stores up to n/2 nodes, result stores all n values
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        # Standard BFS level order traversal
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
        
        # Reverse to get bottom-up order
        return result[::-1]

# Time: O(n) → Visit each node once, reversing is O(levels) which is O(log n) to O(n)
# Space: O(n) → Two lists store up to n/2 nodes each in worst case

class Solution2:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS with level tracking then reverse - most intuitive approach
        if not root:
            return []
        
        result = []
        current_level = [root]
        
        # Process level by level from top to bottom
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
        
        # Reverse to get bottom-up order
        return result[::-1]

# Time: O(n) → DFS visits each node once, no reversal needed
# Space: O(h + n) → Recursion stack height + result storage
class Solution3:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS approach building result in reverse order - avoids final reversal
        if not root:
            return []
        
        # First pass: determine tree depth
        def get_depth(node):
            if not node:
                return 0
            return 1 + max(get_depth(node.left), get_depth(node.right))
        
        depth = get_depth(root)
        result = [[] for _ in range(depth)]
        
        # Second pass: fill result from bottom up
        def dfs(node, level):
            if not node:
                return
            
            # Add to result in reverse level order (depth - 1 - level)
            result[depth - 1 - level].append(node.val)
            
            # Process children at next level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return result

# Test function
def test_solutions():
    # Create test case: [3,9,20,null,null,15,7]
    # Expected: [[15,7],[9,20],[3]]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"Brute Force: {sol1.levelOrderBottom(root)}")  # Expected: [[15,7],[9,20],[3]]
    print(f"Classic: {sol2.levelOrderBottom(root)}")      # Expected: [[15,7],[9,20],[3]]
    print(f"Advanced: {sol3.levelOrderBottom(root)}")     # Expected: [[15,7],[9,20],[3]]
    
    # Test edge case: empty tree
    print(f"Empty tree - Brute Force: {sol1.levelOrderBottom(None)}")  # Expected: []
    print(f"Empty tree - Classic: {sol2.levelOrderBottom(None)}")      # Expected: []
    print(f"Empty tree - Advanced: {sol3.levelOrderBottom(None)}")     # Expected: []
    
    # Test single node
    single = TreeNode(1)
    print(f"Single node - Classic: {sol2.levelOrderBottom(single)}")   # Expected: [[1]]

# Strategy:
# 1. Start with Solution 1 (BFS then reverse) 
# 2. Optimize to Solution 2 (cleaner BFS then reverse)
# 3. If time permits, mention Solution 3 (DFS without reversal) - shows optimization thinking
#
# Key insight: This is essentially LeetCode 102 with result reversal - reuse BFS knowledge
