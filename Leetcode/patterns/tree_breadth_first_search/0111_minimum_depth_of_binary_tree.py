# LeetCode 111: Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth (shortest path from root to any leaf node)

from typing import Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) → In worst case, visit all nodes if tree is completely unbalanced
# Space: O(n) → Recursion stack in worst case (skewed tree)
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # DFS approach - simple but may visit unnecessary nodes
        if not root:
            return 0
        
        # Leaf node case
        if not root.left and not root.right:
            return 1
        
        # If only one child exists, go to that subtree
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # Both children exist, take minimum
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# Time: O(n) → Best case O(w) where w is width of first leaf level, worst case O(n)
# Space: O(n) → Queue stores at most one level worth of nodes (up to n/2 in complete binary tree)
class Solution2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS approach with level tracking - optimal for minimum depth problems
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            for _ in range(len(queue)):
                node, depth = queue.popleft()

                # Found first leaf - this is guaranteed minimum depth
                if not node.left and not node.right:
                    return depth

                # Add children with incremented depth
                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))

# Time: O(w) → Only processes nodes until first leaf level is found
# Space: O(w) → Queue stores nodes level by level
class Solution3:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS with explicit level counter - cleanest level-by-level approach
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            level_size = len(queue)
            
            # Process entire current level
            for _ in range(level_size):
                node = queue.popleft()
                
                # First leaf found at this level
                if not node.left and not node.right:
                    return depth
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

# Test function
def test_solutions():
    # Create test case: [3,9,20,null,null,15,7]
    # Expected: 2 (path: 3 -> 9)
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"DFS: {sol1.minDepth(root)}")          # Expected: 2
    print(f"BFS with tuple: {sol2.minDepth(root)}")  # Expected: 2
    print(f"BFS with counter: {sol3.minDepth(root)}")  # Expected: 2
    
    # Test edge case: empty tree
    print(f"Empty tree - DFS: {sol1.minDepth(None)}")          # Expected: 0
    print(f"Empty tree - BFS tuple: {sol2.minDepth(None)}")    # Expected: 0
    print(f"Empty tree - BFS counter: {sol3.minDepth(None)}")  # Expected: 0
    
    # Test single node
    single = TreeNode(1)
    print(f"Single node - BFS tuple: {sol2.minDepth(single)}")  # Expected: 1
    
    # Test skewed tree: [1,2,null,3,null,4]
    # Expected: 3 (must go to leaf, not just missing child)
    skewed = TreeNode(1)
    skewed.left = TreeNode(2)
    skewed.left.left = TreeNode(3)
    skewed.left.left.left = TreeNode(4)
    print(f"Skewed tree - BFS tuple: {sol2.minDepth(skewed)}")  # Expected: 4
    
    # Test tree where BFS shows advantage: wide tree with early leaf
    # Tree: [1,2,3,4,5,6,7] - leaf at level 3
    advantage = TreeNode(1)
    advantage.left = TreeNode(2)
    advantage.right = TreeNode(3)
    advantage.left.left = TreeNode(4)
    advantage.left.right = TreeNode(5)
    advantage.right.left = TreeNode(6)
    advantage.right.right = TreeNode(7)
    print(f"Wide tree - BFS tuple: {sol2.minDepth(advantage)}")  # Expected: 3

# Key insight: BFS naturally finds shortest path - first leaf encountered is guaranteed minimum depth
