# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Define a helper function to return the height of a subtree
        # If the subtree is unbalanced, return -1 to signal early termination
        def dfs(node):
            if not node:
                return 0  # Base case: the height of an empty tree is 0

            # Recursively get the height of the left subtree
            left = dfs(node.left)
            if left == -1:
                return -1  # Left subtree is unbalanced

            # Recursively get the height of the right subtree
            right = dfs(node.right)
            if right == -1:
                return -1  # Right subtree is unbalanced

            # If the height difference is more than 1, it's not balanced
            if abs(left - right) > 1:
                return -1

            # Return the height of the current subtree
            return 1 + max(left, right)

        # Call the helper function and check if result is -1 (not balanced)
        return dfs(root) != -1
