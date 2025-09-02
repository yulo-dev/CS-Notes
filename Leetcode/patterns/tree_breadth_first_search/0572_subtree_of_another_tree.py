# LeetCode 572: Subtree of Another Tree
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot

from typing import Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(m * n) → For each of m nodes in root, potentially compare with n nodes in subRoot
# Space: O(W(root) + W(subRoot)) → O(m + n) worst case, outer and inner BFS queues combined
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # BFS approach - check each node in root as potential subtree match
        if not subRoot:
            return True

        if not root:
            return False

        def same_bfs(a, b):
            # BFS comparison of two trees for identical structure and values
            q = deque([(a, b)])
            while q:
                x, y = q.popleft()
                if not x and not y:  # Both null - continue
                    continue
                if not x or not y:   # One null, one not - not same
                    return False
                if x.val != y.val:   # Different values - not same
                    return False
                q.append((x.left, y.left))
                q.append((x.right, y.right))
            return True

        # Outer BFS: scan all nodes in root
        q = deque([root])
        target = subRoot.val
        while q:
            node = q.popleft()
            # Only check nodes with matching root value for efficiency
            if node.val == target and same_bfs(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False

# Time: O(m * n) → For each of m nodes in root, potentially compare with n nodes in subRoot
# Space: O(H(root) + H(subRoot)) → O(m + n) worst case, recursion stack for both functions
# ★ This is the classic solution ★
class Solution2:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS recursive approach - natural tree traversal with same tree check
        if not subRoot:
            return True
        if not root:
            return False
        if self.same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def same(self, a, b):
        # Two-Tree Comparison Pattern for identical tree check
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return self.same(a.left, b.left) and self.same(a.right, b.right)

# Time: O(m + n) if using KMP for substring search → O(m * n) worst case for naive substring search
# Space: O(m + n) → Store serialized strings for both trees
class Solution3:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # String serialization approach - convert trees to strings and use substring matching
        def serialize(node):
            if not node:
                return "null"
            return f"#{node.val}#,{serialize(node.left)},{serialize(node.right)}"
        
        root_str = serialize(root)
        sub_str = serialize(subRoot)
        
        return sub_str in root_str

# Test function
def test_solutions():
    # Create test case: root=[3,4,5,1,2], subRoot=[4,1,2]
    # Expected: True
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    print(f"BFS Approach: {sol1.isSubtree(root, subRoot)}")         # Expected: True
    print(f"DFS Recursive: {sol2.isSubtree(root, subRoot)}")        # Expected: True
    print(f"String Serialization: {sol3.isSubtree(root, subRoot)}") # Expected: True
    
    # Test case: root=[3,4,5,1,2,null,null,null,null,0], subRoot=[4,1,2]
    # Expected: False (extra 0 node)
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(0)
    
    print(f"False case - BFS: {sol1.isSubtree(root2, subRoot)}")         # Expected: False
    print(f"False case - DFS: {sol2.isSubtree(root2, subRoot)}")         # Expected: False
    print(f"False case - String: {sol3.isSubtree(root2, subRoot)}")      # Expected: False
    
    # Test edge cases
    print(f"Empty subRoot - DFS: {sol2.isSubtree(root, None)}")          # Expected: True
    print(f"Empty root - DFS: {sol2.isSubtree(None, subRoot)}")          # Expected: False


# 1. Start with Solution 1 (BFS) 
# 2. Preferred: Solution 2 (DFS recursive) 
# 3. If time permits, mention Solution 3 (string serialization)
# Key insight: Subtree problem combines tree traversal with tree comparison using Two-Tree Comparison Pattern
# Solution 2 is preferred: Natural recursive approach, clear Two-Tree Comparison Pattern usage
