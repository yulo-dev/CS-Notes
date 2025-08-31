# LeetCode 199: Binary Tree Right Side View
# Given the root of a binary tree, return the values of the nodes you can see ordered from top to bottom when looking from the right side

from typing import List, Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) → Visit each node once in level order traversal
# Space: O(w) → O(n) worst case, where w is max width of tree level
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS level order traversal - capture rightmost node of each level
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # Last node in current level is rightmost visible node
                if i == level_size - 1:
                    res.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return res

# Time: O(n) → Visit each node once in DFS traversal
# Space: O(h) → O(n) worst case, where h is height of tree (balanced O(log n), skewed O(n))
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # DFS with right-first traversal - first node at each depth is rightmost
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

# Time: O(n) → Visit each node once, but may store more nodes in result tracking
# Space: O(h + d) → O(n) worst case, where h is recursion depth and d is tree depth
class Solution3:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Alternative DFS approach - update rightmost node for each level
        if not root:
            return []
        
        level_map = {}
        
        def dfs(node, depth):
            if not node:
                return
            
            # Always update with current node (later nodes at same depth override)
            level_map[depth] = node.val
            
            # Traverse left first, then right (so right nodes override left nodes)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        
        # Extract values in level order
        return [level_map[i] for i in range(len(level_map))]

# Test function
def test_solutions():
    # Create test case: [1,2,3,null,5,null,4]
    # Expected: [1,3,4] (right side view: 1 from level 0, 3 from level 1, 4 from level 2)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"BFS Level Order: {sol1.rightSideView(root)}")     # Expected: [1,3,4]
    print(f"DFS Right First: {sol2.rightSideView(root)}")     # Expected: [1,3,4]
    print(f"DFS Level Map: {sol3.rightSideView(root)}")       # Expected: [1,3,4]
    
    # Test case: [1,2,3,4]
    # Expected: [1,3,4] (4 is visible from right side even though it's left child)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    
    print(f"Left child visible - BFS: {sol1.rightSideView(root2)}")     # Expected: [1,3,4]
    print(f"Left child visible - DFS: {sol2.rightSideView(root2)}")     # Expected: [1,3,4]
    print(f"Left child visible - Map: {sol3.rightSideView(root2)}")     # Expected: [1,3,4]
    
    # Test edge cases
    print(f"Empty tree - BFS: {sol1.rightSideView(None)}")             # Expected: []
    
    single = TreeNode(1)
    print(f"Single node - DFS: {sol2.rightSideView(single)}")          # Expected: [1]
    
    # Test case: [1,2] - only left child
    # Expected: [1,2] (left child is visible when no right child exists)
    left_only = TreeNode(1)
    left_only.left = TreeNode(2)
    print(f"Left only - DFS: {sol2.rightSideView(left_only)}")         # Expected: [1,2]

# Strategy:
# 1. Start with Solution 1 (BFS level order) 
# 2. Optimize to Solution 2 (DFS right-first) 
# 3. If time permits, mention Solution 3 (DFS level mapping) 
#
# Key insight: Right side view means rightmost visible node at each level, not necessarily right children
