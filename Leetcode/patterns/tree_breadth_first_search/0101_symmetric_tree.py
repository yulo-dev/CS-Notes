# LeetCode 101: Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (symmetric around its center)

from typing import Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution1 (BFS with pair queue)
# Time: O(n) – each node enters/exits the queue at most once
# Space: O(n) – queue can hold up to O(w) nodes at the widest level (worst-case O(n))

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Iterative BFS approach - using queue to simulate recursion
        if not root:
            return True
        
        queue = deque([(root.left, root.right)])
        
        while queue:
            left, right = queue.popleft()
            
            # Both nodes are null - continue to next pair
            if not left and not right:
                continue
                
            # One node is null, other is not - not symmetric
            if not left or not right:
                return False
                
            # Values don't match - not symmetric
            if left.val != right.val:
                return False
            
            # Add symmetric pairs for next iteration
            queue.append((left.left, right.right))    # Outer pair
            queue.append((left.right, right.left))    # Inner pair
        
        return True


# Solution2 (DFS recursion)
# Time: O(n)
# Space: O(h) – recursion stack height (average O(log n), worst O(n))

class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Two-Tree Comparison Pattern using DFS recursion
        if not root:
            return True

        def isMirror(t1, t2):
            # Base case: both nodes are null - symmetric
            if not t1 and not t2:
                return True
            
            # Base case: one null, one non-null - not symmetric
            if not t1 or not t2:
                return False
            
            # Recursive case: current values equal AND subtrees are mirror
            return (t1.val == t2.val and
                    isMirror(t1.left, t2.right) and  # Outer symmetry
                    isMirror(t1.right, t2.left))     # Inner symmetry

        return isMirror(root.left, root.right)


# Solution3 (Level-by-level palindrome check)
# Time: O(n)
# Space: O(n) – store one level (values + next_level) plus queue

class Solution3:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Level-by-level comparison approach
        if not root:
            return True
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_values = []
            next_level = []
            
            # Collect current level values and nodes
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val if node else None)
                
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)
            
            # Check if current level is palindrome
            if level_values != level_values[::-1]:
                return False
            
            # Add next level nodes to queue if any non-null exist
            if any(node for node in next_level):
                queue.extend(next_level)
        
        return True

# Test function
def test_solutions():
    # Create test case: [1,2,2,3,4,4,3] - symmetric tree
    # Expected: True
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"BFS Queue: {sol1.isSymmetric(root1)}")       # Expected: True
    print(f"DFS Recursion: {sol2.isSymmetric(root1)}")   # Expected: True
    print(f"Level Compare: {sol3.isSymmetric(root1)}")   # Expected: True
    
    # Test asymmetric tree: [1,2,2,null,3,null,3]
    # Expected: False
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)
    
    print(f"Asymmetric - BFS: {sol1.isSymmetric(root2)}")       # Expected: False
    print(f"Asymmetric - DFS: {sol2.isSymmetric(root2)}")       # Expected: False
    print(f"Asymmetric - Level: {sol3.isSymmetric(root2)}")     # Expected: False
    
    # Test edge cases
    print(f"Empty tree - DFS: {sol2.isSymmetric(None)}")        # Expected: True
    
    single = TreeNode(1)
    print(f"Single node - DFS: {sol2.isSymmetric(single)}")     # Expected: True

# Interview Strategy:
# 1. Start with Solution 1 (BFS queue approach) 
# 2. Optimize to Solution 2 (DFS recursion) 
# 3. If time permits, mention Solution 3 (level comparison) 
#
# Key insight: Symmetric tree is about comparing two subtrees in mirror fashion, not level order traversal
# Why Solution 2 is preferred: Clean recursive structure, natural mirror comparison, optimal space complexity
