# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize a global variable to track the maximum diameter found
        self.max_diameter = 0

        def dfs(node):
            # Base case: if the node is None, its height is 0
            if not node:
                return 0

            # Recursively find the height of the left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # At this node, the longest path (diameter) that passes through it
            # is left height + right height (number of edges)
            self.max_diameter = max(self.max_diameter, left + right)

            # Return the height of the current subtree to the parent
            # Height = max of left/right subtree heights + 1 for current node
            return max(left, right) + 1

        # Start DFS from the root
        dfs(root)

        # Return the maximum diameter found during DFS
        return self.max_diameter
