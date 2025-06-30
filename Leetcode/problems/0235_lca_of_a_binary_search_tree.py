# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If both target nodes are smaller than the current node,
        # that means they must be in the left subtree.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If both target nodes are greater than the current node,
        # they must be in the right subtree.
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are on different sides of the current node (or one is equal to root),
        # then the current node is their lowest common ancestor.
        else:
            return root
