# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function that checks whether the current node is within a valid range
        def dfs(node, lower, upper):
            # Base case: empty node is valid by default
            if not node:
                return True

            # If the current value violates the BST property, return False
            if not (lower < node.val < upper):
                return False

            # Recursively validate the left subtree with updated upper bound
            if not dfs(node.left, lower, node.val):
                return False

            # Recursively validate the right subtree with updated lower bound
            if not dfs(node.right, node.val, upper):
                return False

            # Current node and subtrees are valid
            return True

        # Start recursion with the full valid range
        return dfs(root, float('-inf'), float('inf'))
