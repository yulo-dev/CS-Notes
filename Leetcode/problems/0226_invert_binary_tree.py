# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: If the current node is None, nothing to invert
        if not root:
            return None

        # Recursively invert the left and right subtrees
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

         # After both subtrees are processed, swap them
        root.left = right
        root.right = left

        # Return the root with its left and right subtrees inverted
        return root
