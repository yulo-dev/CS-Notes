# LeetCode 104: Maximum Depth of Binary Tree
# Given the root of a binary tree, find its maximum depth (longest path from root to any leaf node)

from typing import Optional
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS level-by-level approach - count levels until no more nodes
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            depth += 1

        return depth

# Time: O(n) → Visit each node once with depth tracking
# Space: O(w) → O(n) worst case, where w is max width of tree level
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS with (node, depth) pairs - track depth with each node
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        max_depth = 0
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            # Add children with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return max_depth

# Time: O(n) → Visit each node once in recursive calls
# Space: O(h) → O(n) worst case, where h is height of tree (balanced O(log n), skewed O(n))
# ★ This is the classic interview solution ★
class Solution3:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS recursive approach - natural tree depth calculation
        if not root:
            return 0
        
        # Maximum depth is 1 + max depth of subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)

# Test function
def test_solutions():
    # Create test case: [3,9,20,null,null,15,7]
    # Expected: 3 (levels: 3->9,20->15,7)
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"BFS Level Count: {sol1.maxDepth(root)}")      # Expected: 3
    print(f"BFS Node-Depth: {sol2.maxDepth(root)}")       # Expected: 3
    print(f"DFS Recursive: {sol3.maxDepth(root)}")        # Expected: 3
    
    # Test edge cases
    print(f"Empty tree - BFS: {sol1.maxDepth(None)}")     # Expected: 0
    print(f"Empty tree - DFS: {sol3.maxDepth(None)}")     # Expected: 0
    
    # Test single node
    single = TreeNode(1)
    print(f"Single node - BFS: {sol2.maxDepth(single)}")  # Expected: 1
    print(f"Single node - DFS: {sol3.maxDepth(single)}")  # Expected: 1
    
    # Test deep skewed tree: [1,2,null,3,null,4]
    # Expected: 4
    skewed = TreeNode(1)
    skewed.left = TreeNode(2)
    skewed.left.left = TreeNode(3)
    skewed.left.left.left = TreeNode(4)
    print(f"Skewed tree - BFS: {sol2.maxDepth(skewed)}")  # Expected: 4
    print(f"Skewed tree - DFS: {sol3.maxDepth(skewed)}")  # Expected: 4
    
    # Test wide balanced tree: [1,2,3,4,5,6,7]
    # Expected: 3
    balanced = TreeNode(1)
    balanced.left = TreeNode(2)
    balanced.right = TreeNode(3)
    balanced.left.left = TreeNode(4)
    balanced.left.right = TreeNode(5)
    balanced.right.left = TreeNode(6)
    balanced.right.right = TreeNode(7)
    print(f"Balanced tree - BFS: {sol1.maxDepth(balanced)}")  # Expected: 3
    print(f"Balanced tree - DFS: {sol3.maxDepth(balanced)}")  # Expected: 3


# 1. Start with Solution 1 (BFS level counting) 
# 2. Alternative: Solution 2 (BFS with depth tracking) 
# 3. Preferred: Solution 3 (DFS recursive) 
#
# Key insight: Maximum depth naturally maps to recursive tree structure (height of subtrees + 1)
# Solution 3 is preferred: Most concise, matches problem structure, optimal space for balanced trees
