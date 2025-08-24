# LeetCode 114: Flatten Binary Tree to Linked List
# Given the root of a binary tree, flatten the tree into a "linked list":
# - The "linked list" should use the same TreeNode class where the right child pointer 
#   points to the next node in the list and the left child pointer is always null.
# - The "linked list" should be in the same order as a pre-order traversal of the binary tree.

from typing import Optional, List

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Brute Force - Store Preorder and Rebuild Tree
# Time: O(n) → Visit each node twice (traverse + rebuild)
# Space: O(n) → Store all node values in list
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # Step 1: Get preorder traversal values
        def preorder(node):
            if not node:
                return []
            result = [node.val]
            result.extend(preorder(node.left))
            result.extend(preorder(node.right))
            return result
        
        values = preorder(root)
        
        # Step 2: Rebuild tree as right-skewed linked list
        current = root
        for i in range(1, len(values)):
            current.left = None
            current.right = TreeNode(values[i])
            current = current.right

# Solution 2: Recursive DFS - Modify Tree Structure In-Place (Classic Solution)
# Time: O(n) → Visit each node exactly once
# Space: O(h) → Recursion stack depth equals tree height
class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            """Returns the tail of the flattened subtree"""
            if not node:
                return None
            
            # Store original left and right children
            left_child = node.left
            right_child = node.right
            
            # Clear left pointer (required for linked list format)
            node.left = None
            
            # Recursively flatten left and right subtrees
            left_tail = dfs(left_child)
            right_tail = dfs(right_child)
            
            # Connect flattened left subtree to current node's right
            if left_child:
                node.right = left_child
                # Connect left subtree tail to flattened right subtree
                left_tail.right = right_child
            
            # Return the actual tail of the flattened tree
            # Priority: right_tail > left_tail > current node
            return right_tail if right_tail else (left_tail if left_tail else node)
        
        dfs(root)

# Solution 3: Advanced - Morris-like Iterative Approach
# Time: O(n) → Visit each node with constant operations
# Space: O(1) → No recursion, only constant extra space
class Solution3:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        
        while current:
            # If current node has left child
            if current.left:
                # Find the rightmost node in left subtree
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                # Connect rightmost node of left subtree to original right subtree
                predecessor.right = current.right
                
                # Move left subtree to right and clear left
                current.right = current.left
                current.left = None
            
            # Move to next node in the flattened structure
            current = current.right

# Alternative Solution using Stack (iterative preorder)
class Solution3_Alternative:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        stack = [root]
        prev = None
        
        while stack:
            current = stack.pop()
            
            # Connect previous node to current
            if prev:
                prev.left = None
                prev.right = current
            
            # Add right child first (since stack is LIFO)
            if current.right:
                stack.append(current.right)
            
            # Add left child second (will be processed first)
            if current.left:
                stack.append(current.left)
            
            prev = current

# Test function
def test_solutions():
    # Create test tree:      1
    #                       / \
    #                      2   5
    #                     / \   \
    #                    3   4   6
    # Expected flattened: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    
    def create_test_tree():
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)
        return root
    
    def print_flattened(root):
        """Print the flattened tree structure"""
        result = []
        current = root
        while current:
            result.append(current.val)
            if current.left:  # Should be None after flattening
                result.append(f"LEFT:{current.left.val}")
            current = current.right
        return result
    
    # Test Solution 2 (Recursive)
    root2 = create_test_tree()
    sol2 = Solution2()
    sol2.flatten(root2)
    print(f"Recursive DFS: {print_flattened(root2)}")  # Expected: [1, 2, 3, 4, 5, 6]
    
    # Test Solution 3 (Morris-like)
    root3 = create_test_tree()
    sol3 = Solution3()
    sol3.flatten(root3)
    print(f"Morris-like: {print_flattened(root3)}")    # Expected: [1, 2, 3, 4, 5, 6]
    
    # Test edge case: single node
    single_node = TreeNode(1)
    sol2_single = Solution2()
    sol2_single.flatten(single_node)
    print(f"Single node: {print_flattened(single_node)}")  # Expected: [1]
    
    # Test edge case: empty tree
    sol2_empty = Solution2()
    sol2_empty.flatten(None)
    print("Empty tree: OK")  # Should not crash

# Strategy:
# 1. Start with Solution 1 (Brute Force) 
# 2. Optimize to Solution 2 (Recursive DFS) 
# 3. If time permits, mention Solution 3 (Morris-like) as space-optimal solution
#
# Key insight: Flatten means convert to right-skewed tree following preorder sequence
# Solution 2 is preferred:
# - In-place modification without extra storage for values
# - Clear recursive structure that handles subtree connections properly
# - Returns tail information needed for proper linking
# - Natural divide-and-conquer approach that's easy to explain
# - Optimal time complexity with reasonable space usage
