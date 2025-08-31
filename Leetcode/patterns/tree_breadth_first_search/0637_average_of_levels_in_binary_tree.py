# LeetCode 637: Average of Levels in Binary Tree
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array

from typing import List, Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) → Visit each node once during level order traversal
# Space: O(w) → O(n) worst case, where w is max width of tree level
# ★ This is the classic solution ★
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS level order traversal - calculate average for each level
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            level_sum = 0
            level_len = len(queue)

            # Process all nodes in current level
            for _ in range(level_len):
                node = queue.popleft()
                level_sum += node.val

                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            # Calculate and store average for this level
            res.append(level_sum / level_len)
        
        return res

# Time: O(n) → Visit each node once in DFS traversal
# Space: O(d) → O(n) worst case, where d is tree depth (recursion stack + level arrays)
class Solution2:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # DFS approach - collect level sums and counts, then calculate averages
        if not root:
            return []
        
        level_sums = []
        level_counts = []
        
        def dfs(node, depth):
            if not node:
                return
            
            # Expand arrays if we reach a new depth
            if depth >= len(level_sums):
                level_sums.append(0)
                level_counts.append(0)
            
            # Add current node to its level's sum and count
            level_sums[depth] += node.val
            level_counts[depth] += 1
            
            # Recurse on children
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        
        # Calculate averages from sums and counts
        return [level_sums[i] / level_counts[i] for i in range(len(level_sums))]

# Time: O(n) → Visit each node once, final average calculation also O(n) for all levels
# Space: O(n) → Store all node values in level_map plus recursion stack O(d)
class Solution3:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # DFS with level mapping approach - store all values per level
        if not root:
            return []
        
        level_map = {}
        
        def dfs(node, depth):
            if not node:
                return
            
            # Initialize list for new level
            if depth not in level_map:
                level_map[depth] = []
            
            # Add node value to its level
            level_map[depth].append(node.val)
            
            # Recurse on children
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        
        # Calculate averages from stored values
        return [sum(level_map[i]) / len(level_map[i]) for i in range(len(level_map))]

# Test function
def test_solutions():
    # Create test case: [3,9,20,null,null,15,7]
    # Expected: [3.0, 14.5, 11.0] (level 0: 3, level 1: (9+20)/2=14.5, level 2: (15+7)/2=11.0)
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"BFS Level Order: {sol1.averageOfLevels(root)}")     # Expected: [3.0, 14.5, 11.0]
    print(f"DFS Sum/Count: {sol2.averageOfLevels(root)}")       # Expected: [3.0, 14.5, 11.0]
    print(f"DFS Level Map: {sol3.averageOfLevels(root)}")       # Expected: [3.0, 14.5, 11.0]
    
    # Test case: [3,9,20,15,7]
    # Expected: [3.0, 14.5, 11.0]
    root2 = TreeNode(3)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.left.left = TreeNode(15)
    root2.left.right = TreeNode(7)
    
    print(f"Different structure - BFS: {sol1.averageOfLevels(root2)}")   # Expected: [3.0, 14.5, 11.0]
    print(f"Different structure - DFS: {sol2.averageOfLevels(root2)}")   # Expected: [3.0, 14.5, 11.0]
    print(f"Different structure - Map: {sol3.averageOfLevels(root2)}")   # Expected: [3.0, 14.5, 11.0]
    
    # Test edge cases
    print(f"Empty tree - BFS: {sol1.averageOfLevels(None)}")            # Expected: []
    
    single = TreeNode(1)
    print(f"Single node - DFS: {sol2.averageOfLevels(single)}")         # Expected: [1.0]
    
    # Test large numbers to check for integer overflow
    large = TreeNode(2147483647)  # Max 32-bit int
    large.left = TreeNode(2147483647)
    large.right = TreeNode(2147483647)
    print(f"Large numbers - BFS: {sol1.averageOfLevels(large)}")        # Expected: [2147483647.0, 2147483647.0]


# 1. Start with Solution 1 (BFS level order) 
# 2. If asked for alternatives, show Solution 2 (DFS with sum/count) 
# 3. If time permits, mention Solution 3 (DFS level mapping) 

# Key insight: Level averages require both sum and count for each level - BFS naturally processes complete levels
# Solution 1 is preferred: Direct level processing, clear average calculation, matches problem structure
