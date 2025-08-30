# LeetCode 103: Binary Tree Zigzag Level Order Traversal
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values

from typing import List, Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) → Visit each node once, plus O(level_width) for reverse operations
# Space: O(n) → Queue stores up to n/2 nodes, result stores all n values
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []
        
        result = []
        queue = deque([root])
        level = 0
        
        # BFS with level tracking
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
            
            # Reverse odd levels for zigzag pattern
            if level % 2 == 1:
                current_level.reverse()
            
            result.append(current_level)
            level += 1
        
        return result

# Time: O(n) → Visit each node exactly once, reverse operations total O(n) across all levels
# Space: O(n) → Queue stores up to n/2 nodes, result stores all n values

class Solution2:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS with conditional reverse - clean and intuitive approach
        if not root:
            return []

        queue = deque([root])
        result = []
        left_to_right = True
        
        while queue:
            level = []

            # Process all nodes in current level
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add level to result with correct direction
            if left_to_right:
                result.append(level)
            else:
                result.append(level[::-1])

            left_to_right = not left_to_right

        return result

# Time: O(n) → DFS visits each node once, direct insertion avoids reversal
# Space: O(h + n) → Recursion stack height + result storage
class Solution3:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS approach with level tracking and direction control
        if not root:
            return []
        
        result = []
        
        def dfs(node, level):
            if not node:
                return
            
            # Expand result if we reach a new level
            if level >= len(result):
                result.append([])
            
            # Insert based on level parity
            if level % 2 == 0:
                result[level].append(node.val)         # Left to right
            else:
                result[level].insert(0, node.val)      # Right to left
            
            # Recursively process children
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return result

# Test function
def test_solutions():
    # Create test case: [3,9,20,null,null,15,7]
    # Expected: [[3],[20,9],[15,7]]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"Brute Force: {sol1.zigzagLevelOrder(root)}")  # Expected: [[3],[20,9],[15,7]]
    print(f"Classic: {sol2.zigzagLevelOrder(root)}")      # Expected: [[3],[20,9],[15,7]]
    print(f"Advanced: {sol3.zigzagLevelOrder(root)}")     # Expected: [[3],[20,9],[15,7]]
    
    # Test edge case: empty tree
    print(f"Empty tree - Brute Force: {sol1.zigzagLevelOrder(None)}")  # Expected: []
    print(f"Empty tree - Classic: {sol2.zigzagLevelOrder(None)}")      # Expected: []
    print(f"Empty tree - Advanced: {sol3.zigzagLevelOrder(None)}")     # Expected: []
    
    # Test single node
    single = TreeNode(1)
    print(f"Single node - Classic: {sol2.zigzagLevelOrder(single)}")   # Expected: [[1]]
    
    # Test complex zigzag case: [1,2,3,4,5,6,7]
    # Expected: [[1],[3,2],[4,5,6,7]]
    complex_root = TreeNode(1)
    complex_root.left = TreeNode(2)
    complex_root.right = TreeNode(3)
    complex_root.left.left = TreeNode(4)
    complex_root.left.right = TreeNode(5)
    complex_root.right.left = TreeNode(6)
    complex_root.right.right = TreeNode(7)
    print(f"Complex zigzag - Classic: {sol2.zigzagLevelOrder(complex_root)}")

# Key insight: Zigzag is level order traversal with alternating direction per level
