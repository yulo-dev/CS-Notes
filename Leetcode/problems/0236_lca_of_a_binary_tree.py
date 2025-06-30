# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If the root is None, or the root is one of the nodes we're looking for,
        # we areturn the root as the LCA (Lowest Common Ancestor)
        if not root or root == p or root == q:
            return root

        # Look for the LCA in the left / right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)


        # If both left and right LCA are non-null, it means one node is in the left
        # subtree and the other is in the right, so root is the LCA
        if left and right:
            return root

         # Otherwise, if one of the LCAs is non-null, return that one
        return left if left else right
